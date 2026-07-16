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
├── data/
│   ├── demo_weather_data.json
│   └── appointment_config.json
├── Bilder/
│   ├── DescriptionPic.png
│   ├── ProfilePic.png
│   ├── Screenshot 01_BotConfiguration.png
│   ├── Screenshot 02_test web application.png
│   └── Screenshot 03_test telegram ohne wheathermap key.png
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
| `data/demo_weather_data.json` | Deterministische Demo-Wetterdaten für Tests ohne OpenWeatherMap API-Key |
| `data/appointment_config.json` | Text- und Formatkonfiguration für fiktive Terminbestätigungen |
| `Bilder/` | Bildnachweise zur Konfiguration und visuellen Darstellung des Telegram-Bots |
| `Bilder/DescriptionPic.png` | Bild für den Telegram-Bereich „What can this bot do?“ |
| `Bilder/ProfilePic.png` | Profilbild des konfigurierten Telegram-Bots |
| `Bilder/Screenshot 01_BotConfiguration.png` | Screenshot der BotFather-Konfiguration |
| `Bilder/Screenshot 02_test web application.png` | Nachweis des manuellen Webtests im Demo-Modus |
| `Bilder/Screenshot 03_test telegram ohne wheathermap key.png` | Nachweis des manuellen Telegram-Tests im Demo-Modus |
| `requirements.txt` | Direkte Python-Abhängigkeiten des Projekts |
| `.env.example` | Vorlage der benötigten und optionalen Umgebungsvariablen ohne Secrets |
| `beispiel_dialog.txt` | Beispielabläufe für Telegram und Web |
| `hinweis_zur_abgabe.txt` | Inhalt, Speicherort und Sicherheitsangaben zur ZIP-Abgabe |
| `.gitignore` | Ausschluss lokaler Umgebung, Caches, Secrets und ZIP-Prüfverzeichnis |
| `submission/Angie_Angarita_Soto_Teilprüfung 2.zip` | Finale Datei zur Einreichung |

Die gewählte Struktur trennt Dokumentation, Telegram-Kanallogik, Web-Kanallogik, gemeinsame Geschäftslogik, Frontend-Dateien, Konfigurationsbeispiele, Bildnachweise und Abgabedateien klar voneinander. `telegram_bot.py` enthält ausschließlich die Telegram-spezifische Kanallogik. Der Webkanal verteilt sich auf `web_app.py`, `templates/index.html`, `static/app.js` und `static/style.css`. Die von beiden Kanälen verwendeten fachlichen Funktionen liegen zentral in `weather_service.py` und `booking_service.py`. Die beiden JSON-Dateien trennen kleine Demo- und Konfigurationswerte von der Python-Logik. Dadurch wird doppelter Code vermieden und das Projekt lässt sich leichter verstehen, testen, warten und erweitern.

Weitere Kanäle wie WhatsApp Business, Microsoft Teams oder Slack könnten später als zusätzliche Adapter ergänzt werden, ohne die zentrale Geschäftslogik neu zu schreiben. `Bilder/` dokumentiert die BotFather-Konfiguration und die visuelle Einrichtung des Bots; `submission/` enthält das finale ZIP-Archiv. Git und GitHub dienen der nachvollziehbaren Versionierung und Dokumentation des Entwicklungsprozesses.

## Gitignore und lokale Entwicklungsdateien

Die Regeln in `.gitignore` trennen lokale oder automatisch erzeugte Dateien von den fachlich relevanten Projektbestandteilen:

- `.venv/` wird ausgeschlossen, weil virtuelle Umgebungen lokale Entwicklungsumgebungen sind und nicht versioniert werden sollen.
- `__pycache__/` und `*.pyc` werden ausgeschlossen, da Python diese Cache-Dateien automatisch erzeugt.
- `.env` und `.env.*` werden ausgeschlossen, weil sie reale Telegram-Bot-Tokens, OpenWeatherMap API-Keys oder lokale Konfiguration enthalten können. `.env.example` ist ausdrücklich ausgenommen, da diese Datei die erforderlichen Umgebungsvariablen ohne echte Secrets dokumentiert.
- `submission/check_zip/` wird ausgeschlossen, weil dieses temporäre Verzeichnis nur zur Prüfung des ZIP-Archivs vor der Abgabe dient.
- `.pytest_cache/`, `.DS_Store` und `Thumbs.db` werden ausgeschlossen, da sie lokal durch Testwerkzeuge oder Betriebssysteme entstehen.
- `Bilder/` wird bewusst nicht ausgeschlossen: Die Bilder dokumentieren die Telegram-BotFather-Konfiguration und gehören zur Projektdokumentation auf GitHub.
- `data/` und die JSON-Dateien werden bewusst nicht ausgeschlossen, da sie benötigte Demo-Daten und sichere Konfigurationswerte des Prototyps enthalten.
- Das finale ZIP-Archiv in `submission/` wird nicht allgemein ausgeschlossen, damit es entsprechend dem Arbeitsablauf der vorherigen Teilprüfung versioniert werden kann.

Git protokolliert die Entwicklung nachvollziehbar; GitHub dient als Remote-Repository. Lokale Laufzeitdateien wie `.venv`, `.env`, Python-Caches und `submission/check_zip/` werden ignoriert. Die ZIP-Abgabe enthält nur die freigegebenen Dateitypen und keine Versionsverwaltungsdaten.

# 1. Telegram Bot mit Telegram Bot API

## 1.1 Ziel des Telegram-Bots

Der Telegram-Kanal in `telegram_bot.py` ermöglicht Wetterabfragen und fiktive Terminbuchungen direkt im Messenger. Telegram ist über die Aufgabenanforderung hinaus für einen schnellen akademischen Prototyp geeignet: Die Telegram Bot API ist entwicklungsfreundlich nutzbar, erfordert keine komplexe Unternehmensverifizierung und für diesen Prototyp keine zusätzliche Plattformlizenz. BotFather macht die Einrichtung des Bots und seiner Befehle schnell und transparent.

Durch Polling kann der Bot lokal getestet werden, ohne einen öffentlichen Server oder Webhook bereitzustellen. Telegram ist damit unter begrenzten zeitlichen und technischen Ressourcen ein praktischer Kanal, um eine Multi-Channel-Architektur zu demonstrieren. In einer realen Unternehmensumgebung könnten später weitere Adapter für WhatsApp Business, Microsoft Teams oder Slack ergänzt werden.

## 1.2 Architektur des Telegram-Kanals

**Abbildung 1: Routing und Datenfluss des Telegram-Kanals**

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

Der Routing- und Datenfluss läuft in acht Schritten ab:

1. Die Benutzerin oder der Benutzer sendet in Telegram einen Befehl, beispielsweise `/wetter Berlin` oder `/termin 20.07.2026 14:00`.
2. Telegram leitet den Befehl über die Telegram Bot API an den Bot weiter.
3. `telegram_bot.py` empfängt den Befehl über den konfigurierten Command-Handler.
4. Der Telegram-Handler liest die Befehlsargumente aus.
5. Für Wetteranfragen ruft `telegram_bot.py` die Funktion in `weather_service.py` auf.
6. Für Terminanfragen ruft `telegram_bot.py` die Funktion in `booking_service.py` auf.
7. Der ausgewählte Service gibt einen deutschen Antworttext zurück.
8. `telegram_bot.py` sendet die Antwort über Telegram an die Benutzerin oder den Benutzer zurück.

Die Telegram-Schicht enthält damit ausschließlich kanalspezifische Logik: Sie empfängt Befehle, extrahiert Argumente und sendet Antworten. Wetter- und Buchungslogik werden nicht im Kanaladapter dupliziert, sondern an die gemeinsame Geschäftslogik in `weather_service.py` und `booking_service.py` delegiert. Diese Trennung erleichtert Tests, Wartung und Erweiterungen. Zukünftige Kanäle können dieselben Services wiederverwenden und sich in die Multi-Channel-Architektur einfügen.

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

**Abbildung 2: Telegram BotFather-Konfiguration**

![Telegram Bot Konfiguration](Bilder/Screenshot%2001_BotConfiguration.png)

Abbildung 2 zeigt die konfigurierte BotFather-Übersicht mit Botname, Beschreibung, Befehlen, Bildkonfiguration und verwendeter Telegram Standard Privacy Policy.

**Abbildung 3: Telegram Bot Profilbild**

![Telegram Bot Profilbild](Bilder/ProfilePic.png)

Abbildung 3 zeigt das Profilbild des Bots, das den Wetter- und Termin-Anwendungsfall visuell darstellt.

**Abbildung 4: Telegram Bot Description Picture**

![Telegram Bot Description Picture](Bilder/DescriptionPic.png)

Abbildung 4 zeigt das Description Picture, das im Bereich „What can this bot do?“ angezeigt wird.

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

Die Flask-Webanwendung bietet dieselben zwei Anwendungsfälle wie Telegram über eine leicht bedienbare Browseroberfläche. Dadurch lässt sich der Chatbot auch ohne Telegram-Konto demonstrieren. AJAX ermöglicht dabei die asynchrone Kommunikation zwischen Browser und Flask-Backend: Wetter- und Terminanfragen können abgesendet und beantwortet werden, ohne die gesamte Seite neu zu laden. Damit wird die entsprechende Anforderung der Teilprüfung unmittelbar erfüllt.

Für einen schlanken Prototyp ist AJAX mit der integrierten Fetch API besonders geeignet, weil kein komplexes Frontend-Framework erforderlich ist. Die Oberfläche bleibt bewusst einfach, demonstriert aber das Grundprinzip moderner interaktiver Webanwendungen. Gleichzeitig nutzt sie dieselben Backend-Services wie Telegram, sodass beide Kanäle konsistente fachliche Antworten liefern.

## 2.2 Architektur der Webanwendung

**Abbildung 5: Routing und Datenfluss der Flask-Webanwendung**

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

Der Routing- und Datenfluss läuft in acht Schritten ab:

1. Die Benutzerin oder der Benutzer gibt Daten in ein Formular im Browser ein.
2. `static/app.js` fängt das Absenden des Formulars ab.
3. `fetch` sendet eine JSON-Anfrage an den passenden Flask-Endpunkt.
4. `web_app.py` empfängt die JSON-Anfrage.
5. `web_app.py` leitet die Eingaben an `weather_service.py` oder `booking_service.py` weiter.
6. Der aufgerufene Service gibt einen deutschen Antworttext zurück.
7. Flask verpackt diesen Text als JSON-Antwort.
8. JavaScript schreibt die Antwort in den zugehörigen Ergebnisbereich der Seite.

Die Web-Schicht enthält ausschließlich kanalspezifische Logik für Browser und Flask. Im Browser stellen `templates/index.html` und `static/app.js` Formulare, Ereignisverarbeitung und Ergebnisbereiche bereit. AJAX mit `fetch` verhindert einen vollständigen Seitenreload, während `web_app.py` die Flask-Routen sowie die Verarbeitung von JSON-Anfragen und JSON-Antworten übernimmt. Wetter- und Buchungslogik werden wie beim Telegram-Kanal an `weather_service.py` und `booking_service.py` delegiert. Die parallele Trennung von Kanallogik und gemeinsamer Geschäftslogik bildet die Grundlage der sauberen Multi-Channel-Architektur.

## 2.3 Flask-Routen

Flask-Routen sind URL-Endpunkte, die eine Kombination aus URL und HTTP-Methode mit einer Python-Funktion verbinden. Die Webanwendung benötigt eine Route für die HTML-Seite, einen API-Endpunkt für Wetteranfragen und einen API-Endpunkt für Terminanfragen. `web_app.py` implementiert deshalb genau diese drei Zugänge.

Die beiden API-Endpunkte tauschen JSON mit dem Browser aus. JSON ist ein leichtgewichtiges, strukturiertes Datenformat und kann Felder wie `city`, `date`, `time` und `message` eindeutig darstellen. In diesem Projekt wird JSON auf zwei Ebenen eingesetzt:

1. als Anfrage- und Antwortformat zwischen `static/app.js` und Flask;
2. als lokales Daten- und Konfigurationsformat in `data/demo_weather_data.json` und `data/appointment_config.json`.

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

Der Datenfluss der Wetteranfrage ist auf klar abgegrenzte Komponenten verteilt:

1. In `templates/index.html` gibt die Benutzerin oder der Benutzer eine Stadt in das Eingabefeld mit der ID `city` ein.
2. `static/app.js` liest den Wert über diese ID aus und erzeugt beispielsweise `{ "city": "Berlin" }`.
3. JavaScript sendet das JSON-Objekt per POST an `/api/weather`.
4. `weather_api()` in `web_app.py` empfängt die Anfrage und liest das Feld `city`.
5. Der Flask-Endpunkt ruft `get_weather(city)` aus `weather_service.py` auf.
6. Der Wetterservice verwendet mit API-Key OpenWeatherMap; ohne API-Key liest er die Demo-Daten aus `data/demo_weather_data.json`.
7. `web_app.py` verpackt den deutschen Antworttext als JSON.
8. `static/app.js` schreibt `message` in den Ergebnisbereich `weather-result`.

## 2.6 Terminformular

Auch die fiktive Terminbuchung folgt einem nachvollziehbaren Datenfluss:

1. In `templates/index.html` werden Datum und Uhrzeit in die Felder mit den IDs `date` und `time` eingegeben.
2. `static/app.js` liest beide Werte und bildet ein JSON-Objekt mit `date` und `time`.
3. JavaScript sendet dieses Objekt per POST an `/api/appointment`.
4. `appointment_api()` in `web_app.py` empfängt die Anfrage.
5. Der Endpunkt ruft `create_booking_confirmation(date, time)` aus `booking_service.py` auf.
6. Der Buchungsservice validiert beide Werte mit regulären Ausdrücken und liest Text- und Formatwerte aus `data/appointment_config.json`.
7. `web_app.py` gibt die fiktive Bestätigung oder Fehlermeldung als JSON zurück.
8. `static/app.js` schreibt `message` in den Ergebnisbereich `appointment-result`.

Es wird dabei kein realer Termin erzeugt oder gespeichert.

## 2.7 Antwort ohne Neuladen der Seite

`event.preventDefault()` verhindert das reguläre Neuladen beim Absenden. `static/app.js` sendet mit AJAX beziehungsweise `fetch` asynchrone POST-Anfragen als JSON an den passenden Flask-Endpunkt. Flask gibt eine JSON-Antwort zurück, deren Meldung JavaScript in den jeweiligen Ergebnisbereich schreibt. Die Seite wird dabei nicht neu geladen; damit ist die entsprechende Anforderung der Teilprüfung unmittelbar erfüllt.

`aria-live="polite"` sorgt zusätzlich dafür, dass unterstützende Technologien aktualisierte Antworten ankündigen können. Die Weboberfläche bleibt bewusst einfach, weil der Schwerpunkt auf der Multi-Channel-Architektur und der asynchronen Interaktion liegt.

## 2.8 Gemeinsame Nutzung der Services

Der Webkanal importiert dieselben Funktionen `get_weather()` und `create_booking_confirmation()` wie der Telegram-Bot. Damit gelten für beide Kanäle dieselben Validierungsregeln, Demo-Daten und Antworttexte. Diese gemeinsame Nutzung vermeidet doppelte Implementierungen und erleichtert Wartung und Tests. Die Services kennen weder Flask- noch Telegram-Objekte und bleiben deshalb vollständig kanalunabhängig.

## 2.9 Wetterservice

### 2.9.1 Funktion get_weather(city)

`get_weather(city: str) -> str` ist die zentrale Funktion für Wetteranfragen. Sie erhält einen Stadtnamen, bereinigt die Eingabe und gibt stets einen deutschen Antworttext zurück. Da sie weder Telegram- noch Flask-Objekte verwendet, ist sie kanalunabhängig und kann von beiden Kanälen aufgerufen werden.

Ein `OPENWEATHER_API_KEY` wird nur für reale, produktionsähnliche Wetterdaten von OpenWeatherMap benötigt und ausschließlich aus der gleichnamigen Umgebungsvariable gelesen. Der Schlüssel wird nicht in Quellcode, README, Screenshots, GitHub oder ZIP gespeichert. Fehlt er, verwendet die Funktion stattdessen `data/demo_weather_data.json`. Dadurch bleibt die Anwendung ohne externe Zugangsdaten vollständig testbar.

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

Fehlt `OPENWEATHER_API_KEY`, liest die Funktion deterministische Demo-Daten aus `data/demo_weather_data.json`, beispielsweise `Demo-Wetter für Berlin: 21 °C, leicht bewölkt.` Für nicht hinterlegte Städte wird der Eintrag `default` verwendet. Dieser Modus macht das Projekt für prüfende Personen ohne externe Zugangsdaten testbar und stellt die Reproduzierbarkeit der Abgabe sicher. Ist die JSON-Datei nicht lesbar, greifen zusätzlich sichere Standardwerte im Python-Service.

### 2.9.4 Fehlerbehandlung

Die zentrale Fehlerbehandlung ist direkt in `get_weather()` enthalten:

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
        if response.status_code == 404:
            return (
                f"Die Stadt „{normalized_city}“ wurde nicht gefunden. Bitte prüfen Sie "
                "die Schreibweise oder geben Sie eine gültige Stadt ein."
            )
        if response.status_code == 401:
            return (
                "Der Wetterdienst konnte nicht authentifiziert werden. Bitte prüfen Sie "
                "die lokal konfigurierte OpenWeatherMap API-Key."
            )
        if response.status_code == 429:
            return (
                "Das Limit des Wetterdienstes wurde erreicht. Bitte versuchen Sie es "
                "später erneut."
            )
        response.raise_for_status()
        data = response.json()
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        resolved_city = data.get("name") or normalized_city
        if (
            isinstance(temperature, bool)
            or not isinstance(temperature, (int, float))
            or not math.isfinite(temperature)
            or not isinstance(description, str)
            or not description.strip()
            or not isinstance(resolved_city, str)
            or not resolved_city.strip()
        ):
            raise ValueError
        return f"Wetter für {resolved_city}: {temperature:.1f} °C, {description}."
    except (requests.RequestException, KeyError, IndexError, TypeError, ValueError):
        return (
            f"Die Wetterdaten für {normalized_city} konnten derzeit nicht "
            "abgerufen werden. Bitte versuchen Sie es später erneut."
        )
```

Die Anwendung unterscheidet die wichtigsten Fehlerfälle von OpenWeatherMap gezielt. Eine leere Stadt führt sofort zu einem hilfreichen Eingabehinweis. Ein fehlender API-Key ist kein Fehler, sondern aktiviert bewusst den JSON-basierten Demo-Modus. Eine ungültige oder nicht gefundene Stadt (`HTTP 404`) wird als Problem der Benutzereingabe behandelt und mit einem Hinweis auf Schreibweise und gültige Städtenamen beantwortet. Bei einem ungültigen API-Key (`HTTP 401`) oder einem erreichten Anfragelimit (`HTTP 429`) erscheinen sichere, verständliche Meldungen, ohne den API-Key oder technische Details offenzulegen. Andere HTTP- und Netzwerkfehler, Timeouts, eine unerwartete JSON-Struktur sowie fehlende oder ungültige Werte führen zur allgemeinen Rückfallmeldung. Technische Exceptions werden nicht direkt angezeigt. Das verbessert die Benutzererfahrung und macht den Prototyp robuster.

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

## 2.12 Konfiguration durch JSON-Dateien

In dieser Lösung wird JSON auf zwei Ebenen verwendet: Einerseits als Austauschformat zwischen Browser und Flask-Backend, andererseits als lokale Konfigurations- und Datengrundlage für den Demo-Modus. Dadurch wird deutlich zwischen Kommunikation, Konfiguration und Programmlogik unterschieden.

1. `static/app.js` und die Flask-Endpunkte in `web_app.py` verwenden JSON für Anfragen und Antworten.
2. Die Dateien im Ordner `data/` verwenden JSON als lokale Daten- und Konfigurationsgrundlage.

Die lokalen JSON-Dateien trennen kleine, veränderbare Daten- und Konfigurationswerte von der Python-Logik. Dadurch wird der Prototyp leichter verständlich, wartbar und erweiterbar. Zugleich bleibt der Demo-Modus reproduzierbar, weil die Anwendung ohne reale API-Keys mit festgelegten Daten geprüft werden kann.

**Tabelle 4: JSON-Dateien und Zweck im Projekt**

| Datei | Zweck |
|---|---|
| `data/demo_weather_data.json` | Enthält deterministische Demo-Wetterdaten für Tests ohne OpenWeatherMap API-Key. |
| `data/appointment_config.json` | Enthält einfache Text- und Konfigurationswerte für fiktive Terminbestätigungen. |

### 2.12.1 `data/demo_weather_data.json`

Die Datei enthält deterministische Demo-Wetterdaten für Berlin, Hamburg, München und Köln sowie einen `default`-Eintrag. `weather_service.py` liest diese Daten, wenn kein `OPENWEATHER_API_KEY` verfügbar ist. Dadurch bleibt der Prototyp ohne externe Zugangsdaten testbar. Die Demo-Werte sind von der Python-Logik getrennt und können angepasst werden, ohne `weather_service.py` zu verändern.

Der folgende Auszug entspricht dem aktuellen Inhalt der Datei:

```json
{
  "Berlin": {
    "temperature": 21,
    "description": "leicht bewölkt"
  },
  "Hamburg": {
    "temperature": 18,
    "description": "windig"
  },
  "München": {
    "temperature": 23,
    "description": "sonnig"
  },
  "Köln": {
    "temperature": 20,
    "description": "wechselhaft"
  },
  "default": {
    "temperature": 21,
    "description": "leicht bewölkt"
  }
}
```

Die Stadtnamen bilden die Schlüssel des JSON-Objekts. Jeder Stadteintrag enthält mit `temperature` und `description` die Werte für Temperatur und Beschreibung. Ist eine Stadt nicht explizit vorhanden, kann der Eintrag `default` als Rückfallwert verwendet werden. `weather_service.py` liest diese Struktur und erzeugt daraus einen deutschen Demo-Wettertext. Da dieselbe Stadt stets dieselben Werte liefert, sind Tests reproduzierbar.

**Workflow der Demo-Wetterdaten:**

```text
No OPENWEATHER_API_KEY
    ↓
weather_service.py
    ↓
data/demo_weather_data.json
    ↓
Demo-Wetterantwort
```

### 2.12.2 `data/appointment_config.json`

Die Datei stellt einfache Konfigurationswerte für fiktive Terminbestätigungen bereit und wird von `booking_service.py` gelesen. Damit bleiben veränderbare Textwerte von der Validierungslogik getrennt. Es wird kein realer Termin gespeichert und es werden keine personenbezogenen Daten persistiert; die Buchung bleibt ausdrücklich fiktiv.

Der folgende Auszug entspricht dem aktuellen Inhalt der Datei:

```json
{
  "confirmation_prefix": "Ihr Termin wurde fiktiv",
  "confirmation_suffix": "bestätigt.",
  "date_format_hint": "DD.MM.YYYY",
  "time_format_hint": "HH:MM",
  "example_date": "20.07.2026",
  "example_time": "14:00"
}
```

Die Datei enthält wiederverwendbare Textfragmente, Formatangaben und Beispielwerte. `booking_service.py` verwendet diese Werte für konsistente deutsche Meldungen. Die regulären Ausdrücke zur Prüfung von Datum und Uhrzeit verbleiben dagegen in Python. Diese Aufteilung trennt konfigurierbare Texte von fachlicher Validierung und verbessert die Wartbarkeit.

**Workflow der Terminkonfiguration:**

```text
Date + time from user
    ↓
booking_service.py
    ↓
data/appointment_config.json
    ↓
Fiktive Terminbestätigung
```

### 2.12.3 Begründung für die Konfiguration durch JSON-Dateien

JSON-Dateien machen kleine Daten- und Konfigurationswerte sichtbar, gut lesbar und einfach änderbar. Das sprachunabhängige Format verhindert, dass statische Werte mit dem Python-Kontrollfluss vermischt werden, und unterstützt eine klare Trennung von Code, Daten und Konfiguration. Dadurch wird der Prototyp wartbarer und leichter erweiterbar. Die deterministischen Demo-Daten verbessern zusätzlich die Reproduzierbarkeit von Tests.

Für diese Teilprüfung ist JSON ausreichend, weil die Anwendung ein kleiner Prototyp ist und keine realen Benutzerdaten speichert. In einem größeren Produktivsystem könnten die Dateien später durch eine Datenbank, ein CRM, ein Content-Management-System, eine API oder eine Wissensbasis ersetzt werden.

## 2.13 Erklärung des Codes für die Webanwendung und die gemeinsamen Services

Die Routen `index()`, `weather_api()` und `appointment_api()` sind bereits mit ihrem Originalcode in Abschnitt 2.3 erläutert. Dieser Abschnitt konzentriert sich deshalb auf Serverkonfiguration und gemeinsame Services. `web_app.py` enthält Webkanal-Logik, während `weather_service.py` und `booking_service.py` kanalunabhängige Geschäftslogik bereitstellen.

### 2.13.1 Funktion _is_truthy()

Die Hilfsfunktion interpretiert textbasierte Umgebungsvariablen für `FLASK_DEBUG`.

```python
def _is_truthy(value: str) -> bool:
    return value.strip().lower() in {"1", "true", "yes", "on"}
```

Als Eingabe erhält `_is_truthy()` einen String und gibt einen booleschen Wert zurück. Durch Normalisierung von Leerraum und Groß-/Kleinschreibung werden übliche Wahrheitswerte zuverlässig erkannt. Die Funktion gehört in `web_app.py`, weil sie ausschließlich die lokale Flask-Konfiguration unterstützt.

### 2.13.2 Funktion main() in web_app.py

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

### 2.13.3 Funktion _demo_weather(city)

Die interne Hilfsfunktion stellt eine deterministische Alternative zur externen Wetter-API bereit.

```python
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
```

`_demo_weather()` erhält einen bereinigten Stadtnamen, liest `data/demo_weather_data.json` und sucht den Stadteintrag unabhängig von Groß- und Kleinschreibung. Für unbekannte Städte wird `default` verwendet. Kann die Datei nicht gelesen oder ausgewertet werden, liefern sichere Python-Standardwerte weiterhin eine deutsche Antwort. Damit bleibt die Bewertung ohne API-Key reproduzierbar. Da diese Rückfalllogik von beiden Kanälen nutzbar ist, befindet sie sich in `weather_service.py`.

### 2.13.4 Funktion get_weather(city)

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
        if response.status_code == 404:
            return (
                f"Die Stadt „{normalized_city}“ wurde nicht gefunden. Bitte prüfen Sie "
                "die Schreibweise oder geben Sie eine gültige Stadt ein."
            )
        if response.status_code == 401:
            return (
                "Der Wetterdienst konnte nicht authentifiziert werden. Bitte prüfen Sie "
                "die lokal konfigurierte OpenWeatherMap API-Key."
            )
        if response.status_code == 429:
            return (
                "Das Limit des Wetterdienstes wurde erreicht. Bitte versuchen Sie es "
                "später erneut."
            )
        response.raise_for_status()
        data = response.json()
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        resolved_city = data.get("name") or normalized_city
        if (
            isinstance(temperature, bool)
            or not isinstance(temperature, (int, float))
            or not math.isfinite(temperature)
            or not isinstance(description, str)
            or not description.strip()
            or not isinstance(resolved_city, str)
            or not resolved_city.strip()
        ):
            raise ValueError
        return f"Wetter für {resolved_city}: {temperature:.1f} °C, {description}."
    except (requests.RequestException, KeyError, IndexError, TypeError, ValueError):
        return (
            f"Die Wetterdaten für {normalized_city} konnten derzeit nicht "
            "abgerufen werden. Bitte versuchen Sie es später erneut."
        )
```

Die Funktion erhält den Stadtnamen und gibt in jedem Ausführungspfad einen deutschen String zurück. Zunächst prüft sie eine leere Eingabe. Danach lädt sie `OPENWEATHER_API_KEY`; ohne Schlüssel delegiert sie an `_demo_weather()`. Mit Schlüssel sendet sie Stadt, metrische Einheiten und deutsche Spracheinstellung an OpenWeatherMap. Die Statuscodes `404`, `401` und `429` werden vor der Auswertung der JSON-Antwort gezielt behandelt. Andere HTTP- und Netzwerkfehler sowie fehlende oder ungültige Antwortfelder werden abgefangen und in eine verständliche Rückfallmeldung übersetzt. Die Funktion bleibt frei von Telegram- und Flask-Objekten und kann deshalb von beiden Kanälen verwendet werden.

### 2.13.5 Funktion create_booking_confirmation(date, time)

Der Buchungsservice validiert die beiden Eingaben und erzeugt eine ausdrücklich fiktive Bestätigung.

```python
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
```

`create_booking_confirmation()` lädt zunächst sichere Text- und Formatwerte aus `data/appointment_config.json`; bei einem Dateifehler greift `SAFE_CONFIG`. Die Funktion erhält Datum und Uhrzeit als Strings und gibt immer einen deutschen Text zurück. Fehlende Werte, ein Datum außerhalb des Formats `DD.MM.YYYY` oder eine Uhrzeit außerhalb von `HH:MM` führen zu konkreten Hinweisen. Gültige Eingaben erzeugen lediglich eine fiktive Bestätigung; es wird keine reale Buchung gespeichert. Die kanalunabhängige Funktion wird sowohl vom Telegram- als auch vom Webkanal aufgerufen.

# Ausführung

## Installation

Vorausgesetzt werden Python 3.10 oder neuer, `pip` und die Möglichkeit, eine virtuelle Python-Umgebung anzulegen. Die benötigten Bibliotheken werden aus `requirements.txt` installiert. Unter Windows PowerShell erfolgt die vollständige Vorbereitung mit:

```powershell
cd C:\dev\ai-development-teilpruefung-2
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Virtuelle Umgebung

Die virtuelle Umgebung `.venv` isoliert die Projektabhängigkeiten von der globalen Python-Installation. Sie wird lokal erstellt, vor der Installation aktiviert und durch `.gitignore` von der Versionierung ausgeschlossen.

## Abhängigkeiten installieren

`requirements.txt` installiert Flask für den Webkanal, `requests` für OpenWeatherMap, `python-dotenv` für lokale Umgebungsvariablen und `python-telegram-bot` für den Telegram-Kanal.

## Umgebungsvariablen

`.env.example` dokumentiert die erwarteten Variablen ohne echte Secrets. Für lokale Tests kann eine eigene, durch `.gitignore` ausgeschlossene `.env` angelegt werden. Der Web-Demo-Modus benötigt keinen API-Key, weil `data/demo_weather_data.json` verwendet wird. Für Telegram-Tests ist `TELEGRAM_BOT_TOKEN` lokal erforderlich; für reale OpenWeatherMap-Daten kann `OPENWEATHER_API_KEY` optional konfiguriert werden. `FLASK_HOST`, `FLASK_PORT` und `FLASK_DEBUG` steuern den lokalen Webserver. Die reale `.env` wird weder in GitHub noch in die ZIP-Abgabe aufgenommen.

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

## Tests ohne API-Key

Die Anwendung wurde bewusst ohne aktiven OpenWeatherMap API-Key manuell getestet. Ziel dieser Tests war es, den Demo-Modus und das Fallback-Verhalten unabhängig von externen Wetterdiensten zu prüfen. In diesem Modus liest `weather_service.py` die deterministischen Werte aus `data/demo_weather_data.json`; eine Anfrage an die externe Wetter-API ist nicht erforderlich. Da Telegram und die Flask-Webanwendung denselben Wetterservice aufrufen, gilt dieses Verhalten für beide Kanäle. Damit bleibt das Projekt für prüfende Personen ohne externe Zugangsdaten reproduzierbar.

Folgende manuelle Tests wurden durchgeführt:

- Webanwendung unter `http://127.0.0.1:5000` geladen
- Wetterformular mit `berlin` getestet
- Terminformular mit `30.07.2026` und `13:00` getestet
- Telegram mit `/start` getestet
- Telegram mit `/hilfe` getestet
- Telegram mit `/wetter Berlin` getestet
- Telegram mit `/wetter Paris` getestet
- Telegram mit `/termin 20.07.2026 14:00` getestet
- Telegram mit `/termin 21.07.2026 15:00` getestet

Die Webanwendung zeigte deterministische Demo-Wetterdaten und eine fiktive Terminbestätigung an. Der Telegram-Bot lieferte ebenfalls Demo-Wetterdaten sowie fiktive Terminbestätigungen. Auch die nicht explizit hinterlegte Stadt Paris wurde über den definierten Standardwert beantwortet. Weder Anwendung noch Bot stürzten ab; stattdessen erschienen verständliche deutsche Meldungen. Damit ist das Fallback-Verhalten nachgewiesen: Das System bleibt ohne API-Key im Demo-Modus nutzbar und testbar.

### Manuelle Testergebnisse ohne OpenWeatherMap API-Key

**Abbildung 6: Test der Flask-Webanwendung ohne OpenWeatherMap API-Key**

![Test der Flask-Webanwendung](Bilder/Screenshot%2002_test%20web%20application.png)

Diese Abbildung zeigt die getestete Flask-Webanwendung mit Wetteranfrage im Demo-Modus und fiktiver Terminbuchung. Die Weboberfläche wurde über `http://127.0.0.1:5000` aufgerufen. Die Antwort wird ohne Neuladen der Seite angezeigt.

**Abbildung 7: Test des Telegram-Bots ohne OpenWeatherMap API-Key**

![Test des Telegram-Bots](Bilder/Screenshot%2003_test%20telegram%20ohne%20wheathermap%20key.png)

Diese Abbildung zeigt den erfolgreichen Test des Telegram-Bots im Polling-Modus. Die Befehle `/start`, `/hilfe`, `/wetter` und `/termin` wurden manuell geprüft. Da kein aktiver OpenWeatherMap API-Key verwendet wurde, antwortet der Bot mit Demo-Wetterdaten.

## Tests mit API-Key

Nach der Aktivierung des OpenWeatherMap API-Keys wurde die Anwendung erneut manuell getestet. Der API-Key war ausschließlich lokal in `.env` gespeichert und ist weder in dieser README, im Quellcode, in den Screenshots, im GitHub-Repository noch in der ZIP-Abgabe enthalten. `weather_service.py` liest ihn über die Umgebungsvariable `OPENWEATHER_API_KEY`. Mit aktivem API-Key liefern gültige Städtenamen reale Wetterdaten von OpenWeatherMap. Ungültige Städtenamen führen zu einer spezifischen, benutzerfreundlichen Meldung. Der Telegram-Bot und die Flask-Webanwendung verwenden dafür dieselbe Wetterlogik aus `weather_service.py`.

Folgende manuelle Tests wurden durchgeführt:

- `get_weather("Berlin")` im Terminal getestet
- `get_weather("Paris")` im Terminal getestet
- `get_weather("xyzstadt123")` im Terminal getestet
- `create_booking_confirmation("20.07.2026", "14:00")` im Terminal getestet
- `create_booking_confirmation("2026-07-20", "14:00")` im Terminal getestet
- Flask-Webanwendung mit `Berlin` getestet
- Flask-Webanwendung mit `London` getestet
- Flask-Webanwendung mit ungültiger Stadtangabe getestet
- Flask-Webanwendung mit gültigen fiktiven Termindaten getestet
- Flask-Webanwendung mit ungültigem Datumsformat getestet
- Telegram-Bot mit `/wetter Berlin` getestet
- Telegram-Bot mit `/wetter Paris` getestet
- Telegram-Bot mit ungültiger Stadtangabe getestet
- Telegram-Bot mit gültigem `/termin 20.07.2026 14:00` getestet
- Telegram-Bot mit ungültigen Datumsformaten getestet

Gültige Städte lieferten reale Wetterdaten, beispielsweise `Wetter für Berlin: 24.0 °C, Klarer Himmel.` Für die ungültige Stadt wurde die spezifische Meldung `Die Stadt „xyzstadt123“ wurde nicht gefunden. Bitte prüfen Sie die Schreibweise oder geben Sie eine gültige Stadt ein.` ausgegeben. Dieser Test validiert die `HTTP 404`-Behandlung für ungültige Stadtnamen. Gültige Termindaten führten zu einer fiktiven Buchungsbestätigung; bei einem ungültigen Datumsformat erschien `Bitte verwenden Sie für das Datum das Format DD.MM.YYYY.` Die Anwendung stürzte nicht ab, und alle Meldungen blieben für Benutzerinnen und Benutzer verständlich. Dasselbe Verhalten war in den Terminaltests, in der Flask-Webanwendung und im Telegram-Bot verfügbar.

### Manuelle Testergebnisse mit OpenWeatherMap API-Key

**Abbildung 8: Terminaltests mit aktivem OpenWeatherMap API-Key**

![Terminaltests mit OpenWeatherMap API-Key](Bilder/Screenshot%2004_test%20terminal%20mit%20wheathermap%20key.png)

Diese Abbildung zeigt die erfolgreichen Terminaltests mit aktivem OpenWeatherMap API-Key. Es wurden gültige Städte, eine ungültige Stadt, eine gültige fiktive Terminbuchung und ein ungültiges Datumsformat geprüft.

**Abbildung 9: Flask-Webanwendung mit realen Wetterdaten für Berlin**

![Flask-Webanwendung mit Wetterdaten Berlin](Bilder/Screenshot%2005_test%20web%20mit%20wheathermap%20key1.png)

Diese Abbildung zeigt die Flask-Webanwendung mit aktiver OpenWeatherMap-Anbindung. Für Berlin wird eine reale Wetterantwort angezeigt.

**Abbildung 10: Flask-Webanwendung mit realen Wetterdaten für London**

![Flask-Webanwendung mit Wetterdaten London](Bilder/Screenshot%2006_test%20web%20mit%20wheathermap%20key2.png)

Diese Abbildung zeigt einen weiteren Test der Flask-Webanwendung mit einer anderen gültigen Stadt. Dadurch wurde geprüft, dass die API-Anbindung nicht nur für eine einzelne Stadt funktioniert.

**Abbildung 11: Flask-Webanwendung mit Fehlerbehandlung bei ungültiger Stadt und ungültigem Datum**

![Flask-Webanwendung Fehlerbehandlung](Bilder/Screenshot%2007_test%20web%20mit%20wheathermap%20key3.png)

Diese Abbildung zeigt die Fehlerbehandlung der Webanwendung. Eine ungültige Stadt erzeugt eine spezifische Rückmeldung, und ein ungültiges Datumsformat erzeugt eine klare Validierungsmeldung.

**Abbildung 12: Telegram-Bot mit aktivem OpenWeatherMap API-Key**

![Telegram-Bot mit OpenWeatherMap API-Key](Bilder/Screenshot%2008_test%20telegram%20mit%20wheathermap%20key.png)

Diese Abbildung zeigt den Telegram-Bot im Polling-Modus mit aktivem OpenWeatherMap API-Key. Wetteranfragen für gültige Städte, ungültige Stadtangaben und Terminbuchungen wurden manuell geprüft.

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
data/demo_weather_data.json
data/appointment_config.json
Bilder/DescriptionPic.png
Bilder/ProfilePic.png
Bilder/Screenshot 01_BotConfiguration.png
Bilder/Screenshot 02_test web application.png
Bilder/Screenshot 03_test telegram ohne wheathermap key.png
requirements.txt
.env.example
beispiel_dialog.txt
hinweis_zur_abgabe.txt
```

`README.md` enthält die Hauptlösung. Die beiden Dateien unter `data/` enthalten ausschließlich Demo-Wetterdaten und einfache Konfigurationswerte für den Prototyp, jedoch keine Secrets. `.env.example` ist als Konfigurationsvorlage enthalten; eine reale `.env` wird nicht aufgenommen. Die Abgabe enthält keine echten API-Schlüssel, Tokens oder sonstigen Secrets. Der Ordner `Bilder/` mit den fünf PNG-Dateien ist Bestandteil der ZIP, weil er BotFather-Konfiguration, Profilbild, Description Picture und die manuellen Demo-Tests beider Kanäle dokumentiert. Ergänzende Informationen stehen in `hinweis_zur_abgabe.txt`.

# Reflexion und Fazit

Das Projekt demonstriert eine übersichtliche Multi-Channel-Chatbot-Architektur. Die Telegram Bot API bildet den ersten Kanal, während Flask und AJAX eine asynchron bedienbare Weboberfläche als zweiten Kanal bereitstellen. Beide Kanäle verwenden dieselbe Geschäftslogik für Wetter und Termine. Diese Trennung verbessert Wartbarkeit, Konsistenz und Testbarkeit.

Der JSON-basierte Demo-Modus stellt die Reproduzierbarkeit ohne realen OpenWeatherMap API-Key sicher. Die Lösung kann durch zusätzliche Kanaladapter für WhatsApp Business, Microsoft Teams oder Slack erweitert werden. Neue Anwendungsfälle ließen sich durch weitere Services oder Routing-Logik ergänzen, ohne die bestehenden Kanäle grundlegend umzubauen. Der aktuelle Prototyp konzentriert sich bewusst auf ein klares, nachvollziehbares Minimum Viable Product.

Die JSON-Dateien verdeutlichen, warum konfigurierbare Software leichter wartbar ist: Demo-Wetterwerte und Texte für Terminbestätigungen lassen sich ändern, ohne die zentrale Python-Logik anzupassen. Diese Trennung unterstützt Wartung, Tests und spätere Erweiterungen. In größeren AI- oder Chatbot-Systemen gewinnt Konfigurationsmanagement zusätzlich an Bedeutung, weil sich beispielsweise Prompts, Routing-Regeln, API-Einstellungen, Rückfalltexte, Testdaten oder Wissensreferenzen im Laufe der Zeit ändern. JSON zeigt in diesem Prototyp auf einfache Weise, wie Anwendungsverhalten konfigurierbar bleibt, statt vollständig hartcodiert zu werden—ein wichtiges Prinzip für wartbare AI-Anwendungen und Multi-Channel-Systeme.

Als nächster Qualitätsschritt könnten automatisierte Tests über eigene Skripte oder Testfunktionen ergänzt werden. Besonders `get_weather()` und `create_booking_confirmation()` eignen sich dafür, weil sie kanalunabhängig sind. Flask-Endpunkte können mit einem Test-Client oder externen Testskripten geprüft werden; Telegram-Befehle lassen sich über isolierte Handler und Mock-Objekte testen.

Für einen Produktivbetrieb wären außerdem fortlaufendes Monitoring und Wartung erforderlich. Sinnvolle Messpunkte wären strukturierte Fehlerprotokolle, fehlgeschlagene API-Aufrufe, Antwortzeiten, Nutzungsmuster und ungültige Benutzereingaben. Diese Beobachtbarkeit würde helfen, Zuverlässigkeit und Reaktionsfähigkeit langfristig zu sichern. Zusätzlich wären robustere fachliche Datumsvalidierung, Authentifizierung, Rate Limiting und professionelles Secret-Management nötig. Für den akademischen Prototyp wird die Telegram Standard Privacy Policy verwendet; eine separate Datenschutzdatei wird bewusst nicht parallel gepflegt.
