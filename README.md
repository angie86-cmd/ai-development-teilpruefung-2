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

`telegram_bot.py` enthält ausschließlich Telegram-spezifische Kanallogik. Die Handler sind als `async def` definiert, weil `python-telegram-bot` ab Version 20 asynchrone Handler verwendet. Wetter- und Terminlogik werden nicht im Telegram-Adapter implementiert, sondern an `weather_service.py` und `booking_service.py` delegiert.

### 1.9.1 Funktion main()

`main()` initialisiert den vollständigen Telegram-Kanal und bildet den Einstiegspunkt des Skripts.

```python
def main() -> None:
    load_dotenv()
    token = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
    if not token:
        print(
            "Telegram-Bot wurde nicht gestartet: Die Umgebungsvariable "
            "TELEGRAM_BOT_TOKEN fehlt. Bitte hinterlegen Sie lokal ein gültiges "
            "Token (nicht im Repository)."
        )
        return

    application = ApplicationBuilder().token(token).build()
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("hilfe", help_command))
    application.add_handler(CommandHandler("wetter", weather_command))
    application.add_handler(CommandHandler("termin", appointment_command))
    print("Telegram-Bot wird im Polling-Modus gestartet.")
    application.run_polling()
```

Die Funktion benötigt keine Parameter und besitzt keinen fachlichen Rückgabewert. Sie lädt lokale Umgebungsvariablen, prüft das Bot-Token, erstellt die Telegram-`Application`, registriert die vier Handler und startet das Polling. Ohne Token beendet sie sich kontrolliert. Diese Initialisierung gehört in `telegram_bot.py`, weil sie ausschließlich den Telegram-Kanal konfiguriert; fachliche Services werden erst durch die registrierten Handler aufgerufen.

### 1.9.2 Funktion start_command()

Der Start-Handler begrüßt Benutzerinnen und Benutzer und nennt die zentralen Nutzungsmöglichkeiten.

```python
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    del context  # Der Kontext wird für diesen Befehl nicht benötigt.
    if update.message:
        await update.message.reply_text(
            "Willkommen beim Multi-Channel-Chatbot!\n"
            "Mit /wetter [Stadt] erhalten Sie Wetterinformationen.\n"
            "Mit /termin [Datum] [Zeit] buchen Sie einen fiktiven Termin.\n"
            "Weitere Informationen: /hilfe"
        )
```

Eingaben sind das Telegram-`Update` und der von der Bibliothek bereitgestellte `Context`. Da für `/start` keine Argumente benötigt werden, wird der Kontext verworfen. Als Effekt sendet die Funktion eine Telegram-Nachricht; einen Rückgabewert erzeugt sie nicht. Sie gehört in den Kanaladapter, weil Begrüßung und Nachrichtentransport Telegram-spezifisch sind und kein gemeinsamer Service benötigt wird.

### 1.9.3 Funktion help_command()

`help_command()` dokumentiert die verfügbaren Telegram-Befehle unmittelbar im Chat.

```python
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    del context
    if update.message:
        await update.message.reply_text(
            "Verfügbare Befehle:\n"
            "/start – Begrüßung anzeigen\n"
            "/hilfe – Hilfe anzeigen\n"
            "/wetter [Stadt] – z. B. /wetter Berlin\n"
            "/termin [DD.MM.YYYY] [HH:MM] – z. B. /termin 20.07.2026 14:00"
        )
```

Auch dieser asynchrone Handler erhält `Update` und `Context`, benötigt jedoch keine Befehlsargumente. Er sendet einen formatierten Hilfetext und hat keinen fachlichen Rückgabewert. Die Funktion bleibt in `telegram_bot.py`, weil sie die Telegram-Bedienoberfläche beschreibt und weder Wetter- noch Buchungslogik ausführt.

### 1.9.4 Funktion weather_command()

Der Wetter-Handler übersetzt den Telegram-Befehl in einen Aufruf des gemeinsamen Wetterservices.

```python
async def weather_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    city = " ".join(context.args).strip()
    response = get_weather(city)
    if update.message:
        await update.message.reply_text(response)
```

Die Eingabe besteht aus den Argumenten hinter `/wetter`, die zu einem Stadtnamen verbunden werden. `get_weather()` liefert den deutschen Antworttext, den der Handler anschließend über Telegram sendet. Die Funktion gehört als Übersetzer zwischen Telegram und Service in `telegram_bot.py`; Wetterabfrage, Demo-Modus und Fehlerbehandlung bleiben vollständig in `weather_service.py`.

### 1.9.5 Funktion appointment_command()

Der Termin-Handler liest Datum und Uhrzeit und delegiert die Validierung an den Buchungsservice.

```python
async def appointment_command(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    date = context.args[0] if len(context.args) >= 1 else ""
    time = context.args[1] if len(context.args) >= 2 else ""
    response = create_booking_confirmation(date, time)
    if update.message:
        await update.message.reply_text(response)
```

Als Eingabe dienen die ersten beiden Befehlsargumente; fehlende Werte werden als leere Strings an den Service weitergegeben. `create_booking_confirmation()` erzeugt eine Fehlermeldung oder fiktive Bestätigung, die der Handler über Telegram ausgibt. Die Funktion bleibt kanalspezifisch, während Formatprüfung und Bestätigung in `booking_service.py` wiederverwendbar implementiert sind.

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

### 2.3.1 Route `/`

Die Startseitenroute stellt die Benutzeroberfläche aus `templates/index.html` bereit.

```python
# Rendert für die Startseite das Template templates/index.html.
@app.get("/")
def index():
    return render_template("index.html")
```

`index()` verarbeitet einen GET-Aufruf ohne fachliche Eingabedaten und gibt das gerenderte HTML-Template zurück. Die Funktion gehört zu `web_app.py`, weil sie die Browseroberfläche des Webkanals ausliefert und keine gemeinsame Geschäftslogik benötigt.

### 2.3.2 Route `/api/weather`

Der Wetter-Endpunkt akzeptiert eine POST-Anfrage mit dem JSON-Feld `city`.

```python
# Empfängt POST-JSON mit "city" und gibt die Antwort von get_weather() als JSON aus.
@app.post("/api/weather")
def weather_api():
    payload = request.get_json(silent=True) or {}
    return jsonify({"message": get_weather(str(payload.get("city", "")))})
```

`weather_api()` liest den JSON-Inhalt fehlertolerant, übergibt den Stadtnamen an `get_weather()` und liefert dessen Text unter `message` als JSON zurück. Damit verarbeitet die Funktion ausschließlich HTTP und JSON; die eigentliche Wetterlogik verbleibt im kanalunabhängigen Service.

### 2.3.3 Route `/api/appointment`

Der Termin-Endpunkt akzeptiert POST-JSON mit `date` und `time`.

```python
# Empfängt POST-JSON mit "date" und "time" und delegiert an den Buchungsservice.
@app.post("/api/appointment")
def appointment_api():
    payload = request.get_json(silent=True) or {}
    message = create_booking_confirmation(
        str(payload.get("date", "")), str(payload.get("time", ""))
    )
    return jsonify({"message": message})
```

`appointment_api()` liest Datum und Uhrzeit, ruft `create_booking_confirmation()` auf und gibt die Bestätigung oder Fehlermeldung als JSON aus. Der Endpunkt gehört zum Flask-Kanal, während Validierung und fiktive Buchung im gemeinsamen Service gekapselt bleiben.

## 2.4 AJAX-Verarbeitung

### 2.4.1 Initialisierung nach dem Laden der Seite

`DOMContentLoaded` stellt sicher, dass Formulare und Ergebnisbereiche im DOM vorhanden sind, bevor JavaScript sie auswählt und Event Listener registriert. Die folgende gekürzte Struktur zeigt den äußeren Rahmen; die darin enthaltenen Funktionen und Handler werden anschließend vollständig wiedergegeben.

```javascript
document.addEventListener("DOMContentLoaded", () => {
    const weatherForm = document.querySelector("#weather-form");
    const appointmentForm = document.querySelector("#appointment-form");
    const weatherResult = document.querySelector("#weather-result");
    const appointmentResult = document.querySelector("#appointment-result");

    // ...
});
```

Die vier Konstanten referenzieren exakt die IDs aus `templates/index.html`. Dadurch werden Listener und Rückmeldungen erst verbunden, nachdem die Seitenstruktur geladen wurde.

### 2.4.2 Funktion postJson(url, payload)

Die interne Hilfsfunktion bündelt den wiederkehrenden asynchronen JSON-Aufruf an Flask.

```javascript
    async function postJson(url, payload) {
        const response = await fetch(url, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload),
        });
        if (!response.ok) {
            throw new Error(`HTTP-Fehler ${response.status}`);
        }
        return response.json();
    }
```

`postJson()` erhält die Ziel-URL und ein Nutzdatenobjekt. `fetch` sendet dieses Objekt als JSON per POST. `response.ok` verhindert, dass HTTP-Fehler als erfolgreiche Antworten weiterverarbeitet werden. Bei Erfolg gibt die Funktion das asynchron geparste JSON zurück.

### 2.4.3 AJAX-Verarbeitung der Wetteranfrage

Der Submit-Handler verarbeitet das Wetterformular vollständig ohne Seitenneuladen.

```javascript
    weatherForm.addEventListener("submit", async (event) => {
        event.preventDefault();
        weatherResult.textContent = "Wetterdaten werden geladen …";
        try {
            const data = await postJson("/api/weather", {
                city: document.querySelector("#city").value,
            });
            // Zeigt die vom Flask-Endpunkt gelieferte JSON-Nachricht direkt an.
            weatherResult.textContent = data.message;
        } catch (error) {
            console.error(error);
            // Eine verständliche Meldung ersetzt technische Fehlerdetails für Nutzende.
            weatherResult.textContent =
                "Die Wetteranfrage konnte nicht verarbeitet werden. Bitte versuchen Sie es erneut.";
        }
    });
```

`event.preventDefault()` unterdrückt das reguläre Absenden und damit den Seitenreload. Während der Anfrage erscheint ein Ladetext. Anschließend wird die Stadt an `/api/weather` gesendet und `data.message` im Ergebnisbereich dargestellt. Netzwerk- und HTTP-Fehler führen zu einer nutzerfreundlichen Rückmeldung.

### 2.4.4 AJAX-Verarbeitung der Terminbuchung

Der zweite Submit-Handler überträgt Datum und Uhrzeit an den Termin-Endpunkt.

```javascript
    appointmentForm.addEventListener("submit", async (event) => {
        event.preventDefault();
        appointmentResult.textContent = "Termin wird geprüft …";
        try {
            const data = await postJson("/api/appointment", {
                date: document.querySelector("#date").value,
                time: document.querySelector("#time").value,
            });
            // Aktualisiert den Termin-Ergebnisbereich mit der JSON-Antwort.
            appointmentResult.textContent = data.message;
        } catch (error) {
            console.error(error);
            // Auch Netzwerk- oder Serverfehler werden nutzerfreundlich dargestellt.
            appointmentResult.textContent =
                "Die Terminbuchung konnte nicht verarbeitet werden. Bitte versuchen Sie es erneut.";
        }
    });
```

Auch hier verhindert `event.preventDefault()` den Seitenreload. Der Handler sendet `date` und `time` an `/api/appointment`, zeigt die zurückgegebene Meldung an und behandelt Fehler mit einem verständlichen Text. Beide Handler erfüllen damit die geforderte asynchrone Bedienung der Webanwendung.

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

Die Routen `index()`, `weather_api()` und `appointment_api()` sind bereits mit ihrem Originalcode in Abschnitt 2.3 erläutert. Dieser Abschnitt konzentriert sich deshalb auf Serverkonfiguration und gemeinsame Services. `web_app.py` enthält Webkanal-Logik, während `weather_service.py` und `booking_service.py` kanalunabhängige Geschäftslogik bereitstellen.

### 2.12.1 Funktion _is_truthy()

Die Hilfsfunktion interpretiert textbasierte Umgebungsvariablen für `FLASK_DEBUG`.

```python
def _is_truthy(value: str) -> bool:
    return value.strip().lower() in {"1", "true", "yes", "on"}
```

Als Eingabe erhält `_is_truthy()` einen String und gibt einen booleschen Wert zurück. Durch Normalisierung von Leerraum und Groß-/Kleinschreibung werden übliche Wahrheitswerte zuverlässig erkannt. Die Funktion gehört in `web_app.py`, weil sie ausschließlich die lokale Flask-Konfiguration unterstützt.

### 2.12.2 Funktion main() in web_app.py

`main()` liest die Serverkonfiguration und startet den lokalen Flask-Entwicklungsserver.

```python
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
```

Die Funktion benötigt keine Parameter und liefert keinen fachlichen Rückgabewert. Sie lädt Umgebungsvariablen, liest `FLASK_HOST`, `FLASK_PORT` und `FLASK_DEBUG`, wandelt den Port kontrolliert in eine Ganzzahl um und verwendet bei ungültiger Eingabe Port 5000. Abschließend startet sie Flask. Als Einstiegspunkt des Webkanals gehört diese Konfiguration in `web_app.py`.

### 2.12.3 Funktion _demo_weather(city)

Die interne Hilfsfunktion stellt eine deterministische Alternative zur externen Wetter-API bereit.

```python
def _demo_weather(city: str) -> str:
    return (
        f"Demo-Wetter für {city}: 21 °C, leicht bewölkt. "
        "Hinweis: Es wurde kein OpenWeatherMap API-Key gefunden."
    )
```

`_demo_weather()` erhält einen bereinigten Stadtnamen und gibt einen festen deutschen Wettertext zurück. Damit bleibt die Bewertung ohne API-Key reproduzierbar und es werden keine realen Zugangsdaten benötigt. Da diese Rückfalllogik zu Wetteranfragen gehört und von beiden Kanälen nutzbar ist, befindet sie sich in `weather_service.py`.

### 2.12.4 Funktion get_weather(city)

`get_weather()` bildet den zentralen Einstiegspunkt für Live- und Demo-Wetteranfragen.

```python
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
```

Die Funktion erhält den Stadtnamen und gibt in jedem Ausführungspfad einen deutschen String zurück. Zunächst prüft sie eine leere Eingabe. Danach lädt sie `OPENWEATHER_API_KEY`; ohne Schlüssel delegiert sie an `_demo_weather()`. Mit Schlüssel sendet sie Stadt, metrische Einheiten und deutsche Spracheinstellung an OpenWeatherMap. HTTP-Fehler und fehlende oder ungültige Antwortfelder werden gemeinsam abgefangen und in eine verständliche Rückfallmeldung übersetzt. Die Funktion bleibt frei von Telegram- und Flask-Objekten und kann deshalb von beiden Kanälen verwendet werden.

### 2.12.5 Funktion create_booking_confirmation(date, time)

Der Buchungsservice validiert die beiden Eingaben und erzeugt eine ausdrücklich fiktive Bestätigung.

```python
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
```

`create_booking_confirmation()` erhält Datum und Uhrzeit als Strings und gibt immer einen deutschen Text zurück. Fehlende Werte, ein Datum außerhalb des Formats `DD.MM.YYYY` oder eine Uhrzeit außerhalb von `HH:MM` führen zu konkreten Hinweisen. Gültige Eingaben erzeugen lediglich eine fiktive Bestätigung; es wird keine reale Buchung gespeichert. Die kanalunabhängige Funktion in `booking_service.py` wird sowohl vom Telegram- als auch vom Webkanal aufgerufen.

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
