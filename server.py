import telebot

from settings import TG_TOKEN, ID_ADMIN

bot = telebot.TeleBot(TG_TOKEN)


@bot.message_handler(commands=['start'])
def get_text_messages(message):
    bot.send_message(message.from_user.id, 'Вы запустили бота')



@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text[:4] == 'Дима':
        bot.send_message(ID_ADMIN , message.text)
    else:
        bot.send_message(message.from_user.id, message.text)


bot.polling(none_stop=True)
