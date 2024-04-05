import telebot
from telebot import types
from telebot.handler_backends import State, StatesGroup

API_TOKEN = '7120003879:AAG34pRyUHmT0w06EoXzF8jpTjAJoPtnadg'
admins = [1505244069, 68360888707]

bot = telebot.TeleBot(API_TOKEN)



class MyStates(StatesGroup):
    deleting_question = State()
    adding_question = State()
    adding_choices = State()
    getting_answer = State()


@bot.message_handler(commands=['start'])
def bot_start(message: telebot.types.Message):
    if message.from_user.id in admins or True:
        markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add(
            telebot.types.KeyboardButton("Меню")
        )
        bot.send_message(message.chat.id,
                         'Приветствую, мой повелитель. Чего изволите сделать на этот раз?', reply_markup=markup)
    else:
        markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add(
            telebot.types.KeyboardButton("Меню")
        )
        bot.send_message(message.chat.id,
                         'Здравствуйте, это бот для прохождения опросов. Нажмите на кнопку ниже, чтобы перейти в меню',
                         reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Меню')
def bot_menu(message: telebot.types.Message):
    if message.from_user.id in admins:
        markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add(
            telebot.types.KeyboardButton("Пройти опрос"),
            telebot.types.KeyboardButton("Получить личную статистику")
        )
        markup.add(
            telebot.types.KeyboardButton("Создать вопрос"),
            telebot.types.KeyboardButton("Удалить вопрос"),
            telebot.types.KeyboardButton("Получить общую статистику")
        )
        bot.send_message(message.chat.id, 'Выберите желаемый пункт из меню', reply_markup=markup)
    else:
        markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add(
            telebot.types.KeyboardButton("Пройти опрос"),
            telebot.types.KeyboardButton("Получить личную статистику")
        )
        bot.send_message(message.chat.id, 'Выберите желаемый пункт из меню', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Создать вопрос')
def bot_wait_to_add(message: telebot.types.Message):
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(
        telebot.types.KeyboardButton("Отменить")
    )
    bot.send_message(message.chat.id, 'Введите вопрос (не более 100 символов):\n',
                     reply_markup=markup)
    bot.set_state(message.from_user.id, MyStates.adding_question, message.chat.id)


@bot.message_handler(state=MyStates.adding_question)
def bot_add_question(message: telebot.types.Message):
    with bot.retrieve_data(message.from_user.id) as data:
        data['question_id'] = 1
    bot.set_state(message.from_user.id, MyStates.adding_choices, message.chat.id)
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(
        telebot.types.KeyboardButton("Отменить")
    )
    bot.send_message(message.chat.id, 'Введите минимум 2 варианта ответа (не длиннее 30 символов каждый, по '
                                        'одному варианту ответа на каждой строке):\n', reply_markup=markup)


@bot.message_handler(state=MyStates.adding_choices)
def bot_add_choices(message: telebot.types.Message):
    with bot.retrieve_data(message.from_user.id) as data:
        print(data)
        inserted_question_id = data['question_id']


bot.add_custom_filter(telebot.custom_filters.StateFilter(bot))
bot.infinity_polling()