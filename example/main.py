import os
import logging

import telebot

from db_adapter import create_tables_in_db
from handlers import register_handlers
from init_bot import create_bot


telebot.logger.setLevel(logging.DEBUG)  # Outputs messages to console.

if __name__ == "__main__":
    create_tables_in_db()
    bot = create_bot(os.getenv('TG_TOKEN'))
    register_handlers(bot)
    bot.add_custom_filter(telebot.custom_filters.StateFilter(bot))
    print("Bot is active!")
    bot.infinity_polling()
