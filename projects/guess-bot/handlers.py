from random import randint

from telegram import ForceReply, Update
from telegram.ext import (Application, CommandHandler, ContextTypes,
                          MessageHandler, filters)


def reset_answer(context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data['answer'] = randint(0, 100)


# Command handlers


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    reset_answer(context)
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")


# Message handlers


async def guess(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Check the user message."""

    if not 'answer' in context.user_data:
        reset_answer(context)

    answer = context.user_data.get('answer', None)

    try:
        number = int(update.message.text)
        if number == answer:
            reset_answer(context)
            await update.message.reply_text("Right!")
        elif number < answer:
            await update.message.reply_text("Wrong! Go up..")
        else:
            await update.message.reply_text("Wrong! Go down..")

    except:
        await update.message.reply_text("Not a number!")
