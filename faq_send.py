from telebot import types


def faq_send(message, bot):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    first = types.KeyboardButton('1.')
    second = types.KeyboardButton('2.')
    third = types.KeyboardButton('3.')
    fourth = types.KeyboardButton('4.')
    back_to_help = types.KeyboardButton('Вернуться в раздел поддержки')
    markup.add(first, second, third, fourth, back_to_help)
    bot.send_message(message.from_user.id,
                     'Вы попали в раздел часто задаваемых вопросов которые будут перечислены снизу')
    bot.send_message(message.from_user.id,
                     'Чтобы получить ответ на вопросы представленые ниже нажмите на кнопку с номером вопроса')
    bot.send_message(message.from_user.id, '1. Как выполнить заказ?')
    bot.send_message(message.from_user.id, '2. Как происходит оплата?')
    bot.send_message(message.from_user.id, '3. Как получить товар?', reply_markup=markup)
    bot.send_message(message.from_user.id, '4. Как узнать где есть пункты выдачи?', reply_markup=markup)

    # создаю кнопки
    buttons = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton('Как выполнить заказ?', callback_data='but_faq_1')
    button2 = types.InlineKeyboardButton('Как происходит оплата?', callback_data='but_faq_1')
    button3 = types.InlineKeyboardButton('Как получить товар?', callback_data='but_faq_1')
    buttons.add(button1, button2, button3)
    # отправка сообщения
    bot.send_message(message.chat.id, text='Какой пунк хотие редактировать?', reply_markup=buttons)
