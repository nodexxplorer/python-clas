# config.py — load all secrets and constants in one place
import os
from dotenv import load_dotenv
 
load_dotenv()
 
OPENWEATHER_KEY  = os.getenv("OPENWEATHER_API_KEY")
NEWS_API_KEY     = os.getenv("NEWS_API_KEY")
COINGECKO_BASE   = "https://api.coingecko.com/api/v3"
OPENWEATHER_BASE = "https://api.openweathermap.org/data/2.5"
CACHE_FILE       = "data/cache.json"
CACHE_TTL        = 3600   # seconds before cache is stale
 
# Validate that required keys are set
def validate_config():
    missing = []
    if not OPENWEATHER_KEY: missing.append("OPENWEATHER_API_KEY")
    if not NEWS_API_KEY:    missing.append("NEWS_API_KEY")
    if missing:
        raise EnvironmentError(
            f"Missing required environment variables: {missing}\n"
            f"Create a .env file with these keys."
        )
