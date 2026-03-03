from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from app.database import SessionLocal
from app.models.user import User

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    db = SessionLocal()

    user = db.query(User).filter_by(
        telegram_id=update.effective_user.id
    ).first()

    if not user:
        user = User(
            telegram_id=update.effective_user.id,
            username=update.effective_user.username
        )
        db.add(user)
        db.commit()

    await update.message.reply_text(
        "🌸 Welcome to Astra Harem Enterprise!\n\n"
        "Your journey begins now."
    )

    db.close()

def start_handler():
    return CommandHandler("start", start)
