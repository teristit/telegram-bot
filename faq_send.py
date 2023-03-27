from telebot import types


def faq_send(message, bot):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    first = types.KeyboardButton('1.')
    second = types.KeyboardButton('2.')
    third = types.KeyboardButton('3.')
    back_to_help = types.KeyboardButton('Вернуться в раздел поддержки')
    markup.add(first, second, third, back_to_help)
    bot.send_message(message.from_user.id,
                     'Вы попали в раздел часто задаваемых вопросов которые будут перечислены снизу')
    bot.send_message(message.from_user.id,
                     'Чтобы получить ответ на вопросы представленые ниже нажмите на кнопку с номером вопроса')
    bot.send_message(message.from_user.id, '1. Как выполнить заказ?')
    bot.send_message(message.from_user.id, '2. Как происходит оплата?')
    bot.send_message(message.from_user.id, '3. Как получить товар?', reply_markup=markup)
