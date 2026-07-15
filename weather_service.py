# Kanalunabhängiger Service für Wetterinformationen.
# Telegram und Web verwenden dieselbe Funktion, damit die Antworten konsistent sind.
# API-Schlüssel werden ausschließlich aus der Umgebung gelesen und nie hartcodiert.

import os

import requests
from dotenv import load_dotenv

OPENWEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
REQUEST_TIMEOUT_SECONDS = 10


# Erzeugt feste Demo-Daten und macht das Projekt ohne reale Zugangsdaten reproduzierbar.
def _demo_weather(city: str) -> str:
    return (
        f"Demo-Wetter für {city}: 21 °C, leicht bewölkt. "
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
