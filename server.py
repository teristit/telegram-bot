import telebot
from faq_send import faq_send
from help_send import help_send
from settings import TG_TOKEN, ID_ADMIN

bot = telebot.TeleBot(TG_TOKEN)


@bot.message_handler(commands=['start'])
def get_text_messages(message):
    bot.send_message(message.from_user.id, 'Вы запустили бота')


@bot.message_handler(commands=['help'])
def help_messages(message):
    help_send(message, bot)


@bot.message_handler(commands=['FAQ'])
def faq_messages(message):
    faq_send(message, bot)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text[:4] == 'Дима':
        bot.send_message(ID_ADMIN, message.text)
    elif message.text == 'FAQ':
        faq_send(message, bot)
    elif message.text == 'Вернуться в раздел поддержки':
        help_send(message, bot)
    else:
        bot.send_message(message.from_user.id, message.text)


bot.polling(none_stop=True)
