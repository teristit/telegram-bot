from telebot import types


def first_answer(message, bot):
    pass


def second_answer(message, bot):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = types.KeyboardButton('Вернуться к часто задаваемым вопросам')
    markup.add(back)
    bot.send_message(message.from_user.id, '1. Оплатить товар можно при получении в пункте выдачи'
                                           ' для этого наши пункты выдачи оборудованы терменалами')
    bot.send_message(message.from_user.id,
                     '2. Оплатить товар можно курьеру при получении для этого у курьера имееться терминал',
                     reply_markup=markup)


def third_answer(message, bot):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = types.KeyboardButton('Вернуться к часто задаваемым вопросам')
    markup.add(back)
    bot.send_message(message.from_user.id,
                     '1. Получить товар можно в наших пунктах выдачи или заказать товар на дом')
    bot.send_message(message.from_user.id,
                     '2. Если вы закажите товар на дом то его привезет курьер', reply_markup=markup)


def fourth_answer(message, bot):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = types.KeyboardButton('Вернуться к часто задаваемым вопросам')
    points = types.KeyboardButton('Пункты выдачи')
    markup.add(points, back)
    bot.send_message(message.from_user.id,
                     'Для того чтобы узнать где находяться пункты выдачи достаточно '
                     'написать "Пункты выдачи" или нажать на соответствующую кнопку', reply_markup=markup)
