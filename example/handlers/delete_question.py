import telebot.types

from functions.database_funcs import get_all_questions_db, delete_question_by_id_db
from init_bot import bot
from keyboards.inline import numbers_questions_delete_keyboard


@bot.message_handler()
def start_delete_question(message: telebot.types.Message):
    pass


@bot.message_handler()
def process_user_answer(message: telebot.types.Message):
    pass
