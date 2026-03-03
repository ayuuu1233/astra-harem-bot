from fastapi import FastAPI, Request, Header
from telegram import Update
from app.bot import create_bot
from app.config import settings
from app.database import Base, engine

app = FastAPI()

bot_app = create_bot()

# Create tables automatically
Base.metadata.create_all(bind=engine)

@app.post("/webhook")
async def webhook(
    request: Request,
    x_telegram_bot_api_secret_token: str = Header(None)
):
    if x_telegram_bot_api_secret_token != settings.SECRET_TOKEN:
        return {"error": "Unauthorized"}

    data = await request.json()
    update = Update.de_json(data, bot_app.bot)

    await bot_app.process_update(update)

    return {"ok": True}
