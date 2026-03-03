from telegram.ext import ApplicationBuilder
from app.config import settings
from app.handlers.start import start_handler
from app.handlers.drop import drop_handler
from app.handlers.harem import harem_handler

def create_bot():
    application = (
        ApplicationBuilder()
        .token(settings.BOT_TOKEN)
        .build()
    )

    application.add_handler(start_handler())
    application.add_handler(drop_handler())
    application.add_handler(harem_handler())

    return application
