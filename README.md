# arXiv Embodied AI Paper Digest

Automated paper tracking for embodied AI, world models, VLAs, and robotics research.

## What it does

- Queries arXiv twice daily for papers matching your keywords
- Detects project pages and GitHub links in abstracts/comments
- Generates a markdown digest, prioritizing papers with code/demos
- Commits the digest to this repo automatically

## Quick Setup

### 1. Create your GitHub repo

```bash
# Clone this locally or download the files
git clone <your-repo-url>
cd arxiv-digest
```

### 2. Test locally first

```bash
# No dependencies to install - uses Python standard library
python arxiv_digest.py
```

This creates a `digests/` folder with your first digest.

### 3. Push to GitHub

```bash
git add .
git commit -m "Initial setup"
git push
```

### 4. Enable GitHub Actions

1. Go to your repo on GitHub
2. Click **Settings** → **Actions** → **General**
3. Under "Workflow permissions", select **Read and write permissions**
4. Save

The workflow will now run automatically at 8am and 6pm UTC. You can also trigger it manually from the **Actions** tab.

## Customization

### Edit keywords

Open `arxiv_digest.py` and modify the `KEYWORDS` list:

```python
KEYWORDS = [
    "world model",
    "VLA",
    "embodied AI",
    # Add your own...
]
```

### Edit categories

Modify the `CATEGORIES` list to search different arXiv categories:

```python
CATEGORIES = [
    "cs.RO",  # Robotics
    "cs.CV",  # Computer Vision
    "cs.LG",  # Machine Learning
    "cs.AI",  # Artificial Intelligence
]
```

### Change schedule

Edit `.github/workflows/digest.yml` and modify the cron expressions:

```yaml
schedule:
  - cron: '0 8 * * *'   # 8:00 AM UTC
  - cron: '0 18 * * *'  # 6:00 PM UTC
```

Use [crontab.guru](https://crontab.guru/) to help with cron syntax.

## Output

Digests are saved to the `digests/` folder:
- `digest_YYYY-MM-DD_HHMM.md` - Timestamped archives
- `latest.md` - Always the most recent digest

Papers with project pages or GitHub repos are listed first.

## Future Enhancements

- [ ] Notion database integration
- [ ] Email delivery
- [ ] Hugging Face trending papers integration
- [ ] Paper scoring/ranking system
- [ ] Slack notifications

## License

MIT
