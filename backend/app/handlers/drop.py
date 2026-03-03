from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from app.services.drop_service import drop_character

async def drop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    character = drop_character(update.effective_user.id)

    if not character:
        await update.message.reply_text("No characters available yet.")
        return

    await update.message.reply_text(
        f"✨ You pulled:\n\n"
        f"{character.name}\n"
        f"Rarity: {character.rarity}"
    )

def drop_handler():
    return CommandHandler("drop", drop)
