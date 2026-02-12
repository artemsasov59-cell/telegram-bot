from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import os

TOKEN = os.environ.get("8282371677:AAEfj9kJVYYm0AkV-x3UZ2WYoqLor-ccaEo")

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await update.message.reply_text(
            "Привет! 👋\n"
            "Я сейчас не онлайн, отвечу позже 😊\n\n"
            "📌 Прайс: https://t.me/AnonimHAB/23"
        )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))
app.run_polling()
