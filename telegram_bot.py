# Telegram-Adapter für Befehle, Argumente und Antworten des Chatbots.
# Er verarbeitet Telegram-Befehle und delegiert Wetter- und Buchungslogik an
# gemeinsame Services, damit beide Kanäle dieselben fachlichen Regeln nutzen.

import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from booking_service import create_booking_confirmation
from weather_service import get_weather


# Begrüßt Benutzerinnen und Benutzer und nennt die wichtigsten Befehle.
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    del context  # Der Kontext wird für diesen Befehl nicht benötigt.
    if update.message:
        await update.message.reply_text(
            "Willkommen beim Multi-Channel-Chatbot!\n"
            "Mit /wetter [Stadt] erhalten Sie Wetterinformationen.\n"
            "Mit /termin [Datum] [Zeit] buchen Sie einen fiktiven Termin.\n"
            "Weitere Informationen: /hilfe"
        )


# Zeigt die Syntax der unterstützten Befehle mit Beispielen an.
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


# Liest die Stadt aus den Befehlsargumenten und ruft den Wetterservice auf.
async def weather_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    city = " ".join(context.args).strip()
    response = get_weather(city)
    if update.message:
        await update.message.reply_text(response)


# Liest Datum und Uhrzeit und ruft den gemeinsamen Buchungsservice auf.
async def appointment_command(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    date = context.args[0] if len(context.args) >= 1 else ""
    time = context.args[1] if len(context.args) >= 2 else ""
    response = create_booking_confirmation(date, time)
    if update.message:
        await update.message.reply_text(response)


# Lädt lokale Umgebungsvariablen, prüft das Telegram-Token und startet den Bot.
# Das Token ist ein Secret und darf nicht in Code, README oder GitHub stehen.
# Polling vereinfacht den lokalen Prototyp, da kein öffentlicher Webhook nötig ist.
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


if __name__ == "__main__":
    main()
