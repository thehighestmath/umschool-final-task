import telebot.types
from telebot.handler_backends import StatesGroup, State


from db_adapter import (
    get_random_question,
    get_choices_by_question_id,
    add_user_vote_db,
)

class AnswerQuestion(StatesGroup):
    waiting_answer = State()

logger = telebot.logger

def register_handlers(bot):
    @bot.message_handler(commands=['get_new_question'])
    def start_survey(message: telebot.types.Message):
        # а что на все вопросы?
        question = get_random_question(message.from_user.id)
        choices = get_choices_by_question_id(question[0])
        bot.set_state(message.from_user.id, AnswerQuestion.waiting_answer)
        bot.send_message(message.from_user.id, question[1])
        bot.send_message(
            message.from_user.id,
            'Варианты ответа:\n'+ '\n'.join(choices),
        )

    @bot.message_handler(state=AnswerQuestion.waiting_answer)
    def process_user_answer(message: telebot.types.Message):
        print(message.text)
        user_answer = int(message.text) # посмотреть
        add_user_vote_db(user_answer, message.from_user.id)
        bot.send_message(message.from_user.id, "Записал :)")

