import telebot
from telebot import types

from faq_send import faq_send
from help_send import help_send
from settings import TG_TOKEN, ID_ADMIN

bot = telebot.TeleBot(TG_TOKEN)


def buttons_return(num):
    d = tuple()
    for i in num:
        d = d + (types.InlineKeyboardButton(i[0], callback_data=i[1]),)
    return d


@bot.message_handler(commands=['start'])
def get_text_messages(message):
    bot.send_message(message.from_user.id, 'Вы запустили бота')
    bot.send_message(message.from_user.id, 'ВыБерите действие')
    buttons = types.InlineKeyboardMarkup(row_width=1)

    b = buttons_return(
        [('Мурманская область', 'butr1'), ('Архангельская область', 'butr2')])
    buttons.add(*b)
    bot.send_message(message.chat.id, reply_markup=buttons)


@bot.message_handler(commands=['help'])
def help_messages(message):
    help_send(message, bot)


@bot.message_handler(commands=['FAQ'])
def faq_messages(message):
    faq_send(message, bot)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text[:4] == 'Админ':
        bot.send_message(ID_ADMIN, message.text)
    elif message.text == 'FAQ':
        faq_send(message, bot)
    elif message.text == 'Вернуться в раздел поддержки':
        help_send(message, bot)


bot.polling(none_stop=True)
