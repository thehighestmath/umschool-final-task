import telebot.types


def register_handlers(bot):
    @bot.message_handler()
    def start_delete_question(message: telebot.types.Message):
        pass

    @bot.message_handler()
    def process_user_answer(message: telebot.types.Message):
        pass
