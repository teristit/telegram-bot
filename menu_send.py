from telebot import types


def buttons_return(num):
    d = tuple()
    for i in num:
        d = d + (types.InlineKeyboardButton(i[0], callback_data=i[1]),)
    return d


def menu_send(message, bot):
    bot.send_message(message.from_user.id, 'Вы попали в меню')
    buttons = types.InlineKeyboardMarkup(row_width=1)

    b = buttons_return(
        [('Выбрать товар', 'but1'), ('Помощь', 'but2')])
    buttons.add(*b)
    bot.send_message(message.chat.id, text='Выберите действие', reply_markup=buttons)
