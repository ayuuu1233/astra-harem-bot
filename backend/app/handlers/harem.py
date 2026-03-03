from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from app.database import SessionLocal
from app.models.user import User
from app.models.inventory import Inventory
from app.models.character import Character

async def harem(update: Update, context: ContextTypes.DEFAULT_TYPE):
    db = SessionLocal()

    user = db.query(User).filter_by(
        telegram_id=update.effective_user.id
    ).first()

    if not user:
        await update.message.reply_text("Use /start first.")
        db.close()
        return

    items = db.query(Inventory).filter_by(user_id=user.id).all()

    if not items:
        await update.message.reply_text("Your harem is empty.")
        db.close()
        return

    message = "💖 Your Harem:\n\n"

    for item in items:
        character = db.query(Character).filter_by(id=item.character_id).first()
        message += f"{character.name} x{item.quantity} ({character.rarity})\n"

    await update.message.reply_text(message)

    db.close()

def harem_handler():
    return CommandHandler("harem", harem)
