from telebot import types


def points_of_issue(message, bot):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
    points_v = types.KeyboardButton('Пункты выдачи в Вурнарах')
    points_ch = types.KeyboardButton('Пункты выдачи в Чебоксарах')
    back = types.KeyboardButton('Вернуться к часто задаваемым вопросам')
    markup.add(points_v, points_ch, back)
    bot.send_message(message.from_user.id, 'Наши пункты распологаються в Чувашии')
    bot.send_message(message.from_user.id, 'А именно: г. Чебоксары, пгт. Вурнары')
    bot.send_message(message.from_user.id, 'Чтобы посмотреть по каким адресам расположены пункты в интересующем '
                                           'вас городе или селе нажмите на соответсвующую кнопку', reply_markup=markup)


def points_Vurnary(message, bot):
    pass


def points_Cheboksary(message, bot):
    pass
