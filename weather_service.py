# Kanalunabhängiger Service für Wetterinformationen.
# Telegram und Web verwenden dieselbe Funktion, damit die Antworten konsistent sind.
# API-Schlüssel werden ausschließlich aus der Umgebung gelesen und nie hartcodiert.

import json
import os
from pathlib import Path

import requests
from dotenv import load_dotenv

OPENWEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
REQUEST_TIMEOUT_SECONDS = 10
DEMO_DATA_PATH = Path(__file__).resolve().parent / "data" / "demo_weather_data.json"
SAFE_DEMO_WEATHER = {"temperature": 21, "description": "leicht bewölkt"}


# Liest reproduzierbare Demo-Daten aus JSON und nutzt bei Dateifehlern sichere Werte.
def _demo_weather(city: str) -> str:
    weather = SAFE_DEMO_WEATHER
    try:
        with DEMO_DATA_PATH.open(encoding="utf-8") as file:
            demo_data = json.load(file)

        city_key = next(
            (name for name in demo_data if name.casefold() == city.casefold()),
            "default",
        )
        weather = demo_data.get(city_key, demo_data.get("default", weather))
        temperature = weather["temperature"]
        description = weather["description"]
    except (OSError, json.JSONDecodeError, AttributeError, KeyError, TypeError):
        temperature = SAFE_DEMO_WEATHER["temperature"]
        description = SAFE_DEMO_WEATHER["description"]

    return (
        f"Demo-Wetter für {city}: {temperature} °C, {description}. "
        "Hinweis: Es wurde kein OpenWeatherMap API-Key gefunden."
    )


# Nutzt mit OPENWEATHER_API_KEY die Live-API und andernfalls den Demo-Modus.
# API- und Datenfehler werden als verständliche deutsche Rückfallmeldung behandelt.
def get_weather(city: str) -> str:
    normalized_city = (city or "").strip()
    if not normalized_city:
        return "Bitte geben Sie eine Stadt an, zum Beispiel: Berlin."

    load_dotenv()
    api_key = os.getenv("OPENWEATHER_API_KEY", "").strip()
    if not api_key:
        return _demo_weather(normalized_city)

    params = {
        "q": normalized_city,
        "appid": api_key,
        "units": "metric",
        "lang": "de",
    }
    try:
        response = requests.get(
            OPENWEATHER_URL, params=params, timeout=REQUEST_TIMEOUT_SECONDS
        )
        response.raise_for_status()
        data = response.json()
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        resolved_city = data.get("name") or normalized_city
        return f"Wetter für {resolved_city}: {temperature:.1f} °C, {description}."
    except (requests.RequestException, KeyError, IndexError, TypeError, ValueError):
        return (
            f"Die Wetterdaten für {normalized_city} konnten derzeit nicht "
            "abgerufen werden. Bitte versuchen Sie es später erneut."
        )
