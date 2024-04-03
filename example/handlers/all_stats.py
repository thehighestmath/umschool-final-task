import telebot.types

from init_bot import bot


@bot.message_handler()
def get_all_stats(message: telebot.types.Message):
    pass
