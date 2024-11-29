import telebot.types


def register_handlers(bot):
    @bot.message_handler()
    def get_all_stats(message: telebot.types.Message):
        pass
