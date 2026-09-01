"""
arXiv Embodied AI Paper Digest

Queries arXiv for recent papers on egocentric data, vision-language-action models,
and world models; scores them with deterministic relevance rules; and generates:

  - digests/<topic>.md      one ranked Markdown page per topic
  - digests/latest.md       a combined "new since last run" feed
  - digests/seen.json       minimal state tracking which arXiv IDs we've seen
  - docs/index.html         a static dashboard (GitHub Pages, /docs)
  - docs/papers.json        machine-readable feed backing the dashboard
"""

import argparse
import json
import re
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path


# =============================================================================
# CONFIGURATION
# =============================================================================

# Topics, in priority order. Each topic defines:
#   keywords     - exact phrases queried against arXiv title/abstract
#   require_any  - if non-empty, at least one must appear in title+abstract
#                  (a cheap precision filter for broad terms like "world model")
#   exclude_any  - any match in title+abstract disqualifies the paper
#   hashtags     - appended to the copy-paste social share snippet
CATEGORIES = {
    "egocentric_data": {
        "title": "Egocentric Data",
        "description": "Papers on egocentric / first-person video datasets and learning "
                       "robot or embodied skills from human-centric data.",
        "hashtags": ["#egocentric", "#robotlearning"],
        "keywords": [
            "egocentric video",
            "egocentric dataset",
            "egocentric data",
            "egocentric perception",
            "egocentric human",
            "egocentric demonstration",
            "egocentric human video",
            "first-person video",
            "human video data",
            "Ego4D",
            "EgoExo",
            "Ego-Exo",
        ],
        "require_any": [],
        "exclude_any": [
            "electroencephalog", "social network analysis", "gaussian splatting",
            "video restoration", "scene-text", "text-centric",
        ],
    },
    "vla": {
        "title": "Vision-Language-Action Models",
        "description": "Papers on VLAs and vision-language-action architectures for robotics.",
        "hashtags": ["#VLA", "#robotics"],
        "keywords": [
            "VLA",
            "vision-language-action",
            "vision-language-action model",
        ],
        "require_any": [],
        "exclude_any": [],
    },
    "world_models": {
        "title": "World Models",
        "description": "Papers on world models for robotics, video prediction, "
                       "interactive simulation, and planning.",
        "hashtags": ["#worldmodels", "#robotics"],
        "keywords": [
            "world model",
            "world simulator",
            "interactive world model",
            "action-conditioned video",
        ],
        "require_any": [
            "robot", "embodied", "manipulation", "navigation", "autonomous driving",
            "simulation", "simulator", "video prediction", "video generation",
            "physical", "3d scene", "occupancy", "trajectory", "planning",
            "game", "interactive environment", "dreamer", "jepa", "genie",
            "action-conditioned", "future frame", "dynamics model",
        ],
        "exclude_any": [
            "limit order book", "order book", "electronic health record",
            "clinical", "patient", "physiological", "radiolog", "econometr",
            "portfolio", "stock market", "genomic", "advertising",
            "recommendation", "object detection", "text-centric",
        ],
    },
}

TOPIC_ORDER = list(CATEGORIES)

# arXiv subject categories to search within
ARXIV_CATEGORIES = [
    "cs.RO",  # Robotics
    "cs.CV",  # Computer Vision
    "cs.LG",  # Machine Learning
    "cs.AI",  # Artificial Intelligence
]

# How many days back to search (default)
DAYS_BACK = 7

# Results per API page (arXiv recommends <= 100 with start-based paging)
PAGE_SIZE = 100

# Safety cap on pages fetched per keyword query
MAX_PAGES = 10

# Minimum relevance score for a paper to be shown
MIN_SCORE = 2.0

# Courtesy delay between arXiv API requests (seconds)
REQUEST_DELAY = 3

# Retry backoff schedule (seconds) for a failing arXiv request
RETRY_BACKOFF = [5, 15, 45]

# Prune seen.json entries older than this many days
SEEN_TTL_DAYS = 365

# Output locations
OUTPUT_DIR = Path("digests")
SEEN_FILE = OUTPUT_DIR / "seen.json"
DOCS_DIR = Path("docs")


# =============================================================================
# ARXIV API
# =============================================================================

ARXIV_API_URL = "https://export.arxiv.org/api/query"
ARXIV_NS = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}


def query_arxiv(search_query: str, start: int = 0, page_size: int = PAGE_SIZE,
                allow_partial: bool = False) -> list[dict]:
    """Fetch one page of arXiv results, retrying transient failures.

    Raises RuntimeError after exhausting retries unless allow_partial is set,
    in which case an empty list is returned.
    """
    params = {
        "search_query": search_query,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
        "start": start,
        "max_results": page_size,
    }
    url = f"{ARXIV_API_URL}?{urllib.parse.urlencode(params)}"

    last_err = None
    for attempt in range(len(RETRY_BACKOFF) + 1):
        try:
            req = urllib.request.Request(
                url,
                headers={"User-Agent": "arxiv-embodied-digest/2.0 "
                                        "(https://github.com; research paper tracking)"},
            )
            with urllib.request.urlopen(req, timeout=45) as response:
                data = response.read()
            return parse_arxiv_response(data)
        except Exception as e:  # noqa: BLE001 - network/XML errors are all retryable here
            last_err = e
            if attempt < len(RETRY_BACKOFF):
                wait = RETRY_BACKOFF[attempt]
                print(f"    ! arXiv request failed ({e}); retrying in {wait}s")
                time.sleep(wait)

    msg = f"arXiv request failed after {len(RETRY_BACKOFF) + 1} attempts: {last_err}"
    if allow_partial:
        print(f"    ! {msg} -- continuing with partial results (--allow-partial)")
        return []
    raise RuntimeError(msg)


def _text(entry: ET.Element, tag: str, default: str = "") -> str:
    """Safely read the text of a child element."""
    el = entry.find(tag, ARXIV_NS)
    if el is None or el.text is None:
        return default
    return el.text


def strip_version(arxiv_id: str) -> str:
    """Drop a trailing version suffix, e.g. '2608.27079v2' -> '2608.27079'."""
    return re.sub(r"v\d+$", "", arxiv_id.strip())


def parse_arxiv_response(xml_data: bytes) -> list[dict]:
    """Parse an arXiv API XML response into a list of paper dicts.

    Malformed entries are skipped with a warning rather than aborting the run.
    """
    try:
        root = ET.fromstring(xml_data)
    except ET.ParseError as e:
        raise RuntimeError(f"could not parse arXiv XML response: {e}") from e

    papers = []
    for entry in root.findall("atom:entry", ARXIV_NS):
        try:
            raw_id = _text(entry, "atom:id").split("/abs/")[-1].strip()
            if not raw_id:
                continue
            base_id = strip_version(raw_id)

            title = clean_text(_text(entry, "atom:title"))
            abstract = clean_text(_text(entry, "atom:summary"))
            if not title:
                continue

            comment_el = entry.find("arxiv:comment", ARXIV_NS)
            comment = clean_text(comment_el.text) if comment_el is not None and comment_el.text else ""

            authors = []
            for a in entry.findall("atom:author", ARXIV_NS):
                name_el = a.find("atom:name", ARXIV_NS)
                if name_el is not None and name_el.text and name_el.text.strip():
                    authors.append(name_el.text.strip())

            categories = [c.get("term") for c in entry.findall("atom:category", ARXIV_NS)
                          if c.get("term")]

            paper = {
                "arxiv_id": raw_id,
                "base_id": base_id,
                "title": title,
                "abstract": abstract,
                "comment": comment,
                "authors": authors,
                "categories": categories,
                "published": _text(entry, "atom:published")[:10],
                "updated": _text(entry, "atom:updated")[:10],
                "arxiv_url": f"https://arxiv.org/abs/{base_id}",
                "pdf_url": f"https://arxiv.org/pdf/{base_id}",
            }
            paper["project_page"] = find_project_page(paper)
            paper["github_url"] = find_github_url(paper)
            papers.append(paper)
        except Exception as e:  # noqa: BLE001
            print(f"    ! skipping malformed entry: {e}")
            continue

    return papers


def clean_text(text: str) -> str:
    """Collapse whitespace."""
    if not text:
        return ""
    return " ".join(text.split())


# =============================================================================
# PROJECT PAGE / CODE DETECTION
# =============================================================================

_URL_RE = re.compile(r"^https?://[^\s]+\.[^\s]+$")
_HREF_RE = re.compile(r"\\href\s*\{([^}]*)\}")
_GITHUB_RE = re.compile(r"https?://github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)", re.IGNORECASE)
_BAD_REPO_TOKENS = ("awesome", "survey", "list", "paperswithcode", "template")


def _clean_url(candidate: str) -> str | None:
    """Strip wrapping punctuation / LaTeX and validate that this is a real URL."""
    if not candidate:
        return None
    candidate = candidate.strip().strip("{}()[]<>\"'`")
    candidate = candidate.rstrip(".,;:)]}>\"'`\\")
    # unwrap a stray \href{url}{...}
    m = _HREF_RE.search(candidate)
    if m:
        candidate = m.group(1).strip().strip("{}()[]<>\"'`")
    if not _URL_RE.match(candidate):
        return None
    return candidate


def find_project_page(paper: dict) -> str | None:
    """Find a project / demo page URL in the abstract or comment."""
    text = f"{paper['abstract']} {paper['comment']}"

    # 1) explicit \href{...} targets that aren't arXiv/GitHub
    for m in _HREF_RE.finditer(text):
        url = _clean_url(m.group(1))
        if url and "arxiv.org" not in url and "github.com" not in url:
            return url

    # 2) labelled links
    label_patterns = [
        r"project\s*page[:\s]+(\S+)",
        r"project\s*website[:\s]+(\S+)",
        r"project\s*site[:\s]+(\S+)",
        r"more\s+(?:results|videos)\s+(?:at|on)[:\s]+(\S+)",
        r"videos?\s+(?:and|&)\s+code\s+(?:at|on)[:\s]+(\S+)",
        r"code\s+(?:and|&)\s+videos?\s+(?:at|on)[:\s]+(\S+)",
        r"home\s*page[:\s]+(\S+)",
        r"webpage[:\s]+(\S+)",
        r"website[:\s]+(\S+)",
    ]
    for pat in label_patterns:
        m = re.search(pat, text, re.IGNORECASE)
        if m:
            url = _clean_url(m.group(1))
            if url and "arxiv.org" not in url and "github.com" not in url:
                return url

    # 3) bare github.io / project-style URLs
    for m in re.finditer(r"(https?://[^\s]+)", text):
        url = _clean_url(m.group(1))
        if not url or "arxiv.org" in url or "github.com" in url:
            continue
        if "github.io" in url or "/project" in url or "pages.dev" in url:
            return url

    return None


def _title_tokens(title: str) -> set[str]:
    return {t.lower() for t in re.findall(r"[A-Za-z0-9]+", title) if len(t) >= 4}


def find_github_url(paper: dict) -> str | None:
    """Find the paper's own GitHub repository (comment field preferred)."""
    title_tokens = _title_tokens(paper["title"])

    for source in (paper["comment"], paper["abstract"]):
        matches = list(_GITHUB_RE.finditer(source))
        if not matches:
            continue

        candidates = []
        for m in matches:
            owner, repo = m.group(1), m.group(2)
            repo = repo.rstrip(".,;:)]}>\"'`")
            slug = f"{owner}/{repo}".lower()
            if any(tok in slug for tok in _BAD_REPO_TOKENS):
                continue
            candidates.append((f"https://github.com/{owner}/{repo}", slug))

        if not candidates:
            continue

        for url, slug in candidates:
            if title_tokens & set(re.findall(r"[a-z0-9]+", slug)):
                return url
        return candidates[-1][0]

    return None


# =============================================================================
# RELEVANCE FILTER + SCORING (deterministic)
# =============================================================================

def _norm(text: str) -> str:
    """Lowercase and treat hyphens/underscores/whitespace runs as a single space."""
    return re.sub(r"[-_\s]+", " ", text.lower())


def _term_present(term: str, norm_text: str) -> bool:
    """Whole-word match, hyphen-insensitive, tolerating a trailing plural 's'."""
    return re.search(r"\b" + re.escape(_norm(term)) + r"s?\b", norm_text) is not None


def _keyword_hits(paper: dict, cfg: dict) -> tuple[list[str], list[str]]:
    """Return (keywords matched in title, keywords matched only in abstract)."""
    title = _norm(paper["title"])
    abstract = _norm(paper["abstract"])
    in_title, in_abs = [], []
    for kw in cfg["keywords"]:
        if _term_present(kw, title):
            in_title.append(kw)
        elif _term_present(kw, abstract):
            in_abs.append(kw)
    return in_title, in_abs


def passes_relevance(paper: dict, cfg: dict) -> bool:
    in_title, in_abs = _keyword_hits(paper, cfg)
    if not (in_title or in_abs):
        return False
    text = _norm(f"{paper['title']} {paper['abstract']}")
    if cfg["require_any"] and not any(_term_present(t, text) for t in cfg["require_any"]):
        return False
    if any(_term_present(t, text) for t in cfg["exclude_any"]):
        return False
    return True


def score_paper(paper: dict, cfg: dict, two_days_ago: str) -> tuple[float, list[str]]:
    in_title, in_abs = _keyword_hits(paper, cfg)
    title = _norm(paper["title"])

    score = 0.0
    reasons: list[str] = []

    if in_title:
        score += 3
        reasons.append(f'"{in_title[0]}" in title')
    elif in_abs:
        score += 2
        reasons.append(f'"{in_abs[0]}" in abstract')

    # distinct keywords ignoring trivial singular/plural pairs
    distinct = {kw.rstrip("s") for kw in in_title + in_abs}
    extra = len(distinct) - 1
    if extra > 0:
        score += min(2, extra)
        reasons.append(f"{len(distinct)} distinct keyword hits")

    if paper["project_page"]:
        score += 2
        reasons.append("project page")
    if paper["github_url"]:
        score += 2
        reasons.append("code repo")

    req_title = [t for t in cfg["require_any"] if _term_present(t, title)]
    if req_title:
        score += min(2, len(req_title))
        reasons.append("robotics / embodied focus")

    if "cs.RO" in paper["categories"]:
        score += 0.5

    if paper["published"] >= two_days_ago:
        score += 1
        reasons.append("posted in last 2 days")

    return round(score, 1), reasons


# =============================================================================
# SEARCH
# =============================================================================

def _fetch_window(search_query: str, cutoff_date: str, allow_partial: bool) -> list[dict]:
    """Page through a query (newest first) until results fall outside the window."""
    collected: list[dict] = []
    for page in range(MAX_PAGES):
        start = page * PAGE_SIZE
        batch = query_arxiv(search_query, start=start, allow_partial=allow_partial)
        if not batch:
            break
        collected.extend(batch)
        # results are sorted by submission date descending
        if batch[-1]["published"] < cutoff_date:
            break
        if len(batch) < PAGE_SIZE:
            break
        time.sleep(REQUEST_DELAY)
    return collected


def search_category(topic_key: str, cfg: dict, days_back: int,
                    now: datetime, allow_partial: bool) -> list[dict]:
    """Search arXiv for one topic and return scored, filtered, ranked papers."""
    cutoff_date = (now - timedelta(days=days_back)).strftime("%Y-%m-%d")
    two_days_ago = (now - timedelta(days=2)).strftime("%Y-%m-%d")
    cat_query = " OR ".join(f"cat:{c}" for c in ARXIV_CATEGORIES)

    found: dict[str, dict] = {}
    for keyword in cfg["keywords"]:
        query = f'(ti:"{keyword}" OR abs:"{keyword}") AND ({cat_query})'
        print(f"  searching: {keyword}")
        papers = _fetch_window(query, cutoff_date, allow_partial)
        print(f"    {len(papers)} raw results")
        for p in papers:
            found.setdefault(p["base_id"], p)
        time.sleep(REQUEST_DELAY)

    ranked = []
    for p in found.values():
        if p["published"] < cutoff_date:
            continue
        if not passes_relevance(p, cfg):
            continue
        score, reasons = score_paper(p, cfg, two_days_ago)
        if score < MIN_SCORE:
            continue
        entry = dict(p)
        entry["score"] = score
        entry["match_reasons"] = reasons
        ranked.append(entry)

    ranked.sort(key=lambda x: (x["score"], x["published"]), reverse=True)
    print(f"  -> {len(ranked)} relevant papers")
    return ranked


# =============================================================================
# STATE (seen.json)
# =============================================================================

def load_seen() -> dict:
    if not SEEN_FILE.exists():
        return {}
    try:
        return json.loads(SEEN_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as e:
        print(f"! could not read {SEEN_FILE} ({e}); starting fresh")
        return {}


def save_seen(seen: dict, now: datetime) -> None:
    cutoff = (now - timedelta(days=SEEN_TTL_DAYS)).strftime("%Y-%m-%d")
    pruned = {k: v for k, v in seen.items() if v.get("first_seen", "9999") >= cutoff}
    SEEN_FILE.write_text(json.dumps(pruned, indent=2, sort_keys=True, ensure_ascii=False),
                         encoding="utf-8")


# =============================================================================
# MARKDOWN GENERATION
# =============================================================================

def relevance_stars(score: float) -> str:
    filled = max(1, min(5, round(score / 2)))
    return "★" * filled + "☆" * (5 - filled)


def share_text(paper: dict, cfg: dict) -> str:
    abstract = paper["abstract"]
    hook = re.split(r"(?<=[.!?])\s+", abstract.strip())[0] if abstract else ""
    if len(hook) > 220:
        hook = hook[:217].rstrip() + "..."
    lines = [paper["title"]]
    if hook:
        lines += ["", hook]
    lines += ["", f"arXiv: {paper['arxiv_url']}"]
    if paper["project_page"]:
        lines.append(f"Project page: {paper['project_page']}")
    if paper["github_url"]:
        lines.append(f"Code: {paper['github_url']}")
    lines += ["", " ".join(cfg["hashtags"])]
    return "\n".join(lines)


def format_paper(paper: dict, cfg: dict, also_topics: list[str]) -> list[str]:
    lines = [f"### [{paper['title']}]({paper['arxiv_url']})", ""]

    authors = ", ".join(paper["authors"][:5])
    if len(paper["authors"]) > 5:
        authors += f" et al. ({len(paper['authors'])} authors)"
    lines.append(f"**Authors:** {authors or 'n/a'}")
    lines.append("")

    published = f"**Published:** {paper['published']}"
    if paper["updated"] and paper["updated"] != paper["published"]:
        published += f" (updated {paper['updated']})"
    cats = ", ".join(paper["categories"][:3])
    lines.append(f"{published} | **Categories:** {cats} | **Relevance:** {relevance_stars(paper['score'])}")
    lines.append("")

    if paper["match_reasons"]:
        lines.append(f"**Why surfaced:** {'; '.join(paper['match_reasons'])}")
        lines.append("")

    if also_topics:
        pretty = ", ".join(CATEGORIES[t]["title"] for t in also_topics)
        lines.append(f"**Also relevant to:** {pretty}")
        lines.append("")

    links = [f"[arXiv]({paper['arxiv_url']})", f"[PDF]({paper['pdf_url']})"]
    if paper["project_page"]:
        links.append(f"[Project Page]({paper['project_page']})")
    if paper["github_url"]:
        links.append(f"[Code]({paper['github_url']})")
    marker = " 🔗" if (paper["project_page"] or paper["github_url"]) else ""
    lines.append(f"**Links:**{marker} {' | '.join(links)}")
    lines.append("")

    abstract = paper["abstract"]
    if len(abstract) > 600:
        abstract = abstract[:600].rstrip() + "..."
    lines += ["<details>", "<summary>Abstract</summary>", "", abstract, "", "</details>", ""]

    lines += ["<details>", "<summary>Share</summary>", "", "```", share_text(paper, cfg), "```",
              "", "</details>", "", "---", ""]
    return lines


def generate_category_markdown(topic_key: str, cfg: dict, papers: list[dict],
                               also_map: dict[str, list[str]], now: datetime) -> str:
    lines = [
        f"# {cfg['title']}",
        "",
        cfg["description"],
        "",
        f"**Last updated:** {now.strftime('%Y-%m-%d %H:%M UTC')}",
        "",
        f"**Papers shown:** {len(papers)} (relevance \u2265 {MIN_SCORE:g}, "
        f"last {DAYS_BACK} days)",
        "",
        "[Dashboard](../docs/index.html) \u00b7 [What's new](latest.md) \u00b7 "
        "[Back to Home](../README.md)",
        "",
        "---",
        "",
    ]
    if not papers:
        lines.append("_No papers matched the criteria this run._")
        return "\n".join(lines)

    for paper in papers:
        lines.extend(format_paper(paper, cfg, also_map.get(paper["base_id"], [])))
    return "\n".join(lines)


def generate_latest_markdown(new_by_topic: dict[str, list[dict]],
                             also_map: dict[str, list[str]], now: datetime) -> str:
    total = sum(len(v) for v in new_by_topic.values())
    lines = [
        "# What's New",
        "",
        f"Papers discovered in the run at **{now.strftime('%Y-%m-%d %H:%M UTC')}**.",
        "",
        f"**New this run:** {total}",
        "",
        "[Dashboard](../docs/index.html) \u00b7 [Back to Home](../README.md)",
        "",
        "---",
        "",
    ]
    if not total:
        lines.append("_Nothing new since the last run._")
        return "\n".join(lines)

    for topic_key in TOPIC_ORDER:
        papers = new_by_topic.get(topic_key, [])
        if not papers:
            continue
        cfg = CATEGORIES[topic_key]
        lines += [f"## {cfg['title']} ({len(papers)})", ""]
        for paper in papers:
            lines.extend(format_paper(paper, cfg, also_map.get(paper["base_id"], [])))
    return "\n".join(lines)


# =============================================================================
# DASHBOARD (docs/)
# =============================================================================

DASHBOARD_HTML = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Embodied AI Paper Dashboard</title>
<style>
  :root {
    --bg: #f6f7f9; --card: #ffffff; --text: #14171a; --muted: #5b6470;
    --border: #e2e5ea; --accent: #2f6feb; --accent-fg: #ffffff; --new: #1a7f37;
    --chip: #eef1f5;
  }
  @media (prefers-color-scheme: dark) {
    :root {
      --bg: #0f1216; --card: #171b21; --text: #e6e9ee; --muted: #9aa4b2;
      --border: #2a2f37; --accent: #4c8dff; --accent-fg: #0f1216; --new: #3fb950;
      --chip: #232832;
    }
  }
  * { box-sizing: border-box; }
  body { margin: 0; background: var(--bg); color: var(--text);
         font: 15px/1.5 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
  header { padding: 24px 20px 12px; max-width: 960px; margin: 0 auto; }
  h1 { font-size: 22px; margin: 0 0 4px; }
  .sub { color: var(--muted); font-size: 13px; }
  .bar { position: sticky; top: 0; z-index: 5; background: var(--bg);
         border-bottom: 1px solid var(--border); padding: 12px 20px; }
  .bar-inner { max-width: 960px; margin: 0 auto; display: flex; flex-wrap: wrap;
               gap: 8px; align-items: center; }
  .pill, .toggle, select, input[type=search] {
    font: inherit; border: 1px solid var(--border); background: var(--card);
    color: var(--text); border-radius: 999px; padding: 6px 12px; cursor: pointer; }
  input[type=search] { border-radius: 8px; flex: 1 1 180px; cursor: text; }
  select { border-radius: 8px; cursor: pointer; }
  .pill.active, .toggle.active { background: var(--accent); color: var(--accent-fg);
                                 border-color: var(--accent); }
  main { max-width: 960px; margin: 0 auto; padding: 16px 20px 60px; }
  .count { color: var(--muted); font-size: 13px; margin: 4px 0 12px; }
  .card { background: var(--card); border: 1px solid var(--border); border-radius: 12px;
          padding: 16px; margin-bottom: 12px; }
  .card h2 { font-size: 16px; margin: 0 0 6px; }
  .card h2 a { color: var(--text); text-decoration: none; }
  .card h2 a:hover { text-decoration: underline; }
  .meta { color: var(--muted); font-size: 12.5px; margin-bottom: 8px; }
  .chips { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 8px; }
  .chip { background: var(--chip); border-radius: 999px; padding: 2px 9px; font-size: 12px; }
  .chip.topic { border: 1px solid var(--border); }
  .chip.topic.primary { border-color: var(--accent); color: var(--accent); font-weight: 600; }
  .chip.new { background: var(--new); color: #fff; }
  .abstract { font-size: 14px; color: var(--text); margin: 6px 0; }
  .abstract[hidden] { display: none; }
  .links { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 8px; }
  .links a, .links button {
    font: inherit; font-size: 13px; text-decoration: none; border: 1px solid var(--border);
    background: var(--card); color: var(--accent); border-radius: 8px; padding: 5px 10px;
    cursor: pointer; }
  .stars { letter-spacing: 1px; }
  .empty { text-align: center; color: var(--muted); padding: 48px 0; }
  code.share { display: none; }
</style>
</head>
<body>
<header>
  <h1>Embodied AI Paper Dashboard</h1>
  <div class="sub" id="summary">Loading&hellip;</div>
</header>
<div class="bar">
  <div class="bar-inner">
    <span id="topics"></span>
    <button class="toggle" data-flag="new">New this run</button>
    <button class="toggle" data-flag="code">Has code / page</button>
    <input type="search" id="q" placeholder="Search title &amp; abstract&hellip;">
    <select id="sort">
      <option value="relevance">Sort: Relevance</option>
      <option value="published">Sort: Newest</option>
      <option value="first_seen">Sort: Recently added</option>
    </select>
    <button class="toggle" id="markseen" title="Hide NEW badges on this device">Mark all seen</button>
  </div>
</div>
<main>
  <div class="count" id="count"></div>
  <div id="list"></div>
</main>
<script>
const STORE = "embodied-dash";
let state = { topic: "all", flags: {}, q: "", sort: "relevance" };
try { Object.assign(state, JSON.parse(localStorage.getItem(STORE) || "{}")); } catch (e) {}
let DATA = { papers: [], topics: {}, generated: "", window_days: 7 };
let seenLocal = {};
try { seenLocal = JSON.parse(localStorage.getItem(STORE + "-seen") || "{}"); } catch (e) {}

function persist() { try { localStorage.setItem(STORE, JSON.stringify(state)); } catch (e) {} }
function esc(s) { return (s || "").replace(/[&<>"]/g, c => ({ "&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;" }[c])); }

function render() {
  const topicsEl = document.getElementById("topics");
  const pills = [["all", "All"]].concat(Object.keys(DATA.topics).map(k => [k, DATA.topics[k].title]));
  topicsEl.innerHTML = pills.map(([k, label]) =>
    `<button class="pill ${state.topic === k ? "active" : ""}" data-topic="${k}">${esc(label)}</button>`).join(" ");
  topicsEl.querySelectorAll("button").forEach(b => b.onclick = () => {
    state.topic = b.dataset.topic; persist(); render();
  });
  document.querySelectorAll(".toggle[data-flag]").forEach(b => {
    b.classList.toggle("active", !!state.flags[b.dataset.flag]);
    b.onclick = () => { state.flags[b.dataset.flag] = !state.flags[b.dataset.flag]; persist(); render(); };
  });
  document.getElementById("q").value = state.q;
  document.getElementById("sort").value = state.sort;

  const q = state.q.trim().toLowerCase();
  let rows = DATA.papers.filter(p => {
    if (state.topic !== "all" && !p.topics.includes(state.topic)) return false;
    if (state.flags.new && (!p.is_new || seenLocal[p.id])) return false;
    if (state.flags.code && !p.project_page && !p.github_url) return false;
    if (q && !(p.title.toLowerCase().includes(q) || p.abstract.toLowerCase().includes(q))) return false;
    return true;
  });
  rows.sort((a, b) => {
    if (state.sort === "relevance") return b.score - a.score || b.published.localeCompare(a.published);
    if (state.sort === "published") return b.published.localeCompare(a.published) || b.score - a.score;
    return (b.first_seen || "").localeCompare(a.first_seen || "") || b.score - a.score;
  });

  document.getElementById("count").textContent =
    `${rows.length} paper${rows.length === 1 ? "" : "s"}`;
  const list = document.getElementById("list");
  if (!rows.length) { list.innerHTML = `<div class="empty">No papers match these filters.</div>`; return; }

  list.innerHTML = rows.map((p, i) => {
    const stars = "\u2605".repeat(Math.max(1, Math.min(5, Math.round(p.score / 2))))
      + "\u2606".repeat(5 - Math.max(1, Math.min(5, Math.round(p.score / 2))));
    const isNew = p.is_new && !seenLocal[p.id];
    const topicChips = p.topics.map(t =>
      `<span class="chip topic${t === p.primary_topic ? " primary" : ""}">${esc((DATA.topics[t] || {}).title || t)}</span>`).join("");
    const reasons = (p.match_reasons || []).map(r => `<span class="chip">${esc(r)}</span>`).join("");
    const auth = p.authors.slice(0, 5).join(", ") + (p.authors.length > 5 ? ` et al. (${p.authors.length})` : "");
    const links = [
      `<a href="${esc(p.arxiv_url)}" target="_blank" rel="noopener">arXiv</a>`,
      `<a href="${esc(p.pdf_url)}" target="_blank" rel="noopener">PDF</a>`,
      p.project_page ? `<a href="${esc(p.project_page)}" target="_blank" rel="noopener">Project</a>` : "",
      p.github_url ? `<a href="${esc(p.github_url)}" target="_blank" rel="noopener">Code</a>` : "",
      `<button data-copy="${i}">Copy share text</button>`,
    ].filter(Boolean).join("");
    return `<article class="card">
      <h2><a href="${esc(p.arxiv_url)}" target="_blank" rel="noopener">${esc(p.title)}</a></h2>
      <div class="meta">${esc(auth || "n/a")} &middot; ${esc(p.published)}${p.updated && p.updated !== p.published ? " (upd " + esc(p.updated) + ")" : ""} &middot; <span class="stars">${stars}</span></div>
      <div class="chips">
        ${isNew ? `<span class="chip new">NEW</span>` : ""}
        ${topicChips}${reasons}
      </div>
      <button class="links" data-toggle="${i}" style="border:none;background:none;padding:0;color:var(--accent);cursor:pointer">Show abstract</button>
      <div class="abstract" id="abs-${i}" hidden>${esc(p.abstract)}</div>
      <div class="links">${links}</div>
      <code class="share" id="share-${i}">${esc(p.share_text)}</code>
    </article>`;
  }).join("");

  list.querySelectorAll("[data-toggle]").forEach(b => b.onclick = () => {
    const el = document.getElementById("abs-" + b.dataset.toggle);
    el.hidden = !el.hidden; b.textContent = el.hidden ? "Show abstract" : "Hide abstract";
  });
  list.querySelectorAll("[data-copy]").forEach(b => b.onclick = async () => {
    const txt = document.getElementById("share-" + b.dataset.copy).textContent;
    try { await navigator.clipboard.writeText(txt); b.textContent = "Copied!";
      setTimeout(() => b.textContent = "Copy share text", 1500); } catch (e) { b.textContent = "Copy failed"; }
  });
}

document.getElementById("q").addEventListener("input", e => { state.q = e.target.value; persist(); render(); });
document.getElementById("sort").addEventListener("change", e => { state.sort = e.target.value; persist(); render(); });
document.getElementById("markseen").onclick = () => {
  DATA.papers.forEach(p => { if (p.is_new) seenLocal[p.id] = 1; });
  try { localStorage.setItem(STORE + "-seen", JSON.stringify(seenLocal)); } catch (e) {}
  render();
};

fetch("papers.json").then(r => r.json()).then(d => {
  DATA = d;
  const newCount = d.papers.filter(p => p.is_new).length;
  document.getElementById("summary").textContent =
    `${d.papers.length} papers over the last ${d.window_days} days \u00b7 ${newCount} new this run \u00b7 updated ${d.generated}`;
  render();
}).catch(e => {
  document.getElementById("summary").textContent = "Could not load papers.json";
  document.getElementById("list").innerHTML = `<div class="empty">${esc(String(e))}</div>`;
});
</script>
</body>
</html>
"""


def render_dashboard(papers: list[dict], now: datetime, window_days: int) -> None:
    DOCS_DIR.mkdir(exist_ok=True)
    topics_meta = {}
    for key in TOPIC_ORDER:
        cfg = CATEGORIES[key]
        count = sum(1 for p in papers if key in p["topics"])
        topics_meta[key] = {"title": cfg["title"], "count": count}

    feed = {
        "generated": now.strftime("%Y-%m-%d %H:%M UTC"),
        "window_days": window_days,
        "topics": topics_meta,
        "papers": [
            {
                "id": p["base_id"],
                "title": p["title"],
                "authors": p["authors"],
                "published": p["published"],
                "updated": p["updated"],
                "topics": p["topics"],
                "primary_topic": p["primary_topic"],
                "score": p["score"],
                "match_reasons": p["match_reasons"],
                "abstract": p["abstract"],
                "arxiv_url": p["arxiv_url"],
                "pdf_url": p["pdf_url"],
                "project_page": p["project_page"],
                "github_url": p["github_url"],
                "first_seen": p["first_seen"],
                "is_new": p["is_new"],
                "share_text": share_text(p, CATEGORIES[p["primary_topic"]]),
            }
            for p in papers
        ],
    }
    (DOCS_DIR / "papers.json").write_text(
        json.dumps(feed, indent=2, ensure_ascii=False), encoding="utf-8")
    (DOCS_DIR / "index.html").write_text(DASHBOARD_HTML, encoding="utf-8")
    (DOCS_DIR / ".nojekyll").write_text("", encoding="utf-8")


# =============================================================================
# TEMPLATES (only written on a fresh checkout)
# =============================================================================

def generate_readme_template(counts: dict) -> str:
    now = datetime.now(timezone.utc)
    rows = "\n".join(
        f"| {CATEGORIES[k]['title']} | {counts.get(k, 0)} | [View](digests/{k}.md) |"
        for k in TOPIC_ORDER
    )
    return f"""# Embodied AI Paper Tracker

Automated arXiv tracking for egocentric data, vision-language-action models, and world models.

**Last updated:** {now.strftime('%Y-%m-%d %H:%M UTC')}

- **[Dashboard](docs/index.html)** - filter, search, and grab share text
- **[What's new](digests/latest.md)** - papers found in the latest run

---

## Topics

| Topic | Papers | Link |
|-------|--------|------|
{rows}

---

See [SETUP.md](SETUP.md) to run your own instance.
"""


def generate_setup_doc() -> str:
    return """# Setup Instructions

## Quick Start

1. Fork this repository.
2. Enable GitHub Actions (Settings > Actions > General > Allow all actions).
3. Set workflow permissions to "Read and write" (Settings > Actions > General).
4. Enable GitHub Pages: Settings > Pages > Build and deployment > Deploy from a
   branch > `main` / `/docs`. The dashboard will be served at
   `https://<you>.github.io/<repo>/`.
5. The digest runs automatically at 08:00 and 18:00 UTC.

## Manual Run

```bash
python arxiv_digest.py                 # last 7 days
python arxiv_digest.py --days 30       # custom lookback
python arxiv_digest.py --allow-partial # tolerate arXiv API failures
```

## Customization (`arxiv_digest.py`)

- `CATEGORIES` - per-topic `keywords`, `require_any` (precision filter),
  `exclude_any` (hard blocklist), and `hashtags` for the share snippet.
- `ARXIV_CATEGORIES` - arXiv subject categories to search.
- `DAYS_BACK` - default lookback window.
- `MIN_SCORE` - hide papers below this relevance score.

## Outputs

- `digests/<topic>.md` - one ranked page per topic (partitioned by primary topic).
- `digests/latest.md` - combined "new since last run" feed.
- `digests/seen.json` - state: which arXiv IDs have been seen (auto-pruned).
- `docs/index.html` + `docs/papers.json` - the dashboard and its data.

## Schedule

Edit `.github/workflows/digest.yml`:

```yaml
schedule:
  - cron: '0 16 * * *'  # 8:00 AM PST
  - cron: '0 22 * * *'  # 2:00 PM PST
```
"""


# =============================================================================
# MAIN
# =============================================================================

def main():
    parser = argparse.ArgumentParser(description="arXiv Embodied AI Paper Digest")
    parser.add_argument("--days", type=int, default=DAYS_BACK,
                        help=f"days back to search (default: {DAYS_BACK})")
    parser.add_argument("--allow-partial", action="store_true",
                        help="continue even if some arXiv requests fail")
    args = parser.parse_args()

    now = datetime.now(timezone.utc)
    today = now.strftime("%Y-%m-%d")

    print("=" * 60)
    print(f"arXiv Embodied AI Paper Digest - {now.strftime('%Y-%m-%d %H:%M UTC')}")
    print(f"Looking back {args.days} days")
    print("=" * 60)

    OUTPUT_DIR.mkdir(exist_ok=True)
    seen = load_seen()
    seen_before = set(seen)

    # 1. search each topic
    per_topic: dict[str, list[dict]] = {}
    for topic_key, cfg in CATEGORIES.items():
        print(f"\n[{cfg['title']}]")
        per_topic[topic_key] = search_category(topic_key, cfg, args.days, now, args.allow_partial)

    # 2. merge across topics (one record per base_id)
    merged: dict[str, dict] = {}
    for topic_key in TOPIC_ORDER:
        for p in per_topic[topic_key]:
            rec = merged.get(p["base_id"])
            if rec is None:
                rec = dict(p)
                rec["topics"] = []
                rec["topic_scores"] = {}
                merged[p["base_id"]] = rec
            rec["topics"].append(topic_key)
            rec["topic_scores"][topic_key] = p["score"]
            # keep the highest-scoring view's score/reasons on the merged record
            if p["score"] >= rec["score"]:
                rec["score"] = p["score"]
                rec["match_reasons"] = p["match_reasons"]

    # 3. primary topic (highest score, TOPIC_ORDER as tie-break) + newness
    for rec in merged.values():
        rec["primary_topic"] = min(
            rec["topics"], key=lambda t: (-rec["topic_scores"][t], TOPIC_ORDER.index(t)))
        rec["is_new"] = rec["base_id"] not in seen_before
        rec["first_seen"] = seen.get(rec["base_id"], {}).get("first_seen", today)

    also_map = {
        bid: [t for t in rec["topics"] if t != rec["primary_topic"]]
        for bid, rec in merged.items()
    }

    # 4. update state
    for bid, rec in merged.items():
        seen[bid] = {
            "first_seen": rec["first_seen"],
            "title": rec["title"],
            "topics": rec["topics"],
        }
    save_seen(seen, now)

    # 5. per-topic digests (partitioned by primary topic)
    counts = {}
    by_primary: dict[str, list[dict]] = {k: [] for k in TOPIC_ORDER}
    for rec in merged.values():
        by_primary[rec["primary_topic"]].append(rec)
    for topic_key in TOPIC_ORDER:
        papers = sorted(by_primary[topic_key],
                        key=lambda x: (x["score"], x["published"]), reverse=True)
        counts[topic_key] = len(papers)
        md = generate_category_markdown(topic_key, CATEGORIES[topic_key], papers, also_map, now)
        (OUTPUT_DIR / f"{topic_key}.md").write_text(md, encoding="utf-8")
        print(f"  wrote digests/{topic_key}.md ({len(papers)} papers)")

    # 6. "what's new" feed
    new_by_topic: dict[str, list[dict]] = {k: [] for k in TOPIC_ORDER}
    for rec in merged.values():
        if rec["is_new"]:
            new_by_topic[rec["primary_topic"]].append(rec)
    for k in new_by_topic:
        new_by_topic[k].sort(key=lambda x: (x["score"], x["published"]), reverse=True)
    (OUTPUT_DIR / "latest.md").write_text(
        generate_latest_markdown(new_by_topic, also_map, now), encoding="utf-8")
    new_total = sum(len(v) for v in new_by_topic.values())
    print(f"  wrote digests/latest.md ({new_total} new)")

    # 7. dashboard
    dash_papers = sorted(merged.values(),
                         key=lambda x: (x["score"], x["published"]), reverse=True)
    render_dashboard(dash_papers, now, args.days)
    print(f"  wrote docs/index.html + docs/papers.json ({len(dash_papers)} papers)")

    # 8. templates only if missing
    readme = Path("README.md")
    if not readme.exists():
        readme.write_text(generate_readme_template(counts), encoding="utf-8")
        print("  created README.md")
    setup = Path("SETUP.md")
    if not setup.exists():
        setup.write_text(generate_setup_doc(), encoding="utf-8")
        print("  created SETUP.md")

    print("\nDone.")
    return counts


if __name__ == "__main__":
    main()
