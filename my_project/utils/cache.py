import json, os, time
from config import CACHE_FILE, CACHE_TTL
 
def _load_cache():
    if not os.path.exists(CACHE_FILE): return {}
    with open(CACHE_FILE) as f:
        return json.load(f)
 
def _save_cache(data):
    os.makedirs(os.path.dirname(CACHE_FILE), exist_ok=True)
    with open(CACHE_FILE, "w") as f:
        json.dump(data, f, indent=2)
 
def get_cached(key):
    """Return cached value if fresh, else None."""
    cache = _load_cache()
    if key not in cache: return None
    entry = cache[key]
    age   = time.time() - entry["timestamp"]
    if age > CACHE_TTL: return None
    return entry["data"]
 
def set_cached(key, data):
    """Store data in cache with current timestamp."""
    cache = _load_cache()
    cache[key] = {"timestamp": time.time(), "data": data}
    _save_cache(cache)
