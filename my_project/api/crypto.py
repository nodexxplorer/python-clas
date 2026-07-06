import aiohttp
from config import COINGECKO_BASE
from utils.cache import get_cached, set_cached
 
CACHE_KEY = "crypto_prices"
async def get_prices(session, coins, currency="usd"):
    """Fetch prices for a list of coins. Uses cache if fresh."""
    cached = get_cached(CACHE_KEY)
    if cached:
        return cached
 
    ids    = ",".join(coins)
    url    = f"{COINGECKO_BASE}/simple/price"
    params = {"ids": ids, "vs_currencies": currency, "include_24hr_change": "true"}
 
    async with session.get(url, params=params, timeout=aiohttp.ClientTimeout(total=10)) as r:
        if r.status == 200:
            data = await r.json()
            set_cached(CACHE_KEY, data)
            return data
        return None
