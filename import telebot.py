import telebot
from telebot import types

bot = telebot.TeleBot('')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Вы запустили бота!')

@bot.message_handler(commands=['stop'])
def stop(message):
    keyboard_markup = types.ReplyKeyboardMarkup(row_width=1)
    btn1 = types.KeyboardButton('/start')
    keyboard_markup.add(btn1)
    bot.send_message(message.chat.id, 'Вы остановили бота, надеемся вы вернетесь.', reply_markup=keyboard_markup)

bot.polling(none_stop=True)