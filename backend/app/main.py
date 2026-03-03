from fastapi import FastAPI, Request, Header
from telegram import Update

from app.bot import create_bot
from app.config import settings
from app.database import Base, engine, SessionLocal
from app.models.character import Character

# Create FastAPI app
app = FastAPI()

# Create Telegram bot application
bot_app = create_bot()

# Create database tables automatically
Base.metadata.create_all(bind=engine)


# --------------------------------------------------
# INITIAL CHARACTER SEEDING (Runs once if empty)
# --------------------------------------------------

def seed_characters():
    db = SessionLocal()

    # Check if characters already exist
    if not db.query(Character).first():
        sample_characters = [
            Character(name="Sakura Flame", rarity="Common"),
            Character(name="Yuki Shadow", rarity="Rare"),
            Character(name="Astra Valkyrie", rarity="Epic"),
            Character(name="Celestia Prime", rarity="Legendary"),
            Character(name="Eternal Empress", rarity="Celestial", is_unique=True),
        ]

        db.add_all(sample_characters)
        db.commit()
        print("✅ Sample characters inserted.")

    db.close()


# Run seeding
seed_characters()


# --------------------------------------------------
# WEBHOOK ENDPOINT
# --------------------------------------------------

@app.post("/webhook")
async def webhook(
    request: Request,
    x_telegram_bot_api_secret_token: str = Header(None)
):
    """
    Telegram sends updates here.
    """

    # Security validation
    if x_telegram_bot_api_secret_token != settings.SECRET_TOKEN:
        return {"error": "Unauthorized"}

    # Parse update
    data = await request.json()
    update = Update.de_json(data, bot_app.bot)

    # Process update
    await bot_app.process_update(update)

    return {"ok": True}
