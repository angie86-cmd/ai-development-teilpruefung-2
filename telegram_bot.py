"""Telegram-Kanal des Multi-Channel-Chatbots."""

import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from booking_service import create_booking_confirmation
from weather_service import get_weather


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Begrüßt Benutzerinnen und Benutzer und nennt die wichtigsten Befehle."""
    del context  # Der Kontext wird für diesen Befehl nicht benötigt.
    if update.message:
        await update.message.reply_text(
            "Willkommen beim Multi-Channel-Chatbot!\n"
            "Mit /wetter [Stadt] erhalten Sie Wetterinformationen.\n"
            "Mit /termin [Datum] [Zeit] buchen Sie einen fiktiven Termin.\n"
            "Weitere Informationen: /hilfe"
        )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Zeigt die Syntax der unterstützten Befehle an."""
    del context
    if update.message:
        await update.message.reply_text(
            "Verfügbare Befehle:\n"
            "/start – Begrüßung anzeigen\n"
            "/hilfe – Hilfe anzeigen\n"
            "/wetter [Stadt] – z. B. /wetter Berlin\n"
            "/termin [DD.MM.YYYY] [HH:MM] – z. B. /termin 20.07.2026 14:00"
        )


async def weather_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Liefert Wetterinformationen für die als Argument übergebene Stadt."""
    city = " ".join(context.args).strip()
    response = get_weather(city)
    if update.message:
        await update.message.reply_text(response)


async def appointment_command(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Erstellt anhand von Datum und Uhrzeit eine fiktive Terminbestätigung."""
    date = context.args[0] if len(context.args) >= 1 else ""
    time = context.args[1] if len(context.args) >= 2 else ""
    response = create_booking_confirmation(date, time)
    if update.message:
        await update.message.reply_text(response)


def main() -> None:
    """Konfiguriert den Bot und startet ihn im Polling-Modus."""
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
