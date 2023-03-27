from telebot import types


def help_send(message, bot):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    faq = types.KeyboardButton('FAQ')
    menu = types.KeyboardButton('Вернутся в меню')
    markup.add(faq, menu)
    bot.send_message(message.from_user.id, 'Вы попали в раздел поддержки')
    bot.send_message(message.from_user.id,
                     'Вы можете посмотреть раздел часто задаваемые вопросы написав /FAQ или нажать на кнопку FAQ',
                     reply_markup=markup)
