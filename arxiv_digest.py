"""
arXiv Embodied AI Paper Digest

Queries arXiv for recent papers in world models and VLAs,
checks for project pages, and generates category-specific markdown digests.
"""

import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import re
import time
import argparse
from datetime import datetime, timedelta
from pathlib import Path


# =============================================================================
# CONFIGURATION
# =============================================================================

# Define categories with their keywords
CATEGORIES = {
    "world_models": {
        "title": "World Models",
        "description": "Papers on world models for robotics, video prediction, and simulation.",
        "keywords": [
            "world model",
            "world models",
        ],
    },
    "vla": {
        "title": "Vision-Language-Action Models",
        "description": "Papers on VLAs and vision-language-action architectures for robotics.",
        "keywords": [
            "VLA",
            "vision language action",
            "vision-language-action",
        ],
    },
}

# arXiv categories to search within
ARXIV_CATEGORIES = [
    "cs.RO",  # Robotics
    "cs.CV",  # Computer Vision
    "cs.LG",  # Machine Learning
    "cs.AI",  # Artificial Intelligence
]

# How many days back to search (default)
DAYS_BACK = 2

# Max results per query
MAX_RESULTS = 100

# Output directory
OUTPUT_DIR = Path("digests")


# =============================================================================
# ARXIV API FUNCTIONS
# =============================================================================

ARXIV_API_URL = "http://export.arxiv.org/api/query"
ARXIV_NS = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}


def query_arxiv(search_query: str, max_results: int = 50) -> list[dict]:
    """Query arXiv API and return parsed results."""
    
    params = {
        "search_query": search_query,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
        "max_results": max_results,
    }
    
    url = f"{ARXIV_API_URL}?{urllib.parse.urlencode(params)}"
    
    try:
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "arXiv-Digest/1.0 (https://github.com; research paper tracking)"}
        )
        with urllib.request.urlopen(req, timeout=30) as response:
            data = response.read()
    except Exception as e:
        print(f"Error querying arXiv: {e}")
        return []
    
    return parse_arxiv_response(data)


def parse_arxiv_response(xml_data: bytes) -> list[dict]:
    """Parse arXiv API XML response into list of paper dicts."""
    
    root = ET.fromstring(xml_data)
    papers = []
    
    for entry in root.findall("atom:entry", ARXIV_NS):
        paper = {}
        
        # Basic fields
        paper["title"] = clean_text(entry.find("atom:title", ARXIV_NS).text)
        paper["abstract"] = clean_text(entry.find("atom:summary", ARXIV_NS).text)
        paper["published"] = entry.find("atom:published", ARXIV_NS).text[:10]
        paper["updated"] = entry.find("atom:updated", ARXIV_NS).text[:10]
        
        # Get arXiv ID and links
        paper["arxiv_id"] = entry.find("atom:id", ARXIV_NS).text.split("/abs/")[-1]
        paper["arxiv_url"] = f"https://arxiv.org/abs/{paper['arxiv_id']}"
        paper["pdf_url"] = f"https://arxiv.org/pdf/{paper['arxiv_id']}.pdf"
        
        # Authors
        authors = entry.findall("atom:author", ARXIV_NS)
        paper["authors"] = [a.find("atom:name", ARXIV_NS).text for a in authors]
        
        # Categories
        categories = entry.findall("atom:category", ARXIV_NS)
        paper["categories"] = [c.get("term") for c in categories]
        
        # Comment field (often contains project page links)
        comment_elem = entry.find("arxiv:comment", ARXIV_NS)
        paper["comment"] = comment_elem.text if comment_elem is not None else ""
        
        # Check for project page
        paper["project_page"] = find_project_page(paper)
        paper["github_url"] = find_github_url(paper)
        
        papers.append(paper)
    
    return papers


def clean_text(text: str) -> str:
    """Clean up text by removing extra whitespace."""
    if not text:
        return ""
    return " ".join(text.split())


# =============================================================================
# PROJECT PAGE DETECTION
# =============================================================================

def find_project_page(paper: dict) -> str | None:
    """Look for project page URL in abstract or comment."""
    
    patterns = [
        r'project\s*page[:\s]+(\S+)',
        r'project\s*website[:\s]+(\S+)',
        r'homepage[:\s]+(\S+)',
        r'(https?://[^\s]+\.github\.io/[^\s]*)',
        r'(https?://[^\s]+/project[^\s]*)',
        r'webpage[:\s]+(\S+)',
        r'website[:\s]+(\S+)',
        r'code and videos[:\s]+(\S+)',
    ]
    
    text_to_search = f"{paper['abstract']} {paper['comment']}"
    
    for pattern in patterns:
        match = re.search(pattern, text_to_search, re.IGNORECASE)
        if match:
            url = match.group(1).rstrip(".,;)")
            if "arxiv.org" not in url and "github.com" not in url:
                return url
    
    return None


def find_github_url(paper: dict) -> str | None:
    """Look for GitHub URL in abstract or comment."""
    
    text_to_search = f"{paper['abstract']} {paper['comment']}"
    
    pattern = r'(https?://github\.com/[^\s,;)\]]+)'
    match = re.search(pattern, text_to_search, re.IGNORECASE)
    
    if match:
        return match.group(1).rstrip(".,;)")
    
    return None


# =============================================================================
# SEARCH AND FILTER
# =============================================================================

def search_category(category_key: str, category_config: dict, days_back: int) -> list[dict]:
    """Search arXiv for papers matching a specific category's keywords."""
    
    all_papers = {}
    cat_query = " OR ".join([f"cat:{cat}" for cat in ARXIV_CATEGORIES])
    
    for keyword in category_config["keywords"]:
        search_query = f'(ti:"{keyword}" OR abs:"{keyword}") AND ({cat_query})'
        
        print(f"  Searching for: {keyword}")
        papers = query_arxiv(search_query, max_results=MAX_RESULTS)
        print(f"    Found {len(papers)} results")
        
        for paper in papers:
            if paper["arxiv_id"] not in all_papers:
                all_papers[paper["arxiv_id"]] = paper
        
        time.sleep(3)
    
    # Filter by date
    cutoff_date = (datetime.now() - timedelta(days=days_back)).strftime("%Y-%m-%d")
    recent_papers = [
        p for p in all_papers.values()
        if p["published"] >= cutoff_date
    ]
    
    # Sort by date (newest first)
    recent_papers.sort(key=lambda x: x["published"], reverse=True)
    
    return recent_papers


# =============================================================================
# MARKDOWN GENERATION
# =============================================================================

def generate_category_markdown(category_key: str, category_config: dict, papers: list[dict]) -> str:
    """Generate markdown for a single category page."""
    
    now = datetime.now()
    
    lines = [
        f"# {category_config['title']}",
        f"",
        f"{category_config['description']}",
        f"",
        f"**Last updated:** {now.strftime('%Y-%m-%d %H:%M UTC')}",
        f"",
        f"**Papers found:** {len(papers)}",
        f"",
        f"[Back to Home](../README.md)",
        f"",
        f"---",
        f"",
    ]
    
    # Separate papers with and without resources
    papers_with_resources = [p for p in papers if p["project_page"] or p["github_url"]]
    papers_without = [p for p in papers if not p["project_page"] and not p["github_url"]]
    
    if papers_with_resources:
        lines.append("## Papers with Project Pages / Code\n")
        for paper in papers_with_resources:
            lines.extend(format_paper(paper))
    
    if papers_without:
        lines.append("## Other Recent Papers\n")
        for paper in papers_without:
            lines.extend(format_paper(paper))
    
    if not papers:
        lines.append("No papers found matching the criteria.\n")
    
    return "\n".join(lines)


def format_paper(paper: dict) -> list[str]:
    """Format a single paper as markdown."""
    
    lines = []
    
    # Title with link
    lines.append(f"### [{paper['title']}]({paper['arxiv_url']})")
    lines.append("")
    
    # Metadata
    authors_str = ", ".join(paper["authors"][:5])
    if len(paper["authors"]) > 5:
        authors_str += f" et al. ({len(paper['authors'])} authors)"
    
    lines.append(f"**Authors:** {authors_str}")
    lines.append(f"")
    lines.append(f"**Published:** {paper['published']} | **Categories:** {', '.join(paper['categories'][:3])}")
    lines.append("")
    
    # Links
    links = [f"[arXiv]({paper['arxiv_url']})", f"[PDF]({paper['pdf_url']})"]
    
    if paper["project_page"]:
        links.append(f"[Project Page]({paper['project_page']})")
    
    if paper["github_url"]:
        links.append(f"[GitHub]({paper['github_url']})")
    
    lines.append(f"**Links:** {' | '.join(links)}")
    lines.append("")
    
    # Abstract (truncated)
    abstract = paper["abstract"]
    if len(abstract) > 500:
        abstract = abstract[:500] + "..."
    
    lines.append(f"<details>")
    lines.append(f"<summary>Abstract</summary>")
    lines.append(f"")
    lines.append(f"{abstract}")
    lines.append(f"")
    lines.append(f"</details>")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    return lines


def generate_readme_template(category_counts: dict) -> str:
    """Generate the README landing page template."""
    
    now = datetime.now()
    
    readme = f"""# Embodied AI Paper Tracker

Automated tracking of research papers in world models and vision-language-action models for robotics.

**Last updated:** {now.strftime('%Y-%m-%d %H:%M UTC')}

---

## Highlighted Papers

<!-- Add your manually curated highlights here -->

| Paper | Source | Why it's interesting |
|-------|--------|---------------------|
| [pi0.5](https://www.physicalintelligence.company/blog/pi0-5) | Physical Intelligence | Latest foundation model for general-purpose robotics |
| <!-- Add more rows --> | | |

---

## Categories

| Category | Papers | Link |
|----------|--------|------|
| World Models | {category_counts.get('world_models', 0)} | [View all](digests/world_models.md) |
| Vision-Language-Action | {category_counts.get('vla', 0)} | [View all](digests/vla.md) |

---

## About

This tracker automatically queries arXiv twice daily for new papers matching keywords related to:

- **World Models**: world model, world models
- **VLA**: VLA, vision language action, vision-language-action

Papers with project pages or GitHub repositories are highlighted in each category.

### Want to add a paper?

Edit this README and add it to the Highlighted Papers table above.

### Setup

See [SETUP.md](SETUP.md) for instructions on running your own instance.
"""
    
    return readme


def generate_setup_doc() -> str:
    """Generate setup documentation."""
    
    return """# Setup Instructions

## Quick Start

1. Fork this repository
2. Enable GitHub Actions (Settings > Actions > General > Allow all actions)
3. Set workflow permissions to "Read and write" (Settings > Actions > General > Workflow permissions)
4. The digest will run automatically at 8am and 6pm UTC

## Manual Run

```bash
# Install Python 3.10+
python arxiv_digest.py

# Run with custom lookback period
python arxiv_digest.py --days 30
```

## Customization

Edit `arxiv_digest.py` to modify:

- `CATEGORIES`: Add/remove keyword groups
- `ARXIV_CATEGORIES`: Change which arXiv categories to search
- `DAYS_BACK`: Default lookback period
- `MAX_RESULTS`: Results per keyword query

## Schedule

Edit `.github/workflows/digest.yml` to change the run schedule:

```yaml
schedule:
  - cron: '0 8 * * *'   # 8:00 AM UTC
  - cron: '0 18 * * *'  # 6:00 PM UTC
```
"""


# =============================================================================
# MAIN
# =============================================================================

def main():
    parser = argparse.ArgumentParser(description="arXiv Embodied AI Paper Digest")
    parser.add_argument("--days", type=int, default=DAYS_BACK, 
                        help=f"Number of days back to search (default: {DAYS_BACK})")
    args = parser.parse_args()
    
    print("=" * 60)
    print("arXiv Embodied AI Paper Digest")
    print("=" * 60)
    print(f"Looking back {args.days} days")
    print()
    
    # Ensure output directory exists
    OUTPUT_DIR.mkdir(exist_ok=True)
    
    category_counts = {}
    
    # Process each category
    for category_key, category_config in CATEGORIES.items():
        print(f"\n[{category_config['title']}]")
        
        # Search for papers
        papers = search_category(category_key, category_config, args.days)
        category_counts[category_key] = len(papers)
        print(f"  Total: {len(papers)} papers")
        
        # Generate and save markdown
        markdown = generate_category_markdown(category_key, category_config, papers)
        output_file = OUTPUT_DIR / f"{category_key}.md"
        output_file.write_text(markdown, encoding='utf-8')
        print(f"  Saved: {output_file}")
    
    # Generate README if it doesn't exist or update counts
    readme_path = Path("README.md")
    if not readme_path.exists():
        readme = generate_readme_template(category_counts)
        readme_path.write_text(readme, encoding='utf-8')
        print(f"\nCreated: {readme_path}")
    else:
        print(f"\nREADME.md exists - not overwriting (edit manually)")
    
    # Generate setup doc
    setup_path = Path("SETUP.md")
    if not setup_path.exists():
        setup_path.write_text(generate_setup_doc(), encoding='utf-8')
        print(f"Created: {setup_path}")
    
    print("\nDone!")
    
    return category_counts


if __name__ == "__main__":
    main()
