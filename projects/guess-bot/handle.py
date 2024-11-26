from random import randint

from telegram import ForceReply, Update
from telegram.ext import ContextTypes


def reset_answer(context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data['answer'] = randint(0, 100)


# Command handlers


async def on_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    full_name = update.effective_user.full_name
    reset_answer(context)
    await update.message.reply_html(f"Hi {full_name}!")


async def on_help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")


# Message handlers


async def on_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Check the user message."""

    if not 'answer' in context.user_data:
        reset_answer(context)

    answer = context.user_data.get('answer', None)

    try:
        guess = int(update.message.text)
        if guess == answer:
            reset_answer(context)
            await update.message.reply_text("Right!")
        elif guess < answer:
            await update.message.reply_text("Wrong! Go up..")
        else:
            await update.message.reply_text("Wrong! Go down..")

    except:
        await update.message.reply_text("Huh?")
