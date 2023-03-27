import telebot
from telebot import types

from menu_send import menu_send
from faq_send import faq_send
from help_send import help_send
from settings import TG_TOKEN, ID_ADMIN

bot = telebot.TeleBot(TG_TOKEN)




@bot.message_handler(commands=['start'])
def get_text_messages(message):
    bot.send_message(message.from_user.id, 'Вы запустили бота')
    menu_send(message, bot)


@bot.message_handler(commands=['help'])
def help_messages(message):
    help_send(message, bot)


@bot.message_handler(commands=['FAQ'])
def faq_messages(message):
    faq_send(message, bot)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'but1':
        pass
    elif call.data == 'but2':
        help_send(call, bot)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text[:5] == 'Админ':
        bot.send_message(ID_ADMIN, message.text)
    elif message.text == 'FAQ':
        faq_send(message, bot)
    elif message.text == 'Вернутся в меню':
        menu_send(message, bot)
    elif message.text == 'Вернуться в раздел поддержки':
        help_send(message, bot)


bot.polling(none_stop=True)
