import telebot # импортирует библиотеку тг бота
from telebot import types # импортирует types из telebot (для кнопок)

bot = telebot.TeleBot('') # сюда вставляем токен

@bot.message_handler(commands=['start']) # команда /start
def start(message): # функция старта
    bot.send_message(message.chat.id, 'Вы запустили бота!') # сообщение от бота

@bot.message_handler(commands=['stop']) # команда /stop
def stop(message): # функция стопа
    keyboard_markup = types.ReplyKeyboardMarkup(row_width=1) # обработка кнопок
    btn1 = types.KeyboardButton('/start') # создание кнопки
    keyboard_markup.add(btn1) # подключение кнопки
    bot.send_message(message.chat.id, 'Вы остановили бота, надеемся вы вернетесь.', reply_markup=keyboard_markup) # сообщение + вывод кнопки

bot.polling(none_stop=True) # запускает цикл
