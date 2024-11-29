import telebot.types
from telebot.handler_backends import StatesGroup, State
from datetime import datetime

from db_adapter import (
    add_question_to_db,
    add_choice_to_db,
)


class AdditionQuestion(StatesGroup):
    waiting_question = State()
    waiting_choices = State()


ADMIN_IDS = [
    369937974,  # @the_real_math
]

logger = telebot.logger


def register_handlers(bot):
    def is_admin(func):
        def wrapper(*args, **kwargs):
            message = args[0]
            if message.from_user.id in ADMIN_IDS:
                func(*args, **kwargs)
            else:
                bot.reply_to(message, "Нет прав")
        return wrapper

    @bot.message_handler(commands=['create_question'])
    @is_admin
    def start_addition_question(message: telebot.types.Message):
        bot.reply_to(message, "Введите вопрос")
        bot.set_state(message.from_user.id, AdditionQuestion.waiting_question)

    @bot.message_handler(state=AdditionQuestion.waiting_question)
    @is_admin
    def wait_question(message: telebot.types.Message):
        bot.reply_to(message, "Вопрос получен. Введите варианты ответа")
        question_text = message.text
        publish_date = datetime.now()
        inserted_question_id = add_question_to_db(question_text, publish_date)
        with bot.retrieve_data(message.from_user.id) as data:
            data['question_id'] = inserted_question_id
        bot.set_state(message.from_user.id, AdditionQuestion.waiting_choices)

    @bot.message_handler(state=AdditionQuestion.waiting_choices)
    @is_admin
    def wait_choice(message: telebot.types.Message):
        bot.reply_to(message, "Ответы получены. Сохранил")
        with bot.retrieve_data(message.from_user.id) as data:
            inserted_question_id = data['question_id']
        for x in message.text.split('\n'):
            add_choice_to_db(x, inserted_question_id)
