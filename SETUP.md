# Setup Instructions

## Quick Start

1. Fork this repository.
2. Enable GitHub Actions (Settings > Actions > General > Allow all actions).
3. Set workflow permissions to "Read and write" (Settings > Actions > General > Workflow permissions).
4. Enable GitHub Pages: Settings > Pages > Build and deployment > Deploy from a branch >
   `main` / `/docs`. The dashboard is then served at
   `https://<you>.github.io/<repo>/` (for this repo:
   https://jonstephens85.github.io/awesome-embodied-ai/).
5. The digest runs automatically at 8am and 2pm PST (16:00 / 22:00 UTC), and on manual dispatch.

## Manual Run

```bash
pip install -r requirements-dev.txt   # for the tests only; the script itself is stdlib

python arxiv_digest.py                 # last 7 days
python arxiv_digest.py --days 30       # custom lookback
python arxiv_digest.py --allow-partial # tolerate arXiv API failures instead of erroring

pytest -q                             # run the test suite
```

## Customization (`arxiv_digest.py`)

- `CATEGORIES` - per topic:
  - `keywords` - phrases queried against arXiv title/abstract (plural- and
    hyphen-insensitive when matched locally)
  - `require_any` - if non-empty, at least one must appear in the title/abstract
    (precision filter for broad terms like "world model")
  - `exclude_any` - any match disqualifies the paper
  - `hashtags` - appended to the copy-paste share snippet
- `ARXIV_CATEGORIES` - arXiv subject categories to search (`cs.RO`, `cs.CV`, ...).
- `DAYS_BACK` - default lookback window.
- `MIN_SCORE` - hide papers below this relevance score.

## Outputs

- `digests/<topic>.md` - one ranked page per topic, partitioned by each paper's
  primary (highest-scoring) topic.
- `digests/latest.md` - combined "new since last run" feed across all topics.
- `digests/seen.json` - state: arXiv IDs seen so far, used to compute "new"
  (auto-pruned after 365 days). Committed by CI.
- `docs/index.html` + `docs/papers.json` - the dashboard and its data feed.
  `docs/papers.json` lists every in-window paper once, tagged with all matching topics.

## Schedule

Edit `.github/workflows/digest.yml`:

```yaml
schedule:
  - cron: '0 16 * * *'  # 8:00 AM PST
  - cron: '0 22 * * *'  # 2:00 PM PST
```
