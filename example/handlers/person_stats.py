import telebot.types


def register_handlers(bot):
    @bot.message_handler()
    def get_my_personal_stat(message: telebot.types.Message):
        pass
