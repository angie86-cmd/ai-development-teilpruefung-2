"""Flask-Webkanal des Multi-Channel-Chatbots."""

import os

from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request

from booking_service import create_booking_confirmation
from weather_service import get_weather

app = Flask(__name__)


@app.get("/")
def index():
    """Rendert die Bedienoberfläche des Webkanals."""
    return render_template("index.html")


@app.post("/api/weather")
def weather_api():
    """Verarbeitet eine Wetteranfrage und gibt eine JSON-Antwort zurück."""
    payload = request.get_json(silent=True) or {}
    return jsonify({"message": get_weather(str(payload.get("city", "")))})


@app.post("/api/appointment")
def appointment_api():
    """Verarbeitet eine fiktive Terminbuchung als JSON-Anfrage."""
    payload = request.get_json(silent=True) or {}
    message = create_booking_confirmation(
        str(payload.get("date", "")), str(payload.get("time", ""))
    )
    return jsonify({"message": message})


def _is_truthy(value: str) -> bool:
    """Wandelt übliche Textwerte einer Umgebungsvariable in bool um."""
    return value.strip().lower() in {"1", "true", "yes", "on"}


def main() -> None:
    """Startet den lokalen Flask-Entwicklungsserver."""
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
