"""
main.py — Entry point for the Async News & Crypto Dashboard.

Fetches crypto prices and news headlines CONCURRENTLY using asyncio +
aiohttp, applies JSON caching to avoid burning free-tier API quotas, and
prints a formatted terminal dashboard.

Usage:
    python main.py                # normal run (uses cache if fresh)
    python main.py --no-cache     # force a fresh fetch, bypassing cache
"""
import asyncio
import sys
import time

import aiohttp

import config
from api.crypto import fetch_crypto_prices
from api.news import fetch_top_headlines
from utils.formatter import (
    format_crypto_table,
    format_news_list,
    format_timestamp,
    print_header,
    print_section,
)


async def run_dashboard(use_cache: bool = True) -> None:
    start = time.monotonic()

    async with aiohttp.ClientSession() as session:
        # asyncio.gather runs both API calls concurrently instead of
        # waiting for crypto to finish before starting news.
        crypto_task = fetch_crypto_prices(session, use_cache=use_cache)
        news_task = fetch_top_headlines(session, use_cache=use_cache)

        crypto_data, news_data = await asyncio.gather(crypto_task, news_task)

    elapsed = time.monotonic() - start

    print_header("ASYNC NEWS & CRYPTO DASHBOARD")
    print(f"Generated at: {format_timestamp()}   (fetched in {elapsed:.2f}s)")

    print_section("Crypto Prices")
    print(format_crypto_table(crypto_data))

    print_section("Top Headlines")
    print(format_news_list(news_data))
    print()


def main() -> None:
    warnings = config.validate_config()
    for w in warnings:
        print(f"[config] Warning: {w}")

    use_cache = "--no-cache" not in sys.argv

    try:
        asyncio.run(run_dashboard(use_cache=use_cache))
    except KeyboardInterrupt:
        print("\nInterrupted by user. Exiting.")
        sys.exit(0)


if __name__ == "__main__":
    main()
