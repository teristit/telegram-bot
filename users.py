import telebot
import db_session
from support_to_user import User


def add_user(message, bot, problem):
    if problem:
        db_session.global_init("db/support.db")
        db_sess = db_session.create_session()
        user = User()
        user.problem = f"{problem}"
        user.set_hashed(f"{message.from_user.id}")
        db_sess.add(user)
        db_sess.commit()
        markup = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id,
                         'Ваше обращение создано и отправлено', reply_markup=markup)
