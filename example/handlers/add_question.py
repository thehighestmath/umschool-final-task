import telebot.types


from init_bot import bot


@bot.message_handler()
def start_addition_question(message: telebot.types.Message):
    pass


@bot.message_handler()
def wait_question(message: telebot.types.Message):
    pass


@bot.message_handler()
def wait_choice(message: telebot.types.Message):
    pass
