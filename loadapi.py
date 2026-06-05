import os
import requests
from dotenv import load_dotenv


load_dotenv()  # Load environment variables from .env file
weather_api_key = os.getenv("OPENWEATHER_KEY")

print(f"Your OpenWeather API Key is: {weather_api_key}")





API_KEY = os.getenv("OPENWEATHER_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params, timeout=10)
    response.raise_for_status()
    d = response.json()
    return {
            "city":    d["name"],
            "country": d["sys"]["country"],
            "temp":    d["main"]["temp"],
            "feels":   d["main"]["feels_like"],
            "humid":   d["main"]["humidity"],
            "desc":    d["weather"][0]["description"].title(),
            "wind":    d["wind"]["speed"],
    }

 
def show_weather(w):
    if not w: return
    print(f"""
  City      : {w["city"]}, {w["country"]}
  Temp      : {w["temp"]}°C  (feels like {w["feels"]}°C)
  Humidity  : {w["humid"]}%
  Condition : {w["desc"]}
  Wind      : {w["wind"]} m/s
    """)
 
while True:
    city = input("Enter city (q to quit): ").strip()
    if city.lower() == "q": break
    show_weather(get_weather(city))

