from telegram.ext import ApplicationBuilder
from app.config import settings
from app.handlers.start import start_handler

def create_bot():
    application = (
        ApplicationBuilder()
        .token(settings.BOT_TOKEN)
        .build()
    )

    application.add_handler(start_handler())

    return application
