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
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    all_points = types.KeyboardButton('Вернуться ко всем пунктам выдачи')
    back = types.KeyboardButton('Вернуться к часто задаваемым вопросам')
    markup.add(all_points, back)
    bot.send_message(message.from_user.id, 'Пункты выдачи в Вурнарах распологаються по данным адресам:')
    bot.send_message(message.from_user.id, '№1: Комсомольская улица, 39')
    bot.send_message(message.from_user.id, '№2: улица Жоржа Илюкина, 22', reply_markup=markup)


def points_Cheboksary(message, bot):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    all_points = types.KeyboardButton('Вернуться ко всем пунктам выдачи')
    back = types.KeyboardButton('Вернуться к часто задаваемым вопросам')
    markup.add(all_points, back)
    bot.send_message(message.from_user.id, 'Пункты выдачи в Чебоксарах распологаються по данным адресам:')
    bot.send_message(message.from_user.id, '№1: проспект Ивана Яковлева, 4Б')
    bot.send_message(message.from_user.id, '№2: проспект Тракторостроителей, 1/34')
    bot.send_message(message.from_user.id, '№3: улица Ленинского Комсомола, 21А')
    bot.send_message(message.from_user.id, '№4: улица Калинина, 105А', reply_markup=markup)
