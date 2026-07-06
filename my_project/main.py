import asyncio, aiohttp
from config import validate_config
from api.crypto  import get_prices
from api.weather import get_weather
from api.news    import get_headlines
from utils.formatter import format_dashboard
 
COINS = ["bitcoin","ethereum","solana","bnb","cardano"]
 
async def fetch_all(session):
    prices, weather, news = await asyncio.gather(
        get_prices(session, COINS),
        get_weather(session, "Lagos"),
        get_headlines(session, category="technology"),
    )
    return prices, weather, news
 
async def main():
    validate_config()
    async with aiohttp.ClientSession() as session:
        prices, weather, news = await fetch_all(session)
    format_dashboard(prices, weather, news)
 
if __name__ == "__main__":
    asyncio.run(main())
