"""
api/news.py — News headline fetching via NewsAPI.org (requires a free API key).
"""
import asyncio

import aiohttp

from config import (
    MAX_RETRIES,
    NEWS_API_BASE_URL,
    NEWS_API_KEY,
    NEWS_CATEGORY,
    NEWS_COUNTRY,
    NEWS_PAGE_SIZE,
    REQUEST_TIMEOUT,
    RETRY_BACKOFF_BASE,
)
from utils.cache import get_cached, set_cached


async def _fetch_with_retry(session: aiohttp.ClientSession, url: str, params: dict):
    """GET with exponential-backoff retry. Returns parsed JSON or None on failure."""
    last_error = None
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            timeout = aiohttp.ClientTimeout(total=REQUEST_TIMEOUT)
            async with session.get(url, params=params, timeout=timeout) as resp:
                if resp.status == 429:
                    wait = RETRY_BACKOFF_BASE ** attempt
                    print(f"[news] Rate limited (429). Retrying in {wait:.1f}s...")
                    await asyncio.sleep(wait)
                    continue
                if resp.status == 401:
                    print("[news] Unauthorized — check your NEWS_API_KEY in .env.")
                    return None
                resp.raise_for_status()
                return await resp.json()
        except (aiohttp.ClientError, asyncio.TimeoutError) as e:
            last_error = e
            wait = RETRY_BACKOFF_BASE ** attempt
            print(f"[news] Attempt {attempt}/{MAX_RETRIES} failed ({e}). Retrying in {wait:.1f}s...")
            await asyncio.sleep(wait)

    print(f"[news] All {MAX_RETRIES} attempts failed. Last error: {last_error}")
    return None


async def fetch_top_headlines(session: aiohttp.ClientSession, use_cache: bool = True) -> list[dict]:
    """
    Fetches top headlines for NEWS_COUNTRY/NEWS_CATEGORY from NewsAPI.
    Returns [] gracefully (never raises) if NEWS_API_KEY is missing or
    every retry fails — so the dashboard can still render the crypto half.
    """
    if not NEWS_API_KEY:
        return []

    cache_key = f"news:{NEWS_COUNTRY}:{NEWS_CATEGORY}"

    if use_cache:
        cached = get_cached(cache_key)
        if cached is not None:
            print("[news] Using cached data.")
            return cached

    params = {
        "country": NEWS_COUNTRY,
        "category": NEWS_CATEGORY,
        "pageSize": NEWS_PAGE_SIZE,
        "apiKey": NEWS_API_KEY,
    }

    data = await _fetch_with_retry(session, NEWS_API_BASE_URL, params)
    if data is None:
        return []

    articles = data.get("articles", [])
    set_cached(cache_key, articles)
    return articles
