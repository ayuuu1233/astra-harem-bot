from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from app.services.drop_service import drop_character
from app.services.cooldown_service import check_cooldown

async def drop(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not check_cooldown(update.effective_user.id):
        await update.message.reply_text("⏳ Wait 30 seconds before next drop.")
        return

    character = drop_character(update.effective_user.id)

    if not character:
        await update.message.reply_text("No characters available.")
        return

    await update.message.reply_text(
        f"✨ You pulled:\n\n"
        f"{character.name}\n"
        f"Rarity: {character.rarity}"
    )

def drop_handler():
    return CommandHandler("drop", drop)
