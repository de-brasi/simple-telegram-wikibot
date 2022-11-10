# Get main info about subject from Wikipedia

import telebot
import auth_data
from wiki import get_info_from_wiki, get_lang


def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start', 'help'])
    def send_welcome_msg(message: telebot.types.Message):
        bot.send_message(message.chat.id, "Hello! This is a Wikipedia bot."
                                          " It will help you quickly find"
                                          " out basic information about anything."
                                          "Just type word you interested in.")

    @bot.message_handler(func=lambda command: True)
    def get_main_info(message: telebot.types.Message):
        info = get_info_from_wiki(message.text, get_lang(message.text))
        bot.send_message(message.chat.id, info)

    bot.infinity_polling()


if __name__ == "__main__":
    telegram_bot(auth_data.bot_token)

