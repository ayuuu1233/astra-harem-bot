from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from app.services.economy_service import sell_character

async def sell(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not context.args:
        await update.message.reply_text("Usage: /sell CharacterName")
        return

    character_name = " ".join(context.args)

    value, error = sell_character(
        update.effective_user.id,
        character_name
    )

    if error:
        await update.message.reply_text(error)
        return

    await update.message.reply_text(
        f"💰 Sold {character_name} for {value} coins!"
    )

def sell_handler():
    return CommandHandler("sell", sell)
