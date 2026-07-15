# Kanalunabhängiger Service für fiktive Terminbuchungen.
# Es wird kein realer Termin erzeugt oder gespeichert; damit wird die Prüfungsaufgabe
# ohne Verarbeitung echter Termindaten reproduzierbar umgesetzt.

import json
import re
from pathlib import Path

CONFIG_PATH = Path(__file__).resolve().parent / "data" / "appointment_config.json"
SAFE_CONFIG = {
    "confirmation_prefix": "Ihr Termin wurde fiktiv",
    "confirmation_suffix": "bestätigt.",
    "date_format_hint": "DD.MM.YYYY",
    "time_format_hint": "HH:MM",
    "example_date": "20.07.2026",
    "example_time": "14:00",
}

# Prüft das verlangte Datumsformat DD.MM.YYYY.
DATE_PATTERN = re.compile(r"^\d{2}\.\d{2}\.\d{4}$")

# Prüft HH:MM und begrenzt Stunden und Minuten auf gültige Bereiche.
TIME_PATTERN = re.compile(r"^(?:[01]\d|2[0-3]):[0-5]\d$")


# Validiert beide Eingaben und gibt Fehler oder eine ausdrücklich fiktive Bestätigung zurück.
def create_booking_confirmation(date: str, time: str) -> str:
    config = SAFE_CONFIG
    try:
        with CONFIG_PATH.open(encoding="utf-8") as file:
            config = {**SAFE_CONFIG, **json.load(file)}
    except (OSError, json.JSONDecodeError, TypeError):
        # Die sichere Standardkonfiguration hält den Prototyp ohne JSON-Datei lauffähig.
        config = SAFE_CONFIG

    normalized_date = (date or "").strip()
    normalized_time = (time or "").strip()
    if not normalized_date or not normalized_time:
        return (
            "Bitte geben Sie Datum und Uhrzeit an, zum Beispiel: "
            f"{config['example_date']} {config['example_time']}."
        )
    if not DATE_PATTERN.fullmatch(normalized_date):
        return (
            "Bitte verwenden Sie für das Datum das Format "
            f"{config['date_format_hint']}."
        )
    if not TIME_PATTERN.fullmatch(normalized_time):
        return (
            "Bitte verwenden Sie für die Uhrzeit das Format "
            f"{config['time_format_hint']} (00:00–23:59)."
        )
    return (
        f"{config['confirmation_prefix']} für den {normalized_date} um "
        f"{normalized_time} Uhr {config['confirmation_suffix']}"
    )
