import sqlite3
from collections import Counter

import telebot
from telebot import types

from answer_faq import first_answer, second_answer, third_answer
from correct_queries import correct_points
from users import add_user
from faq_send import faq_send
from help_send import help_send
from menu_send import menu_send
from points_of_issue import points_of_issue, points_Vurnary, points_Cheboksary
from product_menu import product_dict_prices
from product_menu import product_list_callback
from product_menu import product_menu_send
from settings import TG_TOKEN, ID_ADMIN
from support import support
from points_menu import points_menu_send
from points_menu import points_list_callback
from points_menu import points_dict_prices

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

        con = sqlite3.connect('db/paid.db')
        userid = call.from_user.id
        cursor = con.cursor()
        result = cursor.execute("""SELECT * FROM users
                            WHERE userid = userid""").fetchall()
        if result:
            print(result[0])
            bot.send_message(call.from_user.id, result[0][4])
        else:
            bot.send_message(call.from_user.id, 'Вы ничего не заказывали')

    elif call.data == 'menu_but_3':
        faq_send(call, bot)
    elif call.data in product_list_callback():
        con = sqlite3.connect('db/orders.db')
        with con:
            con.execute("""CREATE TABLE IF NOT EXISTS users(
            userid INT PRIMARY KEY,
            products TEXT,
            prices TEXT
            );
            """)
        userid = call.from_user.id

        cursor = con.cursor()
        result = cursor.execute("""SELECT * FROM users
                    WHERE userid = userid""").fetchall()

        cursor.execute(
            """DELETE FROM users
            WHERE userid = userid""")

        products = product_dict_prices()
        products = [products[call.data][0]]
        prices = product_dict_prices()
        prices = [prices[call.data][1]]

        for elem in result:
            products.append(elem[1])
            prices.append(str(elem[2]))

        products = ' '.join(products)
        prices = ' '.join(prices)
        user = (userid, str(products), str(prices))
        cursor.execute("INSERT INTO users (userid, products, prices) VALUES (?, ?, ?)", user)

        con.commit()
        buttons = types.InlineKeyboardMarkup(row_width=1)
        button1 = types.InlineKeyboardButton('Добавить товар', callback_data='menu_but_1')
        button2 = types.InlineKeyboardButton('Выбрать пункт выдачи', callback_data='point')
        button3 = types.InlineKeyboardButton('Отмена', callback_data='cancellation')
        buttons.add(button1, button2, button3)
        # отправка сообщения
        bot.send_message(call.from_user.id, 'выберите действие', reply_markup=buttons)
    elif call.data == 'point':
        points_menu_send(call.from_user.id, bot)

    elif call.data in points_list_callback():
        print(23233)

        con = sqlite3.connect('db/orders.db')
        userid = call.from_user.id

        cursor = con.cursor()
        result = cursor.execute("""SELECT * FROM users
                            WHERE userid = userid""").fetchall()

        cursor.execute(
            """DELETE FROM users
            WHERE userid = userid""")

        con.commit()
        # база данных с выбранными пунктами выдачи
        con = sqlite3.connect('db/points.db')
        with con:
            con.execute("""CREATE TABLE IF NOT EXISTS users(
                    userid INT PRIMARY KEY,
                    products TEXT,
                    prices TEXT,
                    points TEXT
                    );
                    """)
        userid = call.from_user.id

        cursor = con.cursor()
        print(result[0])
        point = points_dict_prices()
        point = point[call.data]
        user = list(result[0])
        user.append(point[0])
        print(user)
        print(point)
        cursor.execute("INSERT INTO users (userid, products, prices, points) VALUES (?, ?, ?, ?)", user)

        con.commit()
        buttons = types.InlineKeyboardMarkup(row_width=1)
        button1 = types.InlineKeyboardButton('Оплатить', callback_data='pay')
        button2 = types.InlineKeyboardButton('Отмена', callback_data='cancellation')
        buttons.add(button1, button2)
        # отправка сообщения
        bot.send_message(call.from_user.id, 'выберите действие', reply_markup=buttons)

    elif call.data == 'pay':
        con = sqlite3.connect('db/points.db')
        userid = call.from_user.id

        cursor = con.cursor()
        result = cursor.execute("""SELECT * FROM users
                                    WHERE userid = userid""").fetchall()

        cursor.execute(
            """DELETE FROM users
            WHERE userid = userid""")

        con.commit()
        # база данных с выбранными пунктами выдачи
        con = sqlite3.connect('db/paid.db')
        with con:
            con.execute("""CREATE TABLE IF NOT EXISTS users(
                            userid INT PRIMARY KEY,
                            products TEXT,
                            prices TEXT,
                            points TEXT,
                            condition TEXT
                            );
                            """)
        userid = call.from_user.id

        cursor = con.cursor()
        res = cursor.execute("""SELECT * FROM users
                                            WHERE userid = userid""").fetchall()
        if res:
            cursor.execute(
                """DELETE FROM users
                WHERE userid = userid""")
        condition = 'В обработе платежа'
        user = list(result[0])
        user.append(condition)
        print(user)
        cursor.execute("INSERT INTO users (userid, products, prices, points, condition) VALUES (?, ?, ?, ?, ?)", user)

        con.commit()
        buttons = types.InlineKeyboardMarkup(row_width=1)
        button1 = types.InlineKeyboardButton('Оплатить', callback_data='menu')
        buttons.add(button1)
        # отправка сообщения
        summ  = user[2].split()
        summ = [int(i) for i in summ]
        summ = sum(summ)
        res = Counter(user[1].split())
        bot.send_message(call.from_user.id, f'Вы заказали:')
        for i in list(set(user[1].split())):
            bot.send_message(call.from_user.id, f'{i} {res[i]} шт')
        bot.send_message(call.from_user.id, f'отправьте {summ} на Сбер по номеру 8**********')
        menu_send(call.from_user.id, bot)

    elif call.data == 'cancellation':
        con = sqlite3.connect('data/orders.db')
        userid = call.from_user.id
        cursor = con.cursor()
        cursor.execute(
            """DELETE FROM users
            WHERE userid = userid""")
        con.commit()

        con = sqlite3.connect('data/orders.db')
        cursor = con.cursor()
        cursor.execute(
            """DELETE FROM users
            WHERE userid = userid""")
        con.commit()

        con = sqlite3.connect('data/orders.db')
        cursor = con.cursor()
        cursor.execute(
            """DELETE FROM users
            WHERE userid = userid""")
        con.commit()



bot.polling(none_stop=True)
