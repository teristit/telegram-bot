from telebot import types


def support(message, bot):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    appeal = types.KeyboardButton('Создать обращение✉')
    markup.add(appeal)
    bot.send_message(message.from_user.id,
                     'Напишите о своей проблеме отправте ее мне после чего нажмите на кнопку: Создать обращение✉️',
                     reply_markup=markup)
