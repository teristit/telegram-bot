import csv

from telebot import types


# создает кнопки
def product_menu_send(id, bot):
    n = 'product_menu_send_'
    buttons = types.InlineKeyboardMarkup(row_width=1)
    # открывается файл
    csvfile = open('data/products.csv', encoding="utf8")
    # читаются данные и присваиваются переменной reader
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for index, row in enumerate(reader):
        # создается кнопка
        button1 = types.InlineKeyboardButton(row[0], callback_data=n + str(index))
        # добавляется кнопка
        buttons.add(button1)
    # отправляются кнопки
    bot.send_message(id, text='Выберите товар', reply_markup=buttons)


# возвращает список из callback_data
def product_list_callback():
    n = 'product_menu_send_'
    d = []
    # открывается файл
    csvfile = open('data/products.csv', encoding="utf8")
    # читаются данные и присваиваются переменной reader
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for index, row in enumerate(reader):
        d.append(n + str(index))
    # возвращает список
    return d


# возвращается словарь с ценами
def product_dict_prices():
    n = 'product_menu_send_'
    d = {}
    # открывается файл
    csvfile = open('data/products.csv', encoding="utf8")
    # читаются данные и присваиваются переменной reader
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for index, row in enumerate(reader):
        # row делется на значения
        row = row.split()
        # добавляется значение в словарь
        d[n + str(index)] = [row[0]]
        # добавляется значение в словарь
        d[n + str(index)].append(row[1])
    # возвращает словарь
    return d
