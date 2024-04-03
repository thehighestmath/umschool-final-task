import telebot

from db_adapter import create_tables_from_db
from handlers import register_handlers
from init_bot import bot


if __name__ == "__main__":
    create_tables_from_db()
    register_handlers()
    bot.add_custom_filter(telebot.custom_filters.StateFilter(bot))
    print("Bot is active!")
    bot.infinity_polling()
