# Setup Instructions

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
  - cron: '0 8 * * *'   # 8:00 AM PST
  - cron: '0 18 * * *'  # 2:00 PM PST
```
