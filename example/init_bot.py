import telebot


def create_bot(token):
    return telebot.TeleBot(token)
