import telebot
import os
import logging

import telebot.formatting

from code_review_checker import CodeReviewChecker

logging.basicConfig(filename='bot.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Ваш токен бота
TOKEN = '7120003879:AAG34pRyUHmT0w06EoXzF8jpTjAJoPtnadg'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Отправь мне ссылку на проект на GitHub, который нужно проверить.')
    logging.info("Бот запущен, начало работы с пользователем.")

@bot.message_handler(func=lambda message: True)
def check_project(message):
    chat_id = message.chat.id
    project_url = message.text
    bot.send_message(
        chat_id,
        telebot.formatting.format_text(
            telebot.formatting.hbold('Проверка началась.'),
            f'Проект {project_url}'
        ),
        parse_mode='HTML'
    )
    os.system(f'git clone {project_url} temp_repo')

    checker = CodeReviewChecker('temp_repo')
    checker.run_checks()
    messages = checker.messages

    os.system('rm -rf temp_repo')

    result = '\n'.join(messages)
    verdict = result or 'Бот не нашёл замечаний'
    bot.send_message(
        chat_id,
        telebot.formatting.format_text(
            telebot.formatting.hbold('Проверка закончена.'),
            'Если есть возражения -- писать @the_real_math / @kiril_python',
            telebot.formatting.hitalic('beta. v0.1'),
            '',
            telebot.formatting.hcode(verdict),
        ),
        parse_mode='HTML'
    )
    logging.info(f"Проверка проекта {project_url} завершена. Результат отправлен пользователю. {verdict}")

bot.polling()
