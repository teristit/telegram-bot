import csv

from telebot import types

def points_menu_send(id, bot):
    n = 'points_menu_send_'
    buttons = types.InlineKeyboardMarkup(row_width=1)
    # открывается файл
    csvfile = open('db/points.csv', encoding="utf8")
    # читаются данные и присваиваются переменной reader
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for index, row in enumerate(reader):
        # создается кнопка
        button1 = types.InlineKeyboardButton(row[0], callback_data=n + str(index))
        # добавляется кнопка
        buttons.add(button1)
    # отправляются кнопки
    bot.send_message(id, text='Выберите пункт выдачи:', reply_markup=buttons)


# возвращает список из callback_data
def points_list_callback():
    n = 'points_menu_send_'
    d = []
    # открывается файл
    csvfile = open('db/points.csv', encoding="utf8")
    # читаются данные и присваиваются переменной reader
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for index, row in enumerate(reader):
        d.append(n + str(index))
    # возвращает список
    print(d)
    return d

# возвращается словарь с ценами
def points_dict_prices():
    n = 'points_menu_send_'
    d = {}
    # открывается файл
    csvfile = open('db/points.csv', encoding="utf8")
    # читаются данные и присваиваются переменной reader
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for index, row in enumerate(reader):
        # row делется на значения
        row = row[0].split()
        # добавляется значение в словарь
        d[n + str(index)] = [row[0]]
    # возвращает словарь
    return d