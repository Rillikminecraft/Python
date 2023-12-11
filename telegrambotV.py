import telebot
from telebot import types

bot = telebot.TeleBot('6703163977:AAH5YUlkhIvl3s8izW_4Tqb5M04FuLjTNw4')

@bot.message_handler(commands=['start', 'restart'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Сайт', url='https://akitilltka.github.io/rilikclient/index.html'))
    bot.send_message(message.chat.id, f'Вы успешно запустили бота💎\nИспользуйте /help для подробной информации⭐\nДобро пожаловать, {message.from_user.first_name}', reply_markup=markup)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Вы открыли "help" меню🔥\n/social - соц сети.\n/restart - перезагрузить бота\n/web - наш сайт\n/acc - аккаунт инфо\n/help2 - 2 страница помощи')

@bot.message_handler(commands=['help2'])
def helptwo(message):
    bot.send_message(message.chat.id, '/buy - купить клиент')

@bot.message_handler(commands=['WebSite', 'web', 'Web', 'Website', 'site', 'website'])
def WebSite(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Сайт✅', url='https://akitilltka.github.io/rilikclient/index.html'))
    bot.send_message(message.chat.id, 'У нас есть сайт, кнопка ниже💥', reply_markup=markup)

@bot.message_handler(commands=['acc', 'Account', 'Acc'])
def Account(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Аккаунты✅', url='https://telegra.ph/Akkaunty-RillikClient-TGBOT-12-11'))
    bot.send_message(message.chat.id, 'У нас нету системы регестраций, подробнее о этом по кнопке ниже\nНо часто мы выводим ваш ник', reply_markup=markup)

@bot.message_handler(commands=['social', 'soc', 'Discord', 'ds', 'YT', 'YouTube', 'Youtube'])
def social(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Дискорд', url='https://discord.gg/h8Yfvzceju'))
    markup.add(types.InlineKeyboardButton('Ютуб', url='https://www.youtube.com/channel/UCcohMrB_cIzJFUbzndDNexg'))
    bot.send_message(message.chat.id, 'Вот наши соц.сети, кнопки ниже', reply_markup=markup)

@bot.message_handler(commands=['buy', 'buyer', 'Buy'])
def buy(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Покупка', url='https://discord.gg/h8Yfvzceju'))
    bot.send_message(message.chat.id, 'Купить по кнопке ниже', reply_markup=markup)

@bot.message_handler(commands=['stop'])
def stop(message):
    keyboard_markup = types.ReplyKeyboardMarkup(row_width=1)
    btn1 = types.KeyboardButton('/start')
    keyboard_markup.add(btn1)
    bot.send_message(message.chat.id, 'Будем ждать вас сново', reply_markup=keyboard_markup)

@bot.message_handler(content_types=['text'])
def send_text(message):
    global keyId
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, /help')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Пока, /stop')
    elif message.text.lower() == '':
            if keyId == '0':
                bot.send_message(message.chat.id, '')
            else:
                bot.send_message(message.chat.id, '')
    else:
        bot.send_message(message.chat.id, 'RillikClient: Не удалось оброботать запрос проверьте на правильность ввода')

bot.polling(none_stop=True)