# Async News & Crypto Dashboard

A terminal dashboard that concurrently fetches live crypto prices (CoinGecko)
and top news headlines (NewsAPI), with disk caching, retry/backoff logic,
and clean error handling — built to exercise `asyncio`/`aiohttp`, `requests`,
`.env` config, and a proper multi-module project layout.

## Features

- **Concurrent fetching** — crypto and news requests run at the same time via
  `asyncio.gather`, not one after another.
- **Retry with exponential backoff** — transient errors and HTTP 429 (rate
  limit) responses are retried automatically before giving up.
- **JSON disk cache** — responses are cached in `data/cache.json` with a
  configurable TTL, so re-running the dashboard within the TTL window doesn't
  spend another API call.
- **Graceful degradation** — if the news API key is missing or a call fails
  after all retries, the dashboard still renders whatever data it *does*
  have instead of crashing.
- **Config via `.env`** — all secrets and tunables live in environment
  variables, loaded once in `config.py`.

## Project structure

```
my_project/
├── .env                   # your secrets (never commit — git-ignored)
├── .env.example           # template showing which variables to set
├── .gitignore
├── requirements.txt
├── README.md
├── main.py                # entry point — runs the app
│
├── config.py              # loads .env, defines constants
├── api/
│   ├── __init__.py
│   ├── crypto.py          # CoinGecko price fetching (async + one sync helper)
│   └── news.py            # NewsAPI headline fetching (async)
│
├── utils/
│   ├── __init__.py
│   ├── cache.py           # JSON cache with TTL expiry
│   └── formatter.py       # terminal display/formatting helpers
│
└── data/
    └── cache.json          # auto-created at runtime, holds cached responses
```

## Setup

1. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

2. **Configure secrets**

   ```bash
   cp .env.example .env
   ```

   Then edit `.env` and add a free NewsAPI key from
   [newsapi.org/register](https://newsapi.org/register). CoinGecko's public
   endpoint used here needs no key.

   > If `NEWS_API_KEY` is left blank, the dashboard still runs — it just
   > skips the news section and shows a startup warning.

3. **Run it**

   ```bash
   python main.py
   ```

   Force a fresh fetch and skip the cache:

   ```bash
   python main.py --no-cache
   ```

## Configuration reference

All of these go in `.env` (see `.env.example`); every one has a sensible default.

| Variable              | Default                              | Meaning                                   |
|------------------------|---------------------------------------|--------------------------------------------|
| `NEWS_API_KEY`          | *(none)*                              | Your NewsAPI.org API key                    |
| `CRYPTO_IDS`            | `bitcoin,ethereum,solana,dogecoin`    | Comma-separated CoinGecko coin IDs          |
| `VS_CURRENCY`           | `usd`                                 | Currency to price coins against             |
| `NEWS_COUNTRY`          | `us`                                  | NewsAPI country code                        |
| `NEWS_CATEGORY`         | `technology`                          | NewsAPI category                            |
| `NEWS_PAGE_SIZE`        | `5`                                   | Number of headlines to fetch                |
| `CACHE_TTL_SECONDS`     | `300`                                 | How long cached responses stay fresh        |
| `MAX_RETRIES`           | `3`                                   | Retry attempts per request before giving up |`
| `RETRY_BACKOFF_BASE`    | `1.5`                                 | Exponential backoff base, in seconds        |
| `REQUEST_TIMEOUT`       | `10`                                  | Per-request timeout, in seconds             |

## How the pieces fit together

- `config.py` is the only module that reads `os.environ` — everything else
  imports constants from it.
- `api/crypto.py` and `api/news.py` each expose one async `fetch_*`
  function. They check the cache first, fall back to an `aiohttp` request
  with retry/backoff on a miss, and write successful responses back to
  the cache.
- `utils/cache.py` is a small JSON-file key/value store keyed by request
  parameters (e.g. `crypto:bitcoin,ethereum:usd`), each entry stamped with
  a timestamp used to check TTL expiry.
- `main.py` wires it all together: opens one shared `aiohttp.ClientSession`,
  fires both fetches concurrently with `asyncio.gather`, and hands the
  results to `utils/formatter.py` for printing.

## Notes / possible extensions

- Swap the terminal output in `utils/formatter.py` for a `rich`-based UI.
- Add more coins/news categories by editing `.env` — no code changes needed.
- Add a `--clear-cache` flag in `main.py` that calls
  `utils.cache.clear_cache()` before fetching.
