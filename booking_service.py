# Kanalunabhängiger Service für fiktive Terminbuchungen.
# Es wird kein realer Termin erzeugt oder gespeichert; damit wird die Prüfungsaufgabe
# ohne Verarbeitung echter Termindaten reproduzierbar umgesetzt.

import re

# Prüft das verlangte Datumsformat DD.MM.YYYY.
DATE_PATTERN = re.compile(r"^\d{2}\.\d{2}\.\d{4}$")

# Prüft HH:MM und begrenzt Stunden und Minuten auf gültige Bereiche.
TIME_PATTERN = re.compile(r"^(?:[01]\d|2[0-3]):[0-5]\d$")


# Validiert beide Eingaben und gibt Fehler oder eine ausdrücklich fiktive Bestätigung zurück.
def create_booking_confirmation(date: str, time: str) -> str:
    normalized_date = (date or "").strip()
    normalized_time = (time or "").strip()
    if not normalized_date or not normalized_time:
        return (
            "Bitte geben Sie Datum und Uhrzeit an, zum Beispiel: "
            "20.07.2026 14:00."
        )
    if not DATE_PATTERN.fullmatch(normalized_date):
        return "Bitte verwenden Sie für das Datum das Format DD.MM.YYYY."
    if not TIME_PATTERN.fullmatch(normalized_time):
        return "Bitte verwenden Sie für die Uhrzeit das Format HH:MM (00:00–23:59)."
    return (
        f"Ihr Termin wurde fiktiv für den {normalized_date} um "
        f"{normalized_time} Uhr bestätigt."
    )
