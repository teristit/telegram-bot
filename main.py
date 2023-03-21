import telebot

from settings import TG_TOKEN

bot = telebot.TeleBot(TG_TOKEN)


@bot.message_handler(commands=['start'])
def get_text_messages(message):
    bot.send_message(message.from_user.id, 'Вы запустили бота')



@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    print(message.text[:4])
    print(message.from_user.id)
    if message.text[:4] == 'Дима':
        print(1)
        bot.send_message(808686261, message.text)
    else:
        bot.send_message(message.from_user.id, message.text)


bot.polling(none_stop=True)