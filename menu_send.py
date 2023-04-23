from telebot import types


def menu_send(id, bot):
    buttons = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton('Заказать товар', callback_data='menu_but_1')
    button2 = types.InlineKeyboardButton('Проверить статус товара', callback_data='menu_but_2')
    button3 = types.InlineKeyboardButton('Помощь', callback_data='menu_but_3')
    buttons.add(button1, button2, button3)
    bot.send_message(id, text='Выберите действие', reply_markup=buttons)
