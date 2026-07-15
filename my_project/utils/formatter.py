"""
utils/formatter.py — Terminal display/formatting helpers for the dashboard.
"""
from datetime import datetime, timezone

RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[32m"
RED = "\033[31m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
DIM = "\033[2m"


def format_price_change(change_pct) -> str:
    """Color-codes a percentage change: green if positive, red if negative."""
    if change_pct is None:
        return "N/A"
    color = GREEN if change_pct >= 0 else RED
    sign = "+" if change_pct >= 0 else ""
    return f"{color}{sign}{change_pct:.2f}%{RESET}"


def format_crypto_table(crypto_data: list) -> str:
    """Builds a readable table of crypto prices from CoinGecko-style records."""
    if not crypto_data:
        return f"{DIM}No crypto data available.{RESET}"

    lines = [f"{BOLD}{'Coin':<12}{'Price (USD)':<16}{'24h Change':<12}{RESET}"]
    lines.append("-" * 40)
    for coin in crypto_data:
        name = str(coin.get("name", "?")).capitalize()
        price = coin.get("current_price")
        change = coin.get("price_change_percentage_24h")
        price_str = f"${price:,.2f}" if isinstance(price, (int, float)) else "N/A"
        lines.append(f"{name:<12}{price_str:<16}{format_price_change(change)}")
    return "\n".join(lines)


def format_news_list(articles: list) -> str:
    """Builds a readable numbered list of news headlines."""
    if not articles:
        return f"{DIM}No news articles available.{RESET}"

    lines = []
    for i, article in enumerate(articles, start=1):
        title = article.get("title", "Untitled")
        source = article.get("source", {}).get("name", "Unknown source")
        lines.append(f"{CYAN}{i}. {title}{RESET} {DIM}({source}){RESET}")
    return "\n".join(lines)


def format_timestamp(ts: float = None) -> str:
    dt = datetime.now(timezone.utc) if ts is None else datetime.fromtimestamp(ts, tz=timezone.utc)
    return dt.strftime("%Y-%m-%d %H:%M:%S UTC")


def print_header(title: str) -> None:
    print(f"\n{BOLD}{YELLOW}{'=' * 60}\n{title.center(60)}\n{'=' * 60}{RESET}\n")


def print_section(title: str) -> None:
    print(f"\n{BOLD}{title}{RESET}")
    print("-" * len(title))
