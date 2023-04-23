from telebot import types


def help_send(message, bot):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    faq = types.KeyboardButton('FAQ')
    support = types.KeyboardButton('Написать в поддержку🖍')
    markup.add(faq, support)
    bot.send_message(message.from_user.id, 'Вы попали в раздел поддержки')
    bot.send_message(message.from_user.id,
                     'Вы можете посмотреть раздел часто задаваемые вопросы написав /FAQ или нажать на кнопку FAQ')
    bot.send_message(message.from_user.id,
                     'Если вы не нашли ответ на свой вопрос напишите его нашей поддержке и наши сотрудники '
                     'постараются в кратчайшее время решить вашу проблему',
                     reply_markup=markup)
