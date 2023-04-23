import sqlite3

import telebot

from answer_faq import second_answer, third_answer, first_answer
from faq_send import faq_send
from help_send import help_send
from menu_send import menu_send
from product_menu import product_menu_send, product_list_callback
from settings import TG_TOKEN, ID_ADMIN
from answers_faq import first_answer, second_answer, third_answer, fourth_answer
from points_of_issue import points_of_issue, points_Vurnary, points_Cheboksary
from correct_queries import correct_points

bot = telebot.TeleBot(TG_TOKEN)
support_check = False
user_problem = ''


@bot.message_handler(commands=['start'])
def get_text_messages(message):
    bot.send_message(message.from_user.id, 'Вы запустили бота')
    menu_send(message.from_user.id, bot)


@bot.message_handler(commands=['help'])
def help_messages(message):
    help_send(message, bot)


@bot.message_handler(commands=['FAQ'])
def faq_messages(message):
    faq_send(message, bot)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global user_problem
    global support_check
    if message.text[:4] == 'админ':
        bot.send_message(ID_ADMIN, message.text)
    elif message.text == 'FAQ':
        faq_send(message, bot)
    elif message.text == 'Вернуться в раздел поддержки':
        help_send(message, bot)
    elif message.text == 'Вернуться к часто задаваемым вопросам':
        faq_send(message, bot)
    elif 'пун' in message.text.lower() or 'пнк' in message.text.lower() or 'пкты' in message.text.lower():
        correct = correct_points(message.text)
        if correct[0] == 'Пункты выдачи':
            if correct[1]:
                points_of_issue(message, bot)
            else:
                bot.send_message(message.from_user.id, 'Мои алгоритмы еще не совершены и я '
                                                       'не совсем понял что вы имели ввиду но возможно вы хотели это:')
                points_of_issue(message, bot)
        elif correct[0] == 'Пункты выдачи в Вурнарах':
            if correct[1]:
                points_Vurnary(message, bot)
            else:
                bot.send_message(message.from_user.id, 'Мои алгоритмы еще не совершены и я '
                                                       'не совсем понял что вы имели ввиду но возможно вы хотели это:')
                points_Vurnary(message, bot)
        elif correct[0] == 'Пункты выдачи в Чебоксарах':
            if correct[1]:
                points_Cheboksary(message, bot)
            else:
                bot.send_message(message.from_user.id, 'Мои алгоритмы еще не совершены и я '
                                                       'не совсем понял что вы имели ввиду но возможно вы хотели это:')
                points_Vurnary(message, bot)
    elif message.text == 'Написать в поддержку🖍':
        support(message, bot)
        support_check = True
    elif message.text == 'Создать обращение✉':
        add_user(message, bot, user_problem)
        support_check = False
        user_problem = ''
    else:
        if support_check:
            user_problem += message.text
            user_problem += '\n'
        else:
            bot.send_message(message.from_user.id, message.text)


# обработка нажатия кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    # удаление InlineKeyboardButton
    bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'but_faq_1':

        first_answer(call, bot)
    elif call.data == 'but_faq_2':

        second_answer(call, bot)
    elif call.data == 'but_faq_3':

        third_answer(call, bot)
    elif call.data == 'menu_but_1':
        product_menu_send(call.from_user.id, bot)
    elif call.data == 'menu_but_2':
        pass
    elif call.data == 'menu_but_3':
        faq_send(call, bot)
    elif call.data == product_list_callback:
        con = sqlite3.connect('orders.db')
        with con:
            con.execute("""
                CREATE TABLE USER (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    age INTEGER
                );
            """)


bot.polling(none_stop=True)
