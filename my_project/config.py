"""
config.py — Loads environment variables and defines app-wide constants.

Every other module pulls its settings from here instead of reading
os.environ directly, so there's exactly one place to look when tuning
behavior (timeouts, cache TTL, which coins to track, etc.).
"""
import os
from dotenv import load_dotenv

load_dotenv()  # reads .env (if present) into environment variables

# --- API Keys ---
NEWS_API_KEY = os.getenv("NEWS_API_KEY", "")

# --- API Base URLs ---
COINGECKO_BASE_URL = "https://api.coingecko.com/api/v3"
NEWS_API_BASE_URL = "https://newsapi.org/v2/top-headlines"

# --- App Settings ---
CRYPTO_IDS = os.getenv("CRYPTO_IDS", "bitcoin,ethereum,solana,dogecoin").split(",")
VS_CURRENCY = os.getenv("VS_CURRENCY", "usd")
NEWS_COUNTRY = os.getenv("NEWS_COUNTRY", "us")
NEWS_CATEGORY = os.getenv("NEWS_CATEGORY", "technology")
NEWS_PAGE_SIZE = int(os.getenv("NEWS_PAGE_SIZE", "5"))

# --- Cache Settings ---
CACHE_FILE_PATH = os.path.join("data", "cache.json")
CACHE_TTL_SECONDS = int(os.getenv("CACHE_TTL_SECONDS", "300"))  # 5 minutes default

# --- Retry / Networking Settings ---
MAX_RETRIES = int(os.getenv("MAX_RETRIES", "3"))
RETRY_BACKOFF_BASE = float(os.getenv("RETRY_BACKOFF_BASE", "1.5"))  # exponential backoff base (seconds)
REQUEST_TIMEOUT = float(os.getenv("REQUEST_TIMEOUT", "10"))  # seconds


def validate_config() -> list[str]:
    """
    Basic startup validation. Returns a list of warning strings instead of
    raising — the dashboard should still run (e.g. crypto-only) if the
    optional NEWS_API_KEY is missing.
    """
    warnings = []
    if not NEWS_API_KEY:
        warnings.append(
            "NEWS_API_KEY is not set — news headlines will be skipped. "
            "Get a free key at https://newsapi.org and add it to your .env file."
        )
    return warnings
