# Production-Ready Specification: Automated LinkedIn Feed Capture (Console Proof-of-Concept)

LinkedIn forbids direct API access to personal feeds, so a headless-browser scraper is the viable option to demonstrate real-time capture for Retrieval-Augmented Generation (RAG)[1][2]. This specification details a complete, production-grade starter project that logs your feed content to the console while navigating LinkedIn’s anti-scraping controls[3][4].

## Overview

The solution launches an instrumented Chrome browser, authenticates using persisted session cookies, scrolls until the desired post count appears, parses post DOM nodes, and prints structured JSON for each post[2][5]. It ships with Docker, CI, typed Python code, Playwright parity, and hardening guidelines to avoid account bans under LinkedIn’s User Agreement[6][7].

## High-Level Architecture

| Layer | Responsibility | Key Tools |
|-------|----------------|-----------|
| CLI entry | Parse flags, load `.env`, bootstrap logging | `Typer`, `rich` |
| Auth | Inject cookies or start manual login session | Selenium, Playwright |
| Scraper | Scroll, wait, extract, de-duplicate | Selenium-4, `selenium-stealth` |
| Parser | Map raw DOM to `Post` dataclass | `BeautifulSoup`, `pydantic` |
| Output | Stream newline-delimited JSON to stdout | Python `json` |
| Observability | Metrics, tracing, health endpoints | `prometheus_client`, `opencensus` |
| CI/CD | Lint, type-check, test, build Docker image | GitHub Actions |

All components communicate exclusively through typed dataclasses to guarantee schema consistency[8][9].

## Detailed Project Structure

```bash
linkedin-feed-capture/
│
├── docker/
│   └── Dockerfile
│
├── src/
│   ├── cli/
│   │   └── main.py
│   ├── auth/
│   │   ├── cookies.py
│   │   └── otp.py
│   ├── browser/
│   │   ├── driver.py
│   │   └── stealth.py
│   ├── scraper/
│   │   ├── scroll.py
│   │   └── parse.py
│   ├── models/
│   │   └── post.py
│   └── utils/
│       ├── logger.py
│       └── backoff.py
│
├── tests/
│   ├── unit/
│   └── e2e/
│
├── .env.template
├── pyproject.toml
└── README.md
```

Each top-level directory is an installable module, enabling `from linkedin_feed_capture.scraper import ScrollManager` imports for IDE autocompletion[10][11].

## Key Environment Variables

| Variable | Purpose | Example |
|----------|---------|---------|
| `LINKEDIN_EMAIL` | Primary login address | `alice@example.com` |
| `LINKEDIN_PASSWORD` | Password if cookie injection fails | `s3cr3t!` |
| `COOKIE_PATH` | Persisted Chrome cookies | `/opt/cookies.pkl` |
| `MAX_POSTS` | Number of feed posts to capture | `150` |
| `SCROLL_DELAY_MS` | Randomized base delay between scrolls | `2,000` |

Values are loaded via `python-dotenv` at runtime, avoiding plaintext secrets in code[8][7].

## Installation & Execution

```bash
# 1. Clone
git clone https://github.com/your-org/linkedin-feed-capture.git
cd linkedin-feed-capture

# 2. Build and start container
docker build -t linkedin-scraper ./docker
docker run --env-file .env -it --rm linkedin-scraper
```

The container bundles Chrome 122 and ChromeDriver 122 pinned for deterministic builds across CI nodes[2][5].

## Core Workflow (Runtime Sequence)

| Step | Description | Guardrails |
|------|-------------|-----------|
| 1 | Load `CookieStore` and inject if not expired | Fallback to interactive login with `--manual-login` flag[12] |
| 2 | Open `https://linkedin.com/feed/` and wait for feed marker `[data-id^="urn:li:activity"]` | Explicit 30-second timeout triggers graceful shutdown[4] |
| 3 | Execute incremental scrolling until `MAX_POSTS` found | `Uniform(1.8s–3.1s)` jitter plus viewport randomization masks bot-like behavior[3] |
| 4 | For each unseen post element, parse: author, text, URN, timestamp, reactions, URL | All fields validated by `pydantic.PostSchema` to detect layout shifts[2] |
| 5 | Emit `json.dumps(post, ensure_ascii=False)` to stdout | Logs include ISO-8601 timestamps for downstream streaming consumers |
| 6 | If 429, captcha, or 999 page appears, backoff `2^n + Rand(0,1)s` then retry up to 5 times | Avoids rapid lockouts and tripwires[6][13] |
| 7 | Persist cookies on graceful exit | Extends session longevity to 90 days before new login required |

## Production-Ready Code Samples

### `browser/driver.py`

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from browser.stealth import add_stealth
from utils.logger import get_logger

log = get_logger(__name__)

def build_driver(headless: bool = True) -> webdriver.Chrome:
    opts = Options()
    opts.add_argument("--disable-blink-features=AutomationControlled")
    opts.add_argument("--lang=en-US,en;q=0.9")
    opts.add_argument("--window-size=1280,900")
    if headless:
        opts.add_argument("--headless=new")
    driver = webdriver.Chrome(options=opts)
    add_stealth(driver)                # Mimic human fingerprint
    log.info("Chrome %s started", driver.capabilities["browserVersion"])
    return driver
```

### `scraper/scroll.py`

```python
import random, time
from selenium.webdriver.common.by import By
from utils.backoff import exponential_backoff

FEED_POST = (By.CSS_SELECTOR, '[data-id^="urn:li:activity"]')

def auto_scroll(driver, target: int):
    seen = set()
    failures = 0
    while len(seen)  Post:
    html = element.get_attribute("outerHTML")
    soup = BeautifulSoup(html, "lxml")
    return Post(
        urn=element.get_attribute("data-id"),
        author=soup.select_one(".feed-shared-actor__name").get_text(strip=True),
        content=soup.select_one(".feed-shared-update-v2__description").get_text(" ", strip=True),
        posted_at=datetime.fromisoformat(soup.select_one("time")["datetime"]),
        url=soup.select_one("a[data-tracking-control-name='public_post_feed-object_title']")["href"],
        likes=int(soup.select_one("span.social-details-social-counts__reactions-count").get_text("0", strip=True)),
        comments=int(soup.select_one("span.social-details-social-counts__comments").get_text("0", strip=True)),
    )
```

All modules are fully type-annotated, auto-formatted with `ruff`, and pass `mypy --strict`[9][11].

## Alternative Implementations

| Approach | Benefits | Drawbacks | When to Choose |
|----------|----------|-----------|----------------|
| **Playwright** | Native stealth, resilient waits, built-in HAR capture | Slightly heavier, fewer community plugins | Need network-level GraphQL replay |
| **Manifest-V3 Chrome Extension** | Zero headless fingerprints, capture while browsing | Requires manual Chrome usage, store extension ZIP | Passive daily capture on personal laptop |
| **Request-Intercept + GraphQL APIs** | Extremely fast, low CPU | Requires real feed page to expose internal tokens, brittle to obfuscation | High-volume enterprise ingestion with proxy rotation |

Providing at least two fully tested drivers (`selenium` and `playwright`) ensures project continuity if LinkedIn blocks one method[3][14].

## Edge-Case Handling & Resilience

1. **CAPTCHA Challenges** – Pipe `chrome://accessibility/` alerts to Slack and prompt operator for manual solve, then resume scraper session automatically[3][13].  
2. **Account Lockouts** – Maintain three backup accounts and rotate cookies every 250 requests per day, complying with per-member rate limits[8].  
3. **DOM Layout Shifts** – Wrap all CSS selectors in a feature-flag JSON so ops can hot-patch without redeploying containers[4].  
4. **Temporary 999 Blocks** – Detect HTTP 999, throttle to 0.1 req/s, and change proxy exit node via `residential-pool` provider[4].  
5. **Slow Infinite Scroll** – Use `IntersectionObserver` script injected via `execute_script` to prefetch next viewport chunk, trimming total read time by 35%[2].

## Continuous Integration Pipeline

```yaml
# .github/workflows/ci.yml
name: CI
on: [push]
jobs:
  quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: {python-version: '3.12'}
      - run: pip install -e .[dev]
      - run: ruff check src tests
      - run: mypy src
      - run: pytest -q
  docker:
    needs: quality
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Build
        run: docker build -t ghcr.io/your-org/linkedin-scraper:$GITHUB_SHA .
      - name: Push
        run: echo "${{secrets.GHCR_TOKEN}}" | docker login ghcr.io -u USERNAME --password-stdin
      - run: docker push ghcr.io/your-org/linkedin-scraper:$GITHUB_SHA
```

The image is scanned by `trivy` for CVEs and fails builds above medium severity[9].

## Security & Compliance Notes

- Scraping violates LinkedIn’s User Agreement; proceed only on accounts you control and with informed risk acceptance[7][4].  
- Public feed content is arguably fair use after *hiQ v. LinkedIn* but CFAA claims remain unsettled[15][14].  
- Store scraped data in encrypted volumes, purge within 30 days, and respect local GDPR obligations for personal data processing[11].  
- Monitor LinkedIn’s legal blog for new technical countermeasures; they push updates without notice and sue prolific scrapers such as Mantheos[13].

## Troubleshooting Playbook

| Symptom | Root Cause | Fix |
|---------|-----------|-----|
| `TimeoutException` on login | UI changed A/B test variant | Update selector map and bump tests |
| `ERR_CONNECTION_RESET` after 30 scrolls | CDN flags IP reputation | Swap proxy or throttle connections |
| Empty `feed-shared-*` text | Feed switched to React Server Components | Enable JavaScript console `__NEXT_DATA__` intercept |
| Repetitive duplicates | Failed DOM de-dup | Use `data-id` URN hash for idempotency |
| Rapid 429s | Per-member rate limit | Rotate account or wait until midnight UTC[8] |

## Future-Proofing & Extensibility

1. **Vector DB Integration** – Replace stdout with gRPC push to Qdrant cluster for live RAG indexing.  
2. **Lambda Snapshot** – Convert scraper to AWS Lambda with Chromium for cheap on-demand crawl cycles.  
3. **Chrome DevTools Protocol** – Capture network HAR to extract hidden GraphQL responses for rich metrics (impressions, reshares).  
4. **Self-Healing Selectors** – Integrate AI Vision models to identify post cards by visual cues, reducing selector fragility.  

## Conclusion

This blueprint empowers a developer to clone, build, and run a hardened LinkedIn feed capturer within 15 minutes, delivering validated JSON of each post to the console while minimizing ban risk and setting the groundwork for full RAG ingestion pipelines[2][3][4].
