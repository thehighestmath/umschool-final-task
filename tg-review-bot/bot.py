import telebot
import os
import logging

import telebot.formatting

from code_review_checker import CodeReviewChecker
from config import TOKEN

logging.basicConfig(
    filename="bot.log",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(
        message.chat.id,
        "Привет! Отправь мне ссылку на проект на GitHub, который нужно проверить.",
    )
    logging.info("Бот запущен, начало работы с пользователем.")


@bot.message_handler(func=lambda message: True)
def check_project(message):
    chat_id = message.chat.id
    project_url = message.text
    bot.send_message(
        chat_id,
        telebot.formatting.format_text(
            telebot.formatting.hbold("Проверка началась."), f"Проект {project_url}"
        ),
        parse_mode="HTML",
    )
    os.system(f"git clone {project_url} temp_repo")

    checker = CodeReviewChecker("temp_repo")
    checker.run_checks()
    messages = checker.messages

    os.system("rm -rf temp_repo")

    result = "\n".join(messages)
    verdict = result or "Бот не нашёл замечаний"
    bot.send_message(
        chat_id,
        telebot.formatting.format_text(
            telebot.formatting.hbold("Проверка закончена."),
            "Если есть возражения -- писать @the_real_math / @kiril_python",
            "Рекомендую почитать этот документ https://github.com/thehighestmath/umschool-final-task/blob/master/review_comments.md даже если бот НЕ нашёл замечаний",
            telebot.formatting.hitalic("beta. v0.1"),
            "",
            telebot.formatting.hcode(verdict),
        ),
        parse_mode="HTML",
    )
    with open('pep8-report.out') as fp:
        report = fp.read()
    bot.send_message(
        chat_id,
        telebot.formatting.format_text(
            telebot.formatting.hcode(report),
        ),
        parse_mode="HTML",
    )
    logging.info(
        f"Проверка проекта {project_url} завершена. Результат отправлен пользователю. {verdict}"
    )


bot.polling()
