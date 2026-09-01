"""Tests for arxiv_digest.py (offline; no network)."""

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import arxiv_digest as ad


# --------------------------------------------------------------------------- #
# helpers
# --------------------------------------------------------------------------- #

def make_paper(**over):
    base = {
        "arxiv_id": "2608.12345v1",
        "base_id": "2608.12345",
        "title": "A Paper",
        "abstract": "An abstract.",
        "comment": "",
        "authors": ["Ada Lovelace"],
        "categories": ["cs.RO"],
        "published": "2000-01-01",
        "updated": "2000-01-01",
        "arxiv_url": "https://arxiv.org/abs/2608.12345",
        "pdf_url": "https://arxiv.org/pdf/2608.12345",
        "project_page": None,
        "github_url": None,
    }
    base.update(over)
    return base


# --------------------------------------------------------------------------- #
# text utilities
# --------------------------------------------------------------------------- #

def test_clean_text_collapses_whitespace():
    assert ad.clean_text("  a\n b\t c ") == "a b c"
    assert ad.clean_text("") == ""
    assert ad.clean_text(None) == ""


@pytest.mark.parametrize("raw,expected", [
    ("2608.27079v2", "2608.27079"),
    ("2608.27079", "2608.27079"),
    ("2608.27079v13", "2608.27079"),
    ("cs/0601001v1", "cs/0601001"),
])
def test_strip_version(raw, expected):
    assert ad.strip_version(raw) == expected


# --------------------------------------------------------------------------- #
# project page extraction
# --------------------------------------------------------------------------- #

def test_find_project_page_plain_url():
    p = make_paper(abstract="See our project page: https://cool-project.github.io/ for videos.")
    assert ad.find_project_page(p) == "https://cool-project.github.io/"


def test_find_project_page_unwraps_href():
    p = make_paper(abstract=r"Project page \href{https://foo.github.io/bar}{https://foo.github.io/bar}.")
    assert ad.find_project_page(p) == "https://foo.github.io/bar"


def test_find_project_page_rejects_bare_words():
    # "code and videos are available at http://..." previously captured "at"/"is"
    p = make_paper(abstract="All code and videos are available at our website. It is great.")
    assert ad.find_project_page(p) in (None, "http://our", )  # never "at" or "is"
    assert ad.find_project_page(p) != "at"
    assert ad.find_project_page(p) != "is"


def test_find_project_page_strips_trailing_punctuation():
    p = make_paper(comment="Homepage: https://example.com/proj/page).")
    assert ad.find_project_page(p) == "https://example.com/proj/page"


def test_find_project_page_ignores_arxiv_and_github():
    p = make_paper(abstract="Website: https://arxiv.org/abs/1234.5678 and https://github.com/a/b")
    assert ad.find_project_page(p) is None


# --------------------------------------------------------------------------- #
# github extraction
# --------------------------------------------------------------------------- #

def test_find_github_prefers_comment_over_abstract():
    p = make_paper(
        title="RoboWidget: Learning to Grasp",
        abstract="We build on https://github.com/someone/baseline-code for comparison.",
        comment="Code: https://github.com/lab/robowidget",
    )
    assert ad.find_github_url(p) == "https://github.com/lab/robowidget"


def test_find_github_skips_awesome_lists():
    p = make_paper(
        title="A Survey of World Models",
        abstract="Curated at https://github.com/foo/Awesome-World-Models and code at "
                 "https://github.com/foo/wm-release",
    )
    assert ad.find_github_url(p) == "https://github.com/foo/wm-release"


def test_find_github_prefers_title_token_match():
    p = make_paper(
        title="DreamFlow: Fast World Models",
        abstract="Baselines from https://github.com/x/other-repo . Ours: "
                 "https://github.com/x/dreamflow .",
    )
    assert ad.find_github_url(p) == "https://github.com/x/dreamflow"


def test_find_github_none_when_absent():
    assert ad.find_github_url(make_paper(abstract="no links here")) is None


# --------------------------------------------------------------------------- #
# relevance filter
# --------------------------------------------------------------------------- #

WM = ad.CATEGORIES["world_models"]
VLA = ad.CATEGORIES["vla"]


def test_passes_relevance_keeps_robotics_world_model():
    p = make_paper(
        title="A World Model for Robot Manipulation",
        abstract="We train a world model for a robot arm doing manipulation tasks.",
    )
    assert ad.passes_relevance(p, WM) is True


def test_passes_relevance_drops_finance_world_model():
    p = make_paper(
        title="An LLM World Model of a Limit Order Book",
        abstract="We study whether a large language model builds an implicit world model "
                 "of the limit order book from synthetic market data.",
    )
    assert ad.passes_relevance(p, WM) is False


def test_passes_relevance_drops_clinical_world_model():
    p = make_paper(
        title="Implicit Medical World Models",
        abstract="We probe whether language models act as implicit world models for "
                 "clinical patient trajectories.",
    )
    assert ad.passes_relevance(p, WM) is False


def test_passes_relevance_requires_keyword():
    p = make_paper(title="Robot Manipulation with Diffusion", abstract="No matching phrase.")
    assert ad.passes_relevance(p, WM) is False


# --------------------------------------------------------------------------- #
# scoring
# --------------------------------------------------------------------------- #

def test_score_title_hit_beats_abstract_hit():
    in_title = make_paper(title="Vision-Language-Action Models for Robots",
                          abstract="robots", categories=[])
    in_abs = make_paper(title="A Robot Policy",
                        abstract="We present a vision-language-action model.", categories=[])
    s_title, _ = ad.score_paper(in_title, VLA, "1900-01-01")
    s_abs, _ = ad.score_paper(in_abs, VLA, "1900-01-01")
    assert s_title > s_abs


def test_score_project_page_and_repo_boost_ordering():
    plain = make_paper(title="A VLA study", abstract="vla", categories=[])
    with_code = make_paper(title="A VLA study", abstract="vla", categories=[],
                           project_page="https://x.github.io", github_url="https://github.com/x/y")
    s_plain, _ = ad.score_paper(plain, VLA, "1900-01-01")
    s_code, reasons = ad.score_paper(with_code, VLA, "1900-01-01")
    assert s_code >= s_plain + 4
    assert "project page" in reasons and "code repo" in reasons


def test_score_recency_bonus():
    p = make_paper(title="VLA", abstract="vla", categories=[], published="2026-08-30")
    old = make_paper(title="VLA", abstract="vla", categories=[], published="2020-01-01")
    s_new, _ = ad.score_paper(p, VLA, "2026-08-29")
    s_old, _ = ad.score_paper(old, VLA, "2026-08-29")
    assert s_new == s_old + 1


# --------------------------------------------------------------------------- #
# XML parsing
# --------------------------------------------------------------------------- #

SAMPLE_XML = b"""<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom" xmlns:arxiv="http://arxiv.org/schemas/atom">
  <entry>
    <id>http://arxiv.org/abs/2608.11111v1</id>
    <title>Good Paper One</title>
    <summary>  Abstract with   spaces.  Project page: https://one.github.io/  </summary>
    <published>2026-08-27T00:00:00Z</published>
    <updated>2026-08-28T00:00:00Z</updated>
    <author><name>Alice A</name></author>
    <author><name>Bob B</name></author>
    <category term="cs.RO"/>
    <category term="cs.AI"/>
    <arxiv:comment>Code: https://github.com/lab/goodpaper</arxiv:comment>
  </entry>
  <entry>
    <id>http://arxiv.org/abs/2608.22222v2</id>
    <title>Good Paper Two</title>
    <summary>Another abstract.</summary>
    <published>2026-08-25T00:00:00Z</published>
    <updated>2026-08-25T00:00:00Z</updated>
    <author><name>Carol C</name></author>
    <category term="cs.LG"/>
  </entry>
  <entry>
    <id>http://arxiv.org/abs/2608.33333v1</id>
    <summary>Malformed: no title element.</summary>
    <published>2026-08-24T00:00:00Z</published>
  </entry>
</feed>
"""


def test_parse_arxiv_response_parses_and_skips_malformed():
    papers = ad.parse_arxiv_response(SAMPLE_XML)
    assert [p["base_id"] for p in papers] == ["2608.11111", "2608.22222"]

    one = papers[0]
    assert one["title"] == "Good Paper One"
    assert one["abstract"] == "Abstract with spaces. Project page: https://one.github.io/"
    assert one["authors"] == ["Alice A", "Bob B"]
    assert one["categories"] == ["cs.RO", "cs.AI"]
    assert one["published"] == "2026-08-27"
    assert one["updated"] == "2026-08-28"
    assert one["arxiv_url"] == "https://arxiv.org/abs/2608.11111"
    assert one["project_page"] == "https://one.github.io/"
    assert one["github_url"] == "https://github.com/lab/goodpaper"


def test_parse_arxiv_response_bad_xml_raises():
    with pytest.raises(RuntimeError):
        ad.parse_arxiv_response(b"<not-xml")


# --------------------------------------------------------------------------- #
# date-window paging
# --------------------------------------------------------------------------- #

def test_fetch_window_stops_when_out_of_window(monkeypatch):
    pages = [
        [make_paper(base_id=f"a{i}", published="2026-08-30") for i in range(ad.PAGE_SIZE)],
        [make_paper(base_id=f"b{i}", published="2026-08-20") for i in range(ad.PAGE_SIZE)],
        [make_paper(base_id=f"c{i}", published="2026-07-01") for i in range(ad.PAGE_SIZE)],
    ]
    calls = []

    def fake_query(q, start=0, allow_partial=False):
        calls.append(start)
        idx = start // ad.PAGE_SIZE
        return pages[idx] if idx < len(pages) else []

    monkeypatch.setattr(ad, "query_arxiv", fake_query)
    monkeypatch.setattr(ad.time, "sleep", lambda *_: None)

    out = ad._fetch_window("q", cutoff_date="2026-08-24", allow_partial=False)
    # page 0 newest ok -> page 1 last item (08-20) < cutoff -> stop
    assert calls == [0, ad.PAGE_SIZE]
    assert len(out) == 2 * ad.PAGE_SIZE


# --------------------------------------------------------------------------- #
# dashboard rendering
# --------------------------------------------------------------------------- #

def test_render_dashboard_writes_valid_feed(tmp_path, monkeypatch):
    monkeypatch.setattr(ad, "DOCS_DIR", tmp_path / "docs")
    now = ad.datetime(2026, 8, 31, 12, 0, tzinfo=ad.timezone.utc)
    papers = [make_paper(
        title="VLA Paper", abstract="A vision-language-action model.", score=8.0,
        match_reasons=["\"VLA\" in title"], topics=["vla"], primary_topic="vla",
        first_seen="2026-08-31", is_new=True,
    )]
    ad.render_dashboard(papers, now, window_days=7)

    feed = json.loads((tmp_path / "docs" / "papers.json").read_text(encoding="utf-8"))
    assert feed["window_days"] == 7
    assert set(feed["topics"]) == set(ad.TOPIC_ORDER)
    assert feed["papers"][0]["id"] == "2608.12345"
    assert feed["papers"][0]["is_new"] is True
    assert "VLA Paper" in feed["papers"][0]["share_text"]
    assert (tmp_path / "docs" / "index.html").read_text(encoding="utf-8").startswith("<!doctype html>")
    assert (tmp_path / "docs" / ".nojekyll").exists()
