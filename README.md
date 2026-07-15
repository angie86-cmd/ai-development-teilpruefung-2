# Multi-Channel Chatbot - Teilprüfung 2

## Teilprüfung 2

### Aufgabe

Teilprüfung 2

Entwickle einen Multi-Channel Chatbot, der sowohl über Telegram als auch über eine einfache Webanwendung erreichbar ist. Dein Chatbot soll in der Lage sein, Benutzeranfragen zu beantworten, die sich auf Wetterinformationen und Terminbuchungen konzentrieren. Nutze die Telegram Bot API für den Telegram-Teil und Flask für die Webanwendung.

Führe folgende Schritte durch:

1. Erstelle ein Python-Skript für den Telegram Bot, der die Telegram Bot API verwendet. Der Bot soll auf einfache Befehle wie “/wetter [Stadt]” reagieren, indem er aktuelle Wetterinformationen aus einer öffentlichen API (z.B. OpenWeatherMap API) abruft. Für “/termin [Datum] [Zeit]” soll der Bot eine fiktive Buchungsbestätigung senden.

2. Entwickle eine einfache Webanwendung mit Flask, die ein ähnliches Verhalten wie der Telegram Bot zeigt. Die Webanwendung soll ein Formular für Wetteranfragen und Terminbuchungen enthalten. Nutze AJAX, um die Anfragen asynchron zu bearbeiten und die Antworten ohne Neuladen der Seite anzuzeigen.

---

# Lösung

## Einleitung

Für die Teilprüfung wurde ein Multi-Channel-Chatbot mit zwei Zugangskanälen umgesetzt: Telegram und eine browserbasierte Webanwendung. Beide Kanäle decken die Anwendungsfälle Wetterabfrage und fiktive Terminbuchung ab. Sie greifen auf dieselbe gemeinsame Geschäftslogik zurück, sodass Regeln und Antworten nicht doppelt implementiert werden.

Das Projekt wird mit Git versioniert und kann über GitHub unter [https://github.com/angie86-cmd/ai-development-teilpruefung-2](https://github.com/angie86-cmd/ai-development-teilpruefung-2) bereitgestellt werden. Die finale ZIP-Datei liegt im Verzeichnis `submission/`. Weder die Projektdateien noch die Abgabe enthalten echte Tokens, API-Schlüssel oder andere Secrets. Benötigte Umgebungsvariablen werden ausschließlich durch Platzhalter in `.env.example` dokumentiert.

Der Telegram-Bot wurde über BotFather eingerichtet. Die konkrete Bot-Konfiguration, die verwendete Telegram Standard Privacy Policy und die zugehörigen Bildnachweise werden in Abschnitt 1.4 dokumentiert.

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

Die gewählte Struktur trennt Dokumentation, Telegram-Kanallogik, Web-Kanallogik, gemeinsame Geschäftslogik, Frontend-Dateien, Konfigurationsbeispiele, Bildnachweise und Abgabedateien klar voneinander. `telegram_bot.py` enthält ausschließlich die Telegram-spezifische Kanallogik. Der Webkanal verteilt sich auf `web_app.py`, `templates/index.html`, `static/app.js` und `static/style.css`. Die von beiden Kanälen verwendeten fachlichen Funktionen liegen zentral in `weather_service.py` und `booking_service.py`. Dadurch wird doppelter Code vermieden und das Projekt lässt sich leichter testen, warten und erweitern.

Weitere Kanäle wie WhatsApp Business, Microsoft Teams oder Slack könnten später als zusätzliche Adapter ergänzt werden, ohne die zentrale Geschäftslogik neu zu schreiben. `Bilder/` dokumentiert die BotFather-Konfiguration und die visuelle Einrichtung des Bots; `submission/` enthält das finale ZIP-Archiv. Git und GitHub dienen der nachvollziehbaren Versionierung und Dokumentation des Entwicklungsprozesses.

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

# 1. Telegram Bot mit Telegram Bot API

## 1.1 Ziel des Telegram-Bots

Der Telegram-Kanal in `telegram_bot.py` ermöglicht Wetterabfragen und fiktive Terminbuchungen direkt im Messenger. Telegram ist über die Aufgabenanforderung hinaus für einen schnellen akademischen Prototyp geeignet: Die Telegram Bot API ist entwicklungsfreundlich nutzbar, erfordert keine komplexe Unternehmensverifizierung und für diesen Prototyp keine zusätzliche Plattformlizenz. BotFather macht die Einrichtung des Bots und seiner Befehle schnell und transparent.

Durch Polling kann der Bot lokal getestet werden, ohne einen öffentlichen Server oder Webhook bereitzustellen. Telegram ist damit unter begrenzten zeitlichen und technischen Ressourcen ein praktischer Kanal, um eine Multi-Channel-Architektur zu demonstrieren. In einer realen Unternehmensumgebung könnten später weitere Adapter für WhatsApp Business, Microsoft Teams oder Slack ergänzt werden.

## 1.2 Architektur des Telegram-Kanals

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

Die Telegram-Schicht enthält bewusst nur kanalspezifische Aufgaben: Sie empfängt Befehle, liest deren Argumente und sendet Antworten über Telegram zurück. Wetter- oder Buchungsregeln werden dort nicht erneut implementiert; `telegram_bot.py` ruft dafür `weather_service.py` beziehungsweise `booking_service.py` auf. Diese Trennung von Kanallogik und Geschäftslogik erleichtert Tests, Wartung und Erweiterungen. Zugleich können künftige Kanäle dieselben Services wiederverwenden.

## 1.3 Unterstützte Befehle

Der Bot nutzt `python-telegram-bot` im Stil der Version 20 oder neuer mit `ApplicationBuilder`, `CommandHandler`, `ContextTypes` und asynchronen Handlerfunktionen. Konfiguriert wurden ausschließlich `/start`, `/hilfe`, `/wetter` und `/termin`. Diese bewusste Begrenzung bildet ein tragfähiges Minimum Viable Product (MVP), das sich auf die geforderten Anwendungsfälle Wetterabfrage und fiktive Terminbuchung konzentriert.

Zusätzliche Befehle wurden vermieden, damit der Prototyp verständlich, testbar und eng an der Teilprüfung ausgerichtet bleibt. Der kleine Befehlsumfang reduziert die Komplexität und vereinfacht manuelle Tests. Die in BotFather hinterlegte Befehlsliste entspricht den in Python registrierten Command-Handlern.

**Tabelle 2: Telegram-Befehle**

| Command | Zweck | Beispiel |
|---|---|---|
| `/start` | Begrüßt und nennt die zentralen Möglichkeiten | `/start` |
| `/hilfe` | Zeigt Befehle und Eingabeformate | `/hilfe` |
| `/wetter [Stadt]` | Fragt Wetter- oder Demo-Wetterdaten ab | `/wetter Berlin` |
| `/termin [Datum] [Zeit]` | Erstellt eine fiktive Terminbestätigung | `/termin 20.07.2026 14:00` |

## 1.4 BotFather-Konfiguration

Der Bot wurde in BotFather mit folgenden öffentlich sichtbaren Angaben konfiguriert:

- **Bot-Benutzername:** `@angie_weather_booking_bot`
- **Bot-Name:** `AngieWeatherAppointmentBot`
- **About:** Multi-Channel Chatbot für Wetterinformationen und fiktive Terminbuchungen.
- **Description:** Dieser Bot ist ein Prototyp für die AI-Development Teilprüfung 2. Er beantwortet einfache Wetteranfragen und erstellt fiktive Terminbuchungsbestätigungen.
- **Verfügbare Befehle:**
  - `/start - Bot starten`
  - `/hilfe - Hilfe anzeigen`
  - `/wetter Berlin - Wetterinformationen abrufen`
  - `/termin 20.07.2026 14:00 - Fiktiven Termin buchen`
- **Privacy Policy:** [https://telegram.org/privacy-tpa](https://telegram.org/privacy-tpa)

**Abbildung 1: Telegram BotFather-Konfiguration**

![Telegram Bot Konfiguration](Bilder/Screenshot%2001_BotConfiguration.png)

Abbildung 1 zeigt die konfigurierte BotFather-Übersicht mit Botname, Beschreibung, Befehlen, Bildkonfiguration und verwendeter Telegram Standard Privacy Policy.

**Abbildung 2: Telegram Bot Profilbild**

![Telegram Bot Profilbild](Bilder/ProfilePic.png)

Abbildung 2 zeigt das Profilbild des Bots, das den Wetter- und Termin-Anwendungsfall visuell darstellt.

**Abbildung 3: Telegram Bot Description Picture**

![Telegram Bot Description Picture](Bilder/DescriptionPic.png)

Abbildung 3 zeigt das Description Picture, das im Bereich „What can this bot do?“ angezeigt wird.

## 1.5 Verwendung gemeinsamer Geschäftslogik

`telegram_bot.py` implementiert weder Wetterabfragen noch Buchungsvalidierung selbst. `weather_command()` verbindet die Befehlsargumente zu einem Stadtnamen und delegiert an `get_weather()`. `appointment_command()` übergibt Datum und Uhrzeit an `create_booking_confirmation()`. Dadurch wird fachliche Logik nicht dupliziert und Telegram sowie Web liefern konsistente Antworten. Die zentrale Ablage unterstützt Wartbarkeit und die spätere Ergänzung weiterer Kanäle.

## 1.6 Authentifizierung über Umgebungsvariable

Beim Start lädt `python-dotenv` lokale Umgebungsvariablen; `TELEGRAM_BOT_TOKEN` wird anschließend mit `os.getenv()` gelesen. Das Token wird wie ein Passwort beziehungsweise Secret behandelt. Es darf weder in `README.md`, Screenshots, Quellcode, Commits, GitHub noch in der ZIP-Abgabe erscheinen. Eine lokale `.env` ist durch `.gitignore` ausgeschlossen. Die enthaltene `.env.example` dokumentiert dagegen sicher die benötigten Variablen, ohne reale Zugangsdaten offenzulegen.

Dieses Vorgehen entspricht grundlegenden Sicherheits- und Datenschutzprinzipien. Für den akademischen Prototyp gilt ausschließlich die [Telegram Standard Privacy Policy](https://telegram.org/privacy-tpa); eine parallele Datenschutzdatei wird bewusst nicht gepflegt. Die Anwendung speichert keine personenbezogenen Daten dauerhaft, erstellt keine realen Termine und fordert keine sensiblen Daten an.

## 1.7 Umgang mit fehlendem Telegram Token

Ist `TELEGRAM_BOT_TOKEN` leer oder nicht vorhanden, gibt `telegram_bot.py` eine klare deutsche Meldung aus und beendet sich kontrolliert. So entstehen bei der Bewertung weder ein Absturz noch ein unklarer Stacktrace; README und Code können ohne reale Zugangsdaten geprüft werden. Dieses Verhalten ist Teil einer sicheren Konfigurationsbehandlung.

Auch in diesem Fehlerfall bleiben die Schutzregeln unverändert: Kein Token steht in README, Code, Screenshots, GitHub oder ZIP. `.env` bleibt lokal und ignoriert, während `.env.example` als sichere Vorlage enthalten ist. Ergänzend gilt die [Telegram Standard Privacy Policy](https://telegram.org/privacy-tpa). Der Prototyp speichert keine personenbezogenen Daten dauerhaft, erzeugt keine echten Termine und verlangt keine sensiblen Angaben.

## 1.8 Datenschutz und Bot Privacy Policy

In BotFather ist die [Telegram Standard Privacy Policy](https://telegram.org/privacy-tpa) konfiguriert. Sie ist für diesen akademischen Prototyp angemessen, weil die Anwendung keine personenbezogenen Daten dauerhaft speichert, keine realen Termine erzeugt und keine sensiblen Daten anfordert. Echte Tokens und API-Schlüssel werden ausschließlich lokal über Umgebungsvariablen bereitgestellt und durch `.gitignore` von Git ausgeschlossen.

## 1.9 Erklärung des Codes für den Telegram-Kanal

`telegram_bot.py` enthält ausschließlich Telegram-spezifische Kanallogik. Die vier Handler sind als `async def` definiert, weil `python-telegram-bot` ab Version 20 asynchrone Handler verwendet. Sie erhalten ein Telegram-`Update` und einen `Context` und senden Antworten mit `await update.message.reply_text(...)`. Wetter- und Terminlogik werden nicht in diesem Adapter implementiert, sondern an `weather_service.py` und `booking_service.py` delegiert. Erläuterungen im Python-Code stehen als `#`-Kommentare oberhalb der zugehörigen Funktionen und nicht als Docstrings.

1. **`main()`** benötigt keine Parameter und liefert keinen Rückgabewert. Die Funktion lädt die lokale Konfiguration, prüft `TELEGRAM_BOT_TOKEN`, erstellt die `Application`, registriert alle Command-Handler und startet das Polling. Sie gehört als Einstiegspunkt in `telegram_bot.py`, weil sie den gesamten Telegram-Kanal initialisiert. Polling ermöglicht dabei lokale Tests ohne öffentlichen Server oder Webhook.
2. **`start_command(update, context)`** verarbeitet `/start`. Der Handler erhält das eingehende Telegram-Update und den Kontext und sendet eine Begrüßung mit Nutzungshinweisen zurück. Begrüßung und Antworttransport sind kanalspezifisch und gehören deshalb in den Telegram-Adapter.
3. **`help_command(update, context)`** verarbeitet `/hilfe` und gibt die unterstützten Befehle sowie Eingabeformate aus. Die Funktion beschreibt die Bedienoberfläche des Telegram-Kanals, enthält jedoch keine fachlichen Regeln.
4. **`weather_command(update, context)`** liest die Argumente hinter `/wetter`, bildet daraus den Stadtnamen und übergibt ihn an `get_weather()`. Der zurückgegebene deutsche Antworttext wird über Telegram gesendet; die Wetterermittlung verbleibt vollständig im gemeinsamen Wetterservice.
5. **`appointment_command(update, context)`** liest Datum und Uhrzeit hinter `/termin` und ruft `create_booking_confirmation()` auf. Der Handler sendet die Bestätigung oder Fehlermeldung zurück und übernimmt ausschließlich die Übersetzung zwischen Telegram-Befehl und gemeinsamem Buchungsservice.

Die geordnete Aufteilung hält die Handler klein, ermöglicht konsistente Antworten in beiden Kanälen und trennt Telegram-Kommunikation klar von der wiederverwendbaren Geschäftslogik.

# 2. Flask-Webanwendung mit AJAX

## 2.1 Ziel der Webanwendung

Die Flask-Webanwendung bietet dieselben zwei Anwendungsfälle wie Telegram über eine leicht bedienbare Browseroberfläche. Dadurch lässt sich der Chatbot auch ohne Telegram-Konto demonstrieren.

## 2.2 Architektur der Webanwendung

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

## 2.3 Flask-Routen

`web_app.py` implementiert eine HTML-Route und zwei JSON-Endpunkte.

**Tabelle 3: Flask-Routen**

| Route | Methode | Zweck |
|---|---|---|
| `/` | GET | Rendert `templates/index.html` |
| `/api/weather` | POST | Liest `city` aus JSON und gibt die Wetterantwort als JSON zurück |
| `/api/appointment` | POST | Liest `date` und `time` aus JSON und gibt die Terminantwort als JSON zurück |

Die zugehörigen Python-Funktionen bilden ausschließlich den Webkanal ab:

- **`index()`** verarbeitet einen GET-Aufruf auf `/`, benötigt keine fachlichen Eingabedaten und gibt das gerenderte Template `templates/index.html` zurück. Die Funktion gehört zum Webkanal, weil sie die Browseroberfläche bereitstellt.
- **`weather_api()`** verarbeitet POST-JSON auf `/api/weather`, liest das Feld `city` und übergibt dessen Wert an die gemeinsame Funktion `get_weather()`. Als Ausgabe liefert sie eine JSON-Antwort mit dem erzeugten Meldungstext. Flask übernimmt hier nur HTTP- und JSON-Verarbeitung; die Wetterlogik bleibt im Service.
- **`appointment_api()`** verarbeitet POST-JSON auf `/api/appointment`, liest `date` und `time` und delegiert an `create_booking_confirmation()`. Der Bestätigungs- oder Fehlertext wird als JSON zurückgegeben. Damit gehört auch diese Funktion als Übersetzer zwischen HTTP-Anfrage und gemeinsamer Geschäftslogik zum Webkanal.

## 2.4 AJAX-Verarbeitung

`static/app.js` registriert nach `DOMContentLoaded` Ereignisbehandlungen für beide Formulare. Die Hilfsfunktion `postJson()` sendet die Eingaben mit `fetch`, der Methode POST und dem Content-Type `application/json` an Flask. Netzwerk- und HTTP-Fehler werden abgefangen und verständlich angezeigt.

## 2.5 Wetterformular

Das Wetterformular in `templates/index.html` nimmt eine Stadt entgegen. Nach dem Absenden wird `{ "city": "Berlin" }` an `/api/weather` übertragen. Der Endpunkt ruft `get_weather()` auf und sendet dessen Ergebnis zurück.

## 2.6 Terminformular

Das Terminformular erfasst Datum und Uhrzeit. Die Werte werden als JSON an `/api/appointment` gesendet und durch `create_booking_confirmation()` geprüft. Der Hinweis im Formular macht die erwarteten Formate transparent.

## 2.7 Antwort ohne Neuladen der Seite

`event.preventDefault()` verhindert das reguläre Neuladen beim Absenden. `static/app.js` sendet mit AJAX beziehungsweise `fetch` asynchrone POST-Anfragen als JSON an den passenden Flask-Endpunkt. Flask gibt eine JSON-Antwort zurück, deren Meldung JavaScript in den jeweiligen Ergebnisbereich schreibt. Die Seite wird dabei nicht neu geladen; damit ist die entsprechende Anforderung der Teilprüfung unmittelbar erfüllt.

`aria-live="polite"` sorgt zusätzlich dafür, dass unterstützende Technologien aktualisierte Antworten ankündigen können. Die Weboberfläche bleibt bewusst einfach, weil der Schwerpunkt auf der Multi-Channel-Architektur und der asynchronen Interaktion liegt.

## 2.8 Gemeinsame Nutzung der Services

Der Webkanal importiert dieselben Funktionen `get_weather()` und `create_booking_confirmation()` wie der Telegram-Bot. Damit gelten für beide Kanäle dieselben Validierungsregeln, Demo-Daten und Antworttexte. Diese gemeinsame Nutzung vermeidet doppelte Implementierungen und erleichtert Wartung und Tests. Die Services kennen weder Flask- noch Telegram-Objekte und bleiben deshalb vollständig kanalunabhängig.

## 2.9 Wetterservice

### 2.9.1 Funktion get_weather(city)

`get_weather(city: str) -> str` ist die zentrale Funktion für Wetteranfragen. Sie erhält einen Stadtnamen, bereinigt die Eingabe und gibt stets einen deutschen Antworttext zurück. Da sie weder Telegram- noch Flask-Objekte verwendet, ist sie kanalunabhängig und kann von beiden Kanälen aufgerufen werden. Anschließend entscheidet sie anhand der Umgebungsvariable `OPENWEATHER_API_KEY` zwischen Live- und Demo-Modus.

### 2.9.2 OpenWeatherMap-Anbindung

Ist ein Schlüssel vorhanden, verwendet der Service `requests.get()` mit einem Timeout und folgender Konfiguration:

```text
URL:   https://api.openweathermap.org/data/2.5/weather
q:     eingegebene Stadt
appid: OPENWEATHER_API_KEY
units: metric
lang:  de
```

Die Anfrage übermittelt den eingegebenen Stadtnamen, metrische Einheiten und die deutsche Spracheinstellung. Temperatur, Beschreibung und aufgelöster Stadtname werden aus der JSON-Antwort gelesen und als deutscher Text formatiert. Der API-Key wird ausschließlich aus der Umgebung geladen und niemals im Quellcode hinterlegt.

### 2.9.3 Demo-Modus ohne API-Key

Fehlt `OPENWEATHER_API_KEY`, liefert die Funktion deterministische Demo-Daten, beispielsweise `Demo-Wetter für Berlin: 21 °C, leicht bewölkt.` Dieser Modus macht das Projekt für prüfende Personen ohne externe Zugangsdaten testbar und stellt die Reproduzierbarkeit der Abgabe sicher.

### 2.9.4 Fehlerbehandlung

Eine fehlende Stadt führt zu einem konkreten Eingabehinweis. HTTP- und API-Fehler, Zeitüberschreitungen, ungültiges JSON und fehlende Antwortfelder werden ebenfalls kontrolliert behandelt. Statt eines technischen Stacktraces erhalten Benutzerinnen und Benutzer eine freundliche deutsche Rückfallmeldung.

## 2.10 Terminbuchung

### 2.10.1 Funktion create_booking_confirmation(date, time)

`create_booking_confirmation(date: str, time: str) -> str` erzeugt eine fiktive Terminbestätigung. Die Funktion nimmt Datum und Uhrzeit als Zeichenketten entgegen und gibt einen deutschen Bestätigungs- oder Fehlertext zurück. Sie besitzt keine Kanalabhängigkeit, wird von Telegram und Web wiederverwendet und kann isoliert getestet werden.

### 2.10.2 Validierung

Zunächst wird geprüft, ob Datum und Uhrzeit vorhanden sind. Ein regulärer Ausdruck validiert das Datumsformat `DD.MM.YYYY`. Ein zweiter regulärer Ausdruck prüft das Zeitformat `HH:MM` einschließlich eines gültigen Stunden- und Minutenbereichs von `00:00` bis `23:59`. Fehlende oder ungültige Angaben führen zu hilfreichen deutschen Fehlermeldungen.

### 2.10.3 Fiktive Buchungsbestätigung

Ein echtes Kalender- oder Buchungssystem ist nicht Teil des Prototyps; es wird kein Termin gespeichert. Für gültige Eingaben gibt die Funktion ausdrücklich eine fiktive Bestätigung aus: `Ihr Termin wurde fiktiv für den 20.07.2026 um 14:00 Uhr bestätigt.` Damit wird die Anforderung der Teilprüfung erfüllt, ohne reale personenbezogene Buchungsdaten zu verarbeiten.

## 2.11 Gemeinsame Geschäftslogik

### 2.11.1 Gemeinsame Services

`weather_service.py` und `booking_service.py` bilden die gemeinsamen Services des Projekts. Sowohl Telegram als auch Web rufen deren Funktionen auf. Die zentrale Implementierung verhindert doppelten Code und sorgt dafür, dass beide Kanäle dieselben Validierungen und Antworttexte verwenden.

### 2.11.2 Trennung von Kanal und Geschäftslogik

```text
Telegram Channel ──┐
                   ├── Shared Business Logic
Web Channel ───────┘
                        ├── weather_service.py
                        └── booking_service.py
```

Telegram-spezifischer Code bleibt in `telegram_bot.py`. Web-spezifischer Code liegt in `web_app.py`, `templates/index.html`, `static/app.js` und `static/style.css`. Die fachlichen Regeln befinden sich dagegen in `weather_service.py` und `booking_service.py`. Diese Trennung der Verantwortlichkeiten ist die zentrale Architekturentscheidung des Projekts.

### 2.11.3 Vorteile der Architektur

Die Services können unabhängig von den Kanälen getestet und gewartet werden. Beide Oberflächen verhalten sich konsistent, weil sie dieselben Funktionen verwenden. Weitere Adapter für WhatsApp Business, Microsoft Teams oder Slack könnten später ergänzt werden, ohne die zentrale Wetter- oder Buchungslogik neu zu implementieren.

## 2.12 Erklärung des Codes für die Webanwendung und die gemeinsamen Services

`web_app.py` enthält ausschließlich die Logik des Webkanals, während `weather_service.py` und `booking_service.py` die gemeinsam verwendete Geschäftslogik bereitstellen. Die Python-Dateien verwenden für Erläuterungen gezielte `#`-Kommentare statt Docstrings. Die Funktionen sind wie folgt aufgeteilt:

1. **`index()` in `web_app.py`** verarbeitet den GET-Aufruf auf `/`. Die Funktion benötigt keine fachlichen Eingabedaten und gibt das gerenderte Template `templates/index.html` zurück. Sie gehört in den Flask-Adapter, weil sie die Browseroberfläche bereitstellt.
2. **`weather_api()` in `web_app.py`** verarbeitet POST-JSON auf `/api/weather`, liest `city` und übergibt den Wert an `get_weather()`. Als Ausgabe liefert sie eine JSON-Nachricht. Die Funktion verbindet HTTP und JSON mit dem kanalunabhängigen Wetterservice, ohne Wetterlogik zu duplizieren.
3. **`appointment_api()` in `web_app.py`** verarbeitet POST-JSON auf `/api/appointment` und liest `date` sowie `time`. Sie delegiert an `create_booking_confirmation()` und gibt dessen Bestätigung oder Fehlermeldung als JSON zurück. Damit bleibt die Funktion auf die Webkanal-Übersetzung beschränkt.
4. **`_is_truthy(value)` in `web_app.py`** erhält den Text einer Umgebungsvariable und gibt einen booleschen Wert zurück. Die Hilfsfunktion interpretiert `FLASK_DEBUG` eindeutig und gehört zur lokalen Flask-Serverkonfiguration.
5. **`main()` in `web_app.py`** benötigt keine Parameter und liefert keinen fachlichen Rückgabewert. Sie lädt die Umgebungsvariablen, liest Host, Port und Debug-Modus, behandelt einen ungültigen Port und startet den Flask-Entwicklungsserver. Als Einstiegspunkt initialisiert sie den Webkanal.
6. **`get_weather(city)` in `weather_service.py`** erhält einen Stadtnamen und gibt einen deutschen Wetter-, Demo- oder Fehlertext zurück. Die Funktion validiert die Eingabe, wählt den Betriebsmodus und verarbeitet die externe API-Antwort. Da sie keine Kanalobjekte kennt, unterstützt sie Web und Telegram gleichermaßen.
7. **`_demo_weather(city)` in `weather_service.py`** erhält einen bereinigten Stadtnamen und erzeugt eine feste deutsche Demoantwort. Die interne Hilfsfunktion gehört zum Wetterservice und gewährleistet reproduzierbare Tests ohne OpenWeatherMap API-Key.
8. **`create_booking_confirmation(date, time)` in `booking_service.py`** erhält Datum und Uhrzeit und gibt einen deutschen Fehler- oder Bestätigungstext zurück. Die Funktion kapselt Formatprüfung und fiktive Bestätigung unabhängig von Flask und Telegram.

Im Browser wartet `static/app.js` auf `DOMContentLoaded`, registriert die Formular-Handler und sendet mit `fetch` asynchrone POST-Anfragen. Nach der JSON-Antwort aktualisiert JavaScript die jeweiligen Ergebnisbereiche, ohne die Seite neu zu laden. Damit ergänzt das Skript den Flask-Adapter um die geforderte asynchrone Interaktion.

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
