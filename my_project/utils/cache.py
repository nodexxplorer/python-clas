"""
utils/cache.py — Simple JSON file cache with TTL (time-to-live) expiry.

Why a file cache instead of just in-memory? Free-tier crypto/news APIs have
tight rate limits. Caching to disk means re-running the dashboard seconds
apart (or after a crash) doesn't burn another request, and the cache
survives between process runs.

Cache file structure (data/cache.json):
{
    "crypto:bitcoin,ethereum:usd": {
        "timestamp": 1720400000.0,
        "data": [...]
    },
    "news:us:technology": {
        "timestamp": 1720400012.0,
        "data": [...]
    }
}
"""
import json
import os
import time
from threading import Lock

from config import CACHE_FILE_PATH, CACHE_TTL_SECONDS

_lock = Lock()  # guards read-modify-write of the cache file across calls


def _ensure_cache_dir() -> None:
    directory = os.path.dirname(CACHE_FILE_PATH)
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)


def _read_cache_file() -> dict:
    _ensure_cache_dir()
    if not os.path.exists(CACHE_FILE_PATH):
        return {}
    try:
        with open(CACHE_FILE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        # Corrupted or unreadable cache file — fail safe, treat as empty.
        return {}


def _write_cache_file(cache_data: dict) -> None:
    _ensure_cache_dir()
    tmp_path = CACHE_FILE_PATH + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        json.dump(cache_data, f, indent=2)
    os.replace(tmp_path, CACHE_FILE_PATH)  # atomic replace on POSIX systems


def get_cached(key: str, ttl_seconds: int = CACHE_TTL_SECONDS):
    """Return cached data for `key` if present and not expired, else None."""
    with _lock:
        cache_data = _read_cache_file()

    entry = cache_data.get(key)
    if entry is None:
        return None

    age = time.time() - entry.get("timestamp", 0)
    if age > ttl_seconds:
        return None  # expired — caller should re-fetch

    return entry.get("data")


def set_cached(key: str, data) -> None:
    """Store `data` under `key`, stamped with the current time."""
    with _lock:
        cache_data = _read_cache_file()
        cache_data[key] = {
            "timestamp": time.time(),
            "data": data,
        }
        _write_cache_file(cache_data)


def clear_cache() -> None:
    """Wipe the entire cache file. Useful for a `--clear-cache` CLI flag."""
    with _lock:
        _write_cache_file({})
