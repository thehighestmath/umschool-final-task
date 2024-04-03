import telebot.types

from init_bot import bot


@bot.message_handler()
def get_my_personal_stat(message: telebot.types.Message):
    pass
