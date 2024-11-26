#!/usr/bin/env python
# pylint: disable=unused-argument

import logging

from handle import *
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("TOKEN").build()

    # on different commands
    application.add_handler(CommandHandler("start", on_start))
    application.add_handler(CommandHandler("help", on_help))

    # on non command i.e message
    application.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND, on_message))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
