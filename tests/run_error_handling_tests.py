import os
import sys
from pathlib import Path
from unittest.mock import patch

# Projektmodule aus dem übergeordneten Repository laden, ohne Cache-Dateien anzulegen.
sys.dont_write_bytecode = True
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

import weather_service
from booking_service import create_booking_confirmation
from weather_service import get_weather

REPORT_PATH = PROJECT_ROOT / "reports" / "error_handling_test_report.txt"
FAKE_API_KEY = "fake-key-for-test"


class FakeResponse:
    # Bildet nur die für diese Tests benötigten Teile einer HTTP-Antwort nach.
    def __init__(self, status_code, payload=None):
        self.status_code = status_code
        self.payload = payload

    def raise_for_status(self):
        return None

    def json(self):
        return self.payload


def run_test(name, test_callable, expected_substring):
    try:
        result = test_callable()
        if expected_substring in result:
            return True, f"PASS: {name}"
        return False, (
            f"FAIL: {name} – Erwarteter Text nicht gefunden: "
            f"{expected_substring}"
        )
    except Exception as error:
        return False, f"FAIL: {name} – {type(error).__name__}: {error}"


def mocked_weather(city, response=None, side_effect=None):
    # Der Platzhalterschlüssel gilt nur innerhalb dieses Kontexts und wird danach entfernt.
    with (
        patch.dict(
            os.environ,
            {"OPENWEATHER_API_KEY": FAKE_API_KEY},
            clear=False,
        ),
        patch("weather_service.load_dotenv"),
        patch(
            "weather_service.requests.get",
            return_value=response,
            side_effect=side_effect,
        ),
    ):
        return get_weather(city)


def main():
    tests = [
        (
            "Leere Stadteingabe",
            lambda: get_weather(""),
            "Bitte geben Sie eine Stadt an",
        ),
        (
            "Ungültige Stadt / HTTP 404",
            lambda: mocked_weather("xyzstadt123", FakeResponse(404)),
            "wurde nicht gefunden",
        ),
        (
            "Ungültiger API-Key / HTTP 401",
            lambda: mocked_weather("Berlin", FakeResponse(401)),
            "nicht authentifiziert",
        ),
        (
            "Anfragelimit / HTTP 429",
            lambda: mocked_weather("Berlin", FakeResponse(429)),
            "Limit des Wetterdienstes",
        ),
        (
            "Netzwerk-Timeout",
            lambda: mocked_weather(
                "Berlin",
                side_effect=weather_service.requests.Timeout("timeout"),
            ),
            "konnten derzeit nicht abgerufen werden",
        ),
        (
            "Unerwartete JSON-Struktur",
            lambda: mocked_weather(
                "Berlin",
                FakeResponse(200, {"unexpected": "structure"}),
            ),
            "konnten derzeit nicht abgerufen werden",
        ),
        (
            "Gültige fiktive Terminbuchung",
            lambda: create_booking_confirmation("20.07.2026", "14:00"),
            "fiktiv",
        ),
        (
            "Ungültiges Datumsformat",
            lambda: create_booking_confirmation("2026-07-20", "14:00"),
            "DD.MM.YYYY",
        ),
        (
            "Ungültiges Uhrzeitformat",
            lambda: create_booking_confirmation("20.07.2026", "25:00"),
            "HH:MM",
        ),
    ]

    results = [run_test(*test) for test in tests]
    passed = sum(success for success, _ in results)
    failed = len(results) - passed
    lines = [
        "Automatisierte Fehlerbehandlungstests",
        *[message for _, message in results],
        "",
        f"Bestanden: {passed}",
        f"Fehlgeschlagen: {failed}",
        f"Status: {'OK' if failed == 0 else 'FEHLER'}",
    ]
    report = "\n".join(lines) + "\n"

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(report, encoding="utf-8")
    print(report, end="")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
