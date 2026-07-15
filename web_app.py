# Flask-Webkanal des Multi-Channel-Chatbots.
# Er stellt eine HTML-Seite und zwei JSON-Endpunkte bereit. Fachliche Wetter-
# und Buchungslogik wird nicht dupliziert, sondern an gemeinsame Services delegiert.

import os

from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request

from booking_service import create_booking_confirmation
from weather_service import get_weather

app = Flask(__name__)


# Rendert für die Startseite das Template templates/index.html.
@app.get("/")
def index():
    return render_template("index.html")


# Empfängt POST-JSON mit "city" und gibt die Antwort von get_weather() als JSON aus.
@app.post("/api/weather")
def weather_api():
    payload = request.get_json(silent=True) or {}
    return jsonify({"message": get_weather(str(payload.get("city", "")))})


# Empfängt POST-JSON mit "date" und "time" und delegiert an den Buchungsservice.
@app.post("/api/appointment")
def appointment_api():
    payload = request.get_json(silent=True) or {}
    message = create_booking_confirmation(
        str(payload.get("date", "")), str(payload.get("time", ""))
    )
    return jsonify({"message": message})


# Wandelt Textwerte aus FLASK_DEBUG zuverlässig in einen booleschen Wert um.
def _is_truthy(value: str) -> bool:
    return value.strip().lower() in {"1", "true", "yes", "on"}


# Lädt die lokale Serverkonfiguration und startet den Flask-Entwicklungsserver.
def main() -> None:
    load_dotenv()
    host = os.getenv("FLASK_HOST", "127.0.0.1")
    port_text = os.getenv("FLASK_PORT", "5000")
    debug = _is_truthy(os.getenv("FLASK_DEBUG", "False"))
    try:
        port = int(port_text)
    except ValueError:
        print(f"Ungültiger FLASK_PORT '{port_text}'. Es wird Port 5000 verwendet.")
        port = 5000
    app.run(host=host, port=port, debug=debug)


if __name__ == "__main__":
    main()
