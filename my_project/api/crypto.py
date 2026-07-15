"""
api/crypto.py — Crypto price fetching via the CoinGecko API (no key required).

Contains:
- get_supported_coins_sync(): a plain synchronous call using `requests`.
  Handy for a one-off startup check or a CLI "list available coins" command
  — not everything needs to be async, and `requests` is still the right
  tool for simple, single, blocking calls.
- fetch_crypto_prices(): the main async fetcher using aiohttp, wrapped
  with retry/backoff logic and disk caching.
"""
import asyncio

import aiohttp
import requests

from config import (
    COINGECKO_BASE_URL,
    CRYPTO_IDS,
    MAX_RETRIES,
    REQUEST_TIMEOUT,
    RETRY_BACKOFF_BASE,
    VS_CURRENCY,
)
from utils.cache import get_cached, set_cached


def get_supported_coins_sync() -> list[str]:
    """
    Synchronous helper (uses `requests`) that fetches the full list of coin
    IDs CoinGecko supports. Useful for validating CRYPTO_IDS before a run.
    """
    url = f"{COINGECKO_BASE_URL}/coins/list"
    try:
        response = requests.get(url, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        coins = response.json()
        return [coin["id"] for coin in coins]
    except requests.RequestException as e:
        print(f"[crypto] Warning: could not fetch supported coin list ({e})")
        return []


async def _fetch_with_retry(session: aiohttp.ClientSession, url: str, params: dict):
    """GET with exponential-backoff retry. Returns parsed JSON or None on failure."""
    last_error = None
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            timeout = aiohttp.ClientTimeout(total=REQUEST_TIMEOUT)
            async with session.get(url, params=params, timeout=timeout) as resp:
                if resp.status == 429:
                    wait = RETRY_BACKOFF_BASE ** attempt
                    print(f"[crypto] Rate limited (429). Retrying in {wait:.1f}s...")
                    await asyncio.sleep(wait)
                    continue
                resp.raise_for_status()
                return await resp.json()
        except (aiohttp.ClientError, asyncio.TimeoutError) as e:
            last_error = e
            wait = RETRY_BACKOFF_BASE ** attempt
            print(f"[crypto] Attempt {attempt}/{MAX_RETRIES} failed ({e}). Retrying in {wait:.1f}s...")
            await asyncio.sleep(wait)

    print(f"[crypto] All {MAX_RETRIES} attempts failed. Last error: {last_error}")
    return None


async def fetch_crypto_prices(session: aiohttp.ClientSession, use_cache: bool = True) -> list[dict]:
    """
    Fetches current price + 24h change for CRYPTO_IDS from CoinGecko.

    Returns a list like:
        [{"id": "bitcoin", "name": "bitcoin", "current_price": 65000.0,
          "price_change_percentage_24h": 2.15}, ...]
    Returns [] (never raises) if all retries fail, so the dashboard can
    still render the news half.
    """
    cache_key = f"crypto:{','.join(CRYPTO_IDS)}:{VS_CURRENCY}"

    if use_cache:
        cached = get_cached(cache_key)
        if cached is not None:
            print("[crypto] Using cached data.")
            return cached

    url = f"{COINGECKO_BASE_URL}/coins/markets"
    params = {
        "vs_currency": VS_CURRENCY,
        "ids": ",".join(CRYPTO_IDS),
        "order": "market_cap_desc",
        "price_change_percentage": "24h",
    }

    data = await _fetch_with_retry(session, url, params)
    if data is None:
        return []

    results = [
        {
            "id": coin.get("id"),
            "name": coin.get("id"),
            "current_price": coin.get("current_price"),
            "price_change_percentage_24h": coin.get("price_change_percentage_24h"),
        }
        for coin in data
    ]

    set_cached(cache_key, results)
    return results
