# Multi-Channel Chatbot - Teilprüfung 2

## Teilprüfung 2

### Aufgabe

Teilprüfung 2

Entwickle einen Multi-Channel Chatbot, der sowohl über Telegram als auch über eine einfache Webanwendung erreichbar ist. Dein Chatbot soll in der Lage sein, Benutzeranfragen zu beantworten, die sich auf Wetterinformationen und Terminbuchungen konzentrieren. Nutze die Telegram Bot API für den Telegram-Teil und Flask für die Webanwendung.

Führe folgende Schritte durch:

Erstelle ein Python-Skript für den Telegram Bot, der die Telegram Bot API verwendet. Der Bot soll auf einfache Befehle wie “/wetter [Stadt]” reagieren, indem er aktuelle Wetterinformationen aus einer öffentlichen API (z.B. OpenWeatherMap API) abruft. Für “/termin [Datum] [Zeit]” soll der Bot eine fiktive Buchungsbestätigung senden.

Entwickle eine einfache Webanwendung mit Flask, die ein ähnliches Verhalten wie der Telegram Bot zeigt. Die Webanwendung soll ein Formular für Wetteranfragen und Terminbuchungen enthalten. Nutze AJAX, um die Anfragen asynchron zu bearbeiten und die Antworten ohne Neuladen der Seite anzuzeigen.

---

# Lösung

## Einleitung

Für die Teilprüfung wurde ein Multi-Channel-Chatbot mit zwei Zugangskanälen umgesetzt: Telegram und eine browserbasierte Webanwendung. Beide Kanäle decken die Anwendungsfälle Wetterabfrage und fiktive Terminbuchung ab. Sie greifen auf dieselbe gemeinsame Geschäftslogik zurück, sodass Regeln und Antworten nicht doppelt implementiert werden.

Das Projekt wird mit Git versioniert und kann über GitHub unter [https://github.com/angie86-cmd/ai-development-teilpruefung-2](https://github.com/angie86-cmd/ai-development-teilpruefung-2) bereitgestellt werden. Die finale ZIP-Datei liegt im Verzeichnis `submission/`. Weder die Projektdateien noch die Abgabe enthalten echte Tokens, API-Schlüssel oder andere Secrets. Benötigte Umgebungsvariablen werden ausschließlich durch Platzhalter in `.env.example` dokumentiert.

Der Telegram-Bot wurde über BotFather mit folgender öffentlich sichtbarer Konfiguration eingerichtet:

| Einstellung | Konfiguration |
|---|---|
| Bot-Benutzername | `@angie_weather_booking_bot` |
| Bot-Name | `AngieWeatherAppointmentBot` |
| About | Multi-Channel Chatbot für Wetterinformationen und fiktive Terminbuchungen. |
| Description | Dieser Bot ist ein Prototyp für die AI-Development Teilprüfung 2. Er beantwortet einfache Wetteranfragen und erstellt fiktive Terminbuchungsbestätigungen. |
| Befehle | `/start`, `/hilfe`, `/wetter Berlin`, `/termin 20.07.2026 14:00` |
| Privacy Policy | [Telegram Standard Privacy Policy](https://telegram.org/privacy-tpa) |

Die hinterlegten Befehlsbeschreibungen lauten `/start - Bot starten`, `/hilfe - Hilfe anzeigen`, `/wetter Berlin - Wetterinformationen abrufen` und `/termin 20.07.2026 14:00 - Fiktiven Termin buchen`. Für den akademischen Prototyp wird die Telegram Standard Privacy Policy verwendet. Die Anwendung speichert keine personenbezogenen Daten dauerhaft, erstellt keine echten Termine und fordert keine sensiblen Daten an.

![Telegram Bot Konfiguration](Bilder/Screenshot%2001_BotConfiguration.png)

*Der Screenshot zeigt die BotFather-Konfiguration des Telegram-Bots.*

![Telegram Bot Profilbild](Bilder/ProfilePic.png)

*`ProfilePic.png` ist das Profilbild des Bots.*

![Telegram Bot Description Picture](Bilder/DescriptionPic.png)

*`DescriptionPic.png` wird im Bereich „What can this bot do?“ angezeigt.*

## Projektstruktur und Versionierung

```text
ai-development-teilpruefung-2/
├── README.md
├── telegram_bot.py
├── web_app.py
├── weather_service.py
├── booking_service.py
├── templates/
│   └── index.html
├── static/
│   ├── app.js
│   └── style.css
├── Bilder/
│   ├── DescriptionPic.png
│   ├── ProfilePic.png
│   └── Screenshot 01_BotConfiguration.png
├── requirements.txt
├── .env.example
├── beispiel_dialog.txt
├── hinweis_zur_abgabe.txt
├── .gitignore
└── submission/
    └── Angie_Angarita_Soto_Teilprüfung 2.zip
```

**Tabelle 1: Dateien und Zweck im Projekt**

| Datei | Zweck |
|---|---|
| `README.md` | Hauptdokumentation mit Aufgabenstellung, Architektur, Umsetzung, Ausführung und Reflexion |
| `telegram_bot.py` | Telegram-Adapter mit asynchronen Command-Handlern und Polling |
| `web_app.py` | Flask-Anwendung, HTML-Route und JSON-API-Endpunkte |
| `weather_service.py` | Gemeinsame Wetterlogik mit OpenWeatherMap-Anbindung und Demo-Modus |
| `booking_service.py` | Gemeinsame Validierung und fiktive Terminbestätigung |
| `templates/index.html` | Deutsche Benutzeroberfläche mit Wetter- und Terminformular |
| `static/app.js` | Asynchrone Formularverarbeitung mit der Fetch API |
| `static/style.css` | Einfaches responsives Erscheinungsbild ohne externes Framework |
| `Bilder/` | Bildnachweise zur Konfiguration und visuellen Darstellung des Telegram-Bots |
| `Bilder/DescriptionPic.png` | Bild für den Telegram-Bereich „What can this bot do?“ |
| `Bilder/ProfilePic.png` | Profilbild des konfigurierten Telegram-Bots |
| `Bilder/Screenshot 01_BotConfiguration.png` | Screenshot der BotFather-Konfiguration |
| `requirements.txt` | Direkte Python-Abhängigkeiten des Projekts |
| `.env.example` | Vorlage der benötigten und optionalen Umgebungsvariablen ohne Secrets |
| `beispiel_dialog.txt` | Beispielabläufe für Telegram und Web |
| `hinweis_zur_abgabe.txt` | Inhalt, Speicherort und Sicherheitsangaben zur ZIP-Abgabe |
| `.gitignore` | Ausschluss lokaler Umgebung, Caches, Secrets und ZIP-Prüfverzeichnis |
| `submission/Angie_Angarita_Soto_Teilprüfung 2.zip` | Finale Datei zur Einreichung |

## Gitignore und lokale Entwicklungsdateien

Die Regeln in `.gitignore` trennen lokale oder automatisch erzeugte Dateien von den fachlich relevanten Projektbestandteilen:

- `.venv/` wird ausgeschlossen, weil virtuelle Umgebungen lokale Entwicklungsumgebungen sind und nicht versioniert werden sollen.
- `__pycache__/` und `*.pyc` werden ausgeschlossen, da Python diese Cache-Dateien automatisch erzeugt.
- `.env` und `.env.*` werden ausgeschlossen, weil sie reale Telegram-Bot-Tokens, OpenWeatherMap API-Keys oder lokale Konfiguration enthalten können. `.env.example` ist ausdrücklich ausgenommen, da diese Datei die erforderlichen Umgebungsvariablen ohne echte Secrets dokumentiert.
- `submission/check_zip/` wird ausgeschlossen, weil dieses temporäre Verzeichnis nur zur Prüfung des ZIP-Archivs vor der Abgabe dient.
- `.pytest_cache/`, `.DS_Store` und `Thumbs.db` werden ausgeschlossen, da sie lokal durch Testwerkzeuge oder Betriebssysteme entstehen.
- `Bilder/` wird bewusst nicht ausgeschlossen: Die Bilder dokumentieren die Telegram-BotFather-Konfiguration und gehören zur Projektdokumentation auf GitHub.
- Das finale ZIP-Archiv in `submission/` wird nicht allgemein ausgeschlossen, damit es entsprechend dem Arbeitsablauf der vorherigen Teilprüfung versioniert werden kann.

Git protokolliert die Entwicklung nachvollziehbar; GitHub dient als Remote-Repository. Lokale Laufzeitdateien wie `.venv`, `.env`, Python-Caches und `submission/check_zip/` werden ignoriert. Die ZIP-Abgabe enthält nur die freigegebenen Dateitypen und keine Versionsverwaltungsdaten.

# a) Telegram Bot mit Telegram Bot API

## a.1 Ziel des Telegram-Bots

Der Telegram-Kanal in `telegram_bot.py` ermöglicht Wetterabfragen und fiktive Terminbuchungen direkt im Messenger. Begrüßung und Hilfe erläutern die Verwendung. Die fachlichen Antworten stammen aus den gemeinsamen Services.

## a.2 Architektur des Telegram-Kanals

```text
Telegram User
    ↓
Telegram Bot API
    ↓
telegram_bot.py
    ↓
weather_service.py / booking_service.py
    ↓
Bot Response
```

## a.3 Unterstützte Befehle

Der Bot nutzt `python-telegram-bot` im Stil der Version 20 oder neuer mit `ApplicationBuilder`, `CommandHandler`, `ContextTypes` und asynchronen Handlerfunktionen.

**Tabelle 2: Telegram-Befehle**

| Command | Zweck | Beispiel |
|---|---|---|
| `/start` | Begrüßt und nennt die zentralen Möglichkeiten | `/start` |
| `/hilfe` | Zeigt Befehle und Eingabeformate | `/hilfe` |
| `/wetter [Stadt]` | Fragt Wetter- oder Demo-Wetterdaten ab | `/wetter Berlin` |
| `/termin [Datum] [Zeit]` | Erstellt eine fiktive Terminbestätigung | `/termin 20.07.2026 14:00` |

## a.4 BotFather-Konfiguration

Der Bot wurde in BotFather unter dem Namen `AngieWeatherAppointmentBot` und dem Benutzernamen `@angie_weather_booking_bot` konfiguriert. About-Text, ausführliche Beschreibung, Befehlsübersicht, Profilbild, Description Picture und die Telegram Standard Privacy Policy wurden dort hinterlegt. Die drei Dateien im Ordner `Bilder/` dokumentieren diese Konfiguration, ohne ein Token oder andere Secrets offenzulegen.

## a.5 Verwendung gemeinsamer Geschäftslogik

`weather_command()` verbindet alle Befehlsargumente zu einem Stadtnamen und ruft `get_weather()` auf. `appointment_command()` übergibt Datum und Uhrzeit an `create_booking_confirmation()`. Fachliche Logik wird nicht im Telegram-Adapter dupliziert.

## a.6 Authentifizierung über Umgebungsvariable

Beim Start lädt `python-dotenv` optionale lokale Einstellungen. Das Telegram-Token wird ausschließlich mit `os.getenv("TELEGRAM_BOT_TOKEN")` gelesen und nicht hartcodiert. `.env.example` enthält nur einen Platzhalter; `.env` ist durch `.gitignore` ausgeschlossen.

## a.7 Umgang mit fehlendem Telegram Token

Ist `TELEGRAM_BOT_TOKEN` leer oder nicht vorhanden, gibt `main()` eine klare deutsche Meldung aus und kehrt kontrolliert zurück. Dadurch entsteht kein unverständlicher Verbindungsfehler und das Projekt bleibt ohne echte Zugangsdaten testbar.

## a.8 Python-Code und zentrale Funktionen

Die vier Handler sind als `async def` definiert: `start_command`, `help_command`, `weather_command` und `appointment_command`. Antworten werden mit `await update.message.reply_text(...)` versendet. Beispiel für die Delegation:

```python
async def weather_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    city = " ".join(context.args).strip()
    response = get_weather(city)
    if update.message:
        await update.message.reply_text(response)
```

`main()` lädt die Konfiguration, prüft das Token, baut die `Application`, registriert alle Handler und startet anschließend das Polling. Die Handler bleiben klein und delegieren fachliche Aufgaben an die Services.

## a.9 Begründung der Polling-Variante

Für den lokalen Prototyp nutzt `python-telegram-bot` bewusst Polling. Der Bot fragt neue Nachrichten fortlaufend bei Telegram ab. Dies vermeidet die Einrichtung einer öffentlich erreichbaren HTTPS-Adresse und eines Webhooks. Für eine produktive, skalierte Bereitstellung könnte später ein Webhook eingesetzt werden.

## a.10 Datenschutz und Bot Privacy Policy

In BotFather ist die [Telegram Standard Privacy Policy](https://telegram.org/privacy-tpa) konfiguriert. Sie ist für diesen akademischen Prototyp angemessen, weil die Anwendung keine personenbezogenen Daten dauerhaft speichert, keine realen Termine erzeugt und keine sensiblen Daten anfordert. Echte Tokens und API-Schlüssel werden ausschließlich lokal über Umgebungsvariablen bereitgestellt und durch `.gitignore` von Git ausgeschlossen.

# b) Flask Webanwendung mit AJAX

## b.1 Ziel der Webanwendung

Die Flask-Webanwendung bietet dieselben zwei Anwendungsfälle wie Telegram über eine leicht bedienbare Browseroberfläche. Dadurch lässt sich der Chatbot auch ohne Telegram-Konto demonstrieren.

## b.2 Architektur der Webanwendung

```text
Browser
    ↓
index.html + app.js
    ↓
AJAX fetch
    ↓
Flask API endpoint
    ↓
weather_service.py / booking_service.py
    ↓
JSON Response
    ↓
Result shown on page
```

## b.3 Flask-Routen

`web_app.py` implementiert eine HTML-Route und zwei JSON-Endpunkte.

**Tabelle 3: Flask-Routen**

| Route | Methode | Zweck |
|---|---|---|
| `/` | GET | Rendert `templates/index.html` |
| `/api/weather` | POST | Liest `city` aus JSON und gibt die Wetterantwort als JSON zurück |
| `/api/appointment` | POST | Liest `date` und `time` aus JSON und gibt die Terminantwort als JSON zurück |

## b.4 AJAX-Verarbeitung

`static/app.js` registriert nach `DOMContentLoaded` Ereignisbehandlungen für beide Formulare. Die Hilfsfunktion `postJson()` sendet die Eingaben mit `fetch`, der Methode POST und dem Content-Type `application/json` an Flask. Netzwerk- und HTTP-Fehler werden abgefangen und verständlich angezeigt.

## b.5 Wetterformular

Das Wetterformular in `templates/index.html` nimmt eine Stadt entgegen. Nach dem Absenden wird `{ "city": "Berlin" }` an `/api/weather` übertragen. Der Endpunkt ruft `get_weather()` auf und sendet dessen Ergebnis zurück.

## b.6 Terminformular

Das Terminformular erfasst Datum und Uhrzeit. Die Werte werden als JSON an `/api/appointment` gesendet und durch `create_booking_confirmation()` geprüft. Der Hinweis im Formular macht die erwarteten Formate transparent.

## b.7 Gemeinsame Nutzung der Services

Auch `web_app.py` enthält keine eigene Wetter- oder Buchungslogik. Die Anwendung importiert dieselben Servicefunktionen wie der Telegram-Bot und bleibt dadurch ein schlanker Kanaladapter.

## b.8 Antwort ohne Neuladen der Seite

`event.preventDefault()` verhindert das reguläre Neuladen beim Absenden. Nach Abschluss des `fetch`-Aufrufs setzt JavaScript den Text im jeweiligen Ergebnisbereich. `aria-live="polite"` sorgt zusätzlich dafür, dass unterstützende Technologien aktualisierte Antworten ankündigen können.

# Gemeinsame Geschäftslogik

## Gemeinsame Services

`weather_service.py` und `booking_service.py` sind kanalunabhängig. Sie nehmen einfache Zeichenketten entgegen und geben eine Zeichenkette zurück. Damit benötigen sie weder Telegram- noch Flask-Objekte.

## Trennung von Kanal und Geschäftslogik

```text
Telegram Channel ──┐
                   ├── Shared Business Logic
Web Channel ───────┘
                        ├── weather_service.py
                        └── booking_service.py
```

Telegram übersetzt Befehlsargumente, Web übersetzt JSON-Felder. Anschließend rufen beide Adapter die gleichen Funktionen auf. Diese Trennung verhindert doppelten Code und hält Änderungen an fachlichen Regeln an einer zentralen Stelle.

## Vorteile der Architektur

Die Services können isoliert getestet, wiederverwendet und unabhängig von den Benutzeroberflächen weiterentwickelt werden. Weitere Kanäle wie WhatsApp Business, Microsoft Teams oder Slack könnten später als zusätzliche Adapter ergänzt werden, ohne die vorhandene Geschäftslogik zu duplizieren.

# Wetterservice

## Funktion get_weather(city)

`get_weather(city: str) -> str` bereinigt zunächst die Eingabe. Bei einer leeren Stadt liefert die Funktion einen hilfreichen Eingabehinweis. Anschließend entscheidet sie anhand der Umgebungsvariable `OPENWEATHER_API_KEY` zwischen Live- und Demo-Modus.

## OpenWeatherMap-Anbindung

Ist ein Schlüssel vorhanden, verwendet der Service `requests.get()` mit einem Timeout und folgender Konfiguration:

```text
URL:   https://api.openweathermap.org/data/2.5/weather
q:     eingegebene Stadt
appid: OPENWEATHER_API_KEY
units: metric
lang:  de
```

Temperatur, Beschreibung und aufgelöster Stadtname werden aus der JSON-Antwort gelesen und als deutscher Text formatiert. Der API-Key wird niemals im Quellcode hinterlegt.

## Demo-Modus ohne API-Key

Fehlt `OPENWEATHER_API_KEY`, liefert die Funktion deterministische Demo-Daten, beispielsweise `Demo-Wetter für Berlin: 21 °C, leicht bewölkt.` Dieser Modus macht das Projekt für die prüfende Person ohne Zugangsdaten reproduzierbar und testbar.

## Fehlerbehandlung

HTTP-Fehler, Zeitüberschreitungen, ungültiges JSON und fehlende Antwortfelder werden abgefangen. Statt eines technischen Stacktraces erhält die Benutzerin oder der Benutzer eine freundliche Meldung mit der Bitte, es später erneut zu versuchen.

# Terminbuchung

## Funktion create_booking_confirmation(date, time)

`create_booking_confirmation(date: str, time: str) -> str` nimmt Datum und Uhrzeit als Zeichenketten entgegen. Die Funktion besitzt keine externe Abhängigkeit und kann daher besonders einfach getestet werden.

## Validierung

Zunächst wird geprüft, ob beide Werte vorhanden sind. Ein regulärer Ausdruck prüft das Datumsformat `DD.MM.YYYY`. Ein zweiter regulärer Ausdruck prüft das Zeitformat `HH:MM` einschließlich eines gültigen Stunden- und Minutenbereichs von `00:00` bis `23:59`. Bei ungültigen Angaben wird ein konkreter Format-Hinweis zurückgegeben.

## Fiktive Buchungsbestätigung

Ein echtes Kalender- oder Buchungssystem ist nicht Teil des Prototyps. Für gültige Eingaben gibt die Funktion daher bewusst eine fiktive Bestätigung aus: `Ihr Termin wurde fiktiv für den 20.07.2026 um 14:00 Uhr bestätigt.`

# Ausführung

## Installation

Voraussetzung ist eine lokale Python-Installation. Alle Befehle werden im Projektverzeichnis ausgeführt. Es werden keine echten Zugangsdaten mitgeliefert.

## Virtuelle Umgebung

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

## Abhängigkeiten installieren

```powershell
pip install -r requirements.txt
```

## Umgebungsvariablen

`.env.example` zeigt die erwarteten Variablen. Für lokale Live-Tests kann eine eigene, durch `.gitignore` ausgeschlossene `.env` angelegt werden. Sie darf nicht in Git oder die ZIP-Abgabe aufgenommen werden. `TELEGRAM_BOT_TOKEN` ist zum Start des Telegram-Bots erforderlich; `OPENWEATHER_API_KEY` ist für echte Wetterdaten optional. `FLASK_HOST`, `FLASK_PORT` und `FLASK_DEBUG` konfigurieren den lokalen Webserver.

## Webanwendung starten

```powershell
python web_app.py
```

Danach ist die Anwendung standardmäßig unter `http://127.0.0.1:5000` erreichbar.

## Telegram Bot starten

```powershell
python telegram_bot.py
```

Ohne `TELEGRAM_BOT_TOKEN` beendet sich das Programm kontrolliert und gibt einen klaren deutschen Hinweis aus.

## Test ohne API-Keys

Für den Demo-Modus der Webanwendung werden keine Schlüssel benötigt. Ohne OpenWeatherMap-Schlüssel liefert der Wetterservice reproduzierbare Demo-Daten. Der Telegram-Kanal benötigt zwar ein eigenes Telegram-Token für die Verbindung zur Telegram Bot API, kann aber ebenfalls ohne OpenWeatherMap-Schlüssel Wetter-Demoantworten liefern.

# Beispieldialog

## Telegram

```text
User:
/start

Bot:
Willkommen beim Multi-Channel-Chatbot! Die Befehle /wetter und /termin stehen zur Verfügung.

User:
/hilfe

Bot:
Verfügbare Befehle: /start, /hilfe, /wetter [Stadt] und /termin [DD.MM.YYYY] [HH:MM].

User:
/wetter Berlin

Bot:
Demo-Wetter für Berlin: 21 °C, leicht bewölkt. Hinweis: Es wurde kein OpenWeatherMap API-Key gefunden.

User:
/termin 20.07.2026 14:00

Bot:
Ihr Termin wurde fiktiv für den 20.07.2026 um 14:00 Uhr bestätigt.
```

## Web

```text
Wetterformular
Stadt: Berlin
Antwort: Demo-Wetter für Berlin: 21 °C, leicht bewölkt. Hinweis: Es wurde kein OpenWeatherMap API-Key gefunden.

Terminformular
Datum: 20.07.2026
Uhrzeit: 14:00
Antwort: Ihr Termin wurde fiktiv für den 20.07.2026 um 14:00 Uhr bestätigt.
```

Weitere Beispiele für `/start`, `/hilfe` und beide Kanäle enthält `beispiel_dialog.txt`.

# Hinweis zur Abgabe

Die ZIP-Datei trägt den Namen `Angie_Angarita_Soto_Teilprüfung 2.zip` und liegt im Verzeichnis `submission/`. Sie enthält ausschließlich erlaubte Dateitypen und folgende Dateien:

```text
README.md
telegram_bot.py
web_app.py
weather_service.py
booking_service.py
templates/index.html
static/app.js
static/style.css
Bilder/DescriptionPic.png
Bilder/ProfilePic.png
Bilder/Screenshot 01_BotConfiguration.png
requirements.txt
.env.example
beispiel_dialog.txt
hinweis_zur_abgabe.txt
```

`README.md` enthält die Hauptlösung. `.env.example` ist als Konfigurationsvorlage enthalten; eine reale `.env` wird nicht aufgenommen. Die Abgabe enthält keine echten API-Schlüssel, Tokens oder sonstigen Secrets. Der Ordner `Bilder/` mit den drei PNG-Dateien ist Bestandteil der ZIP, weil er BotFather-Konfiguration, Profilbild und Description Picture des Telegram-Bots dokumentiert. Ergänzende Informationen stehen in `hinweis_zur_abgabe.txt`.

# Reflexion und Fazit

Das Projekt demonstriert eine übersichtliche Multi-Channel-Chatbot-Architektur. Die Telegram Bot API bildet den ersten Kanal, während Flask und AJAX eine asynchron bedienbare Weboberfläche als zweiten Kanal bereitstellen. Beide Kanäle verwenden dieselbe Geschäftslogik für Wetter und Termine. Diese Trennung verbessert Wartbarkeit, Konsistenz und Testbarkeit.

Der deterministische Demo-Modus stellt die Reproduzierbarkeit ohne realen OpenWeatherMap API-Key sicher. Weitere Kanäle wie WhatsApp Business oder Microsoft Teams könnten durch zusätzliche Adapter ergänzt werden. Für den akademischen Prototyp wurde die Telegram Standard Privacy Policy verwendet; auf eine separate Datenschutzdatei wurde bewusst verzichtet, damit keine widersprüchlichen parallelen Richtlinien gepflegt werden. Für den Produktivbetrieb wären darüber hinaus robustere fachliche Datumsvalidierung, strukturiertes Logging, Monitoring, Authentifizierung, Rate Limiting sowie ein professionelles und sicheres Secret-Management erforderlich.
