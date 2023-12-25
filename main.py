import telebot # несоветую использовать данный код так как он очень плохой, лутше зделайте сами или используйте что-то другое (этот я писал только когда начинал кодить на Python
from telebot import types

bot = telebot.TeleBot('')

@bot.message_handler(commands=['start', 'restart', 'restarting'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Купить рекламу💥', url='https://t.me/CrashPack1777'))
    bot.send_message(message.chat.id, 'Бот успешно запущен!🔥')
    bot.send_message(message.chat.id, f'Спасибо за решили воспользоватся нашим ботом✅ {message.from_user.first_name}')
    bot.send_message(message.chat.id, 'Вы попали в CrasherMineBot Beta 💎')
    bot.send_message(message.chat.id, 'Функционал бота командой /function ⭐')
    bot.send_message(message.chat.id, 'Пропишите /PlayerSuccess чтобы узнать информацию📌')
    bot.send_message(message.chat.id, 'Пропишите /version чтобы узнать текущию версию бота и другую инфу📌')
    bot.send_message(message.chat.id, 'Заходите в наш тг канал: https://t.me/CrasherMineBot 📌')
    bot.send_message(message.chat.id, 'Пропишите /social 💥')
    bot.send_message(message.chat.id, 'Реклама: None (не куплена)', reply_markup=markup)

@bot.message_handler(commands=['recode'])
def main(message):
    bot.send_message(message.chat.id, 'рекод выдет скоро)')

@bot.message_handler(commands=['buyad'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Купить рекламу💥', url='https://t.me/CrashPack1777'))
    bot.send_message(message.chat.id, '1. Реклама на данный момент стоит 130 рублей 💲')
    bot.send_message(message.chat.id, '2. Реклама покупается в ЛС у создателя бота (кнопка ниже)📌')
    bot.send_message(message.chat.id, '3. Бесплатной рекламы нет⚠️⚠️⚠️')
    bot.send_message(message.chat.id, '4. У нас есть команда /partner ✅✅✅')
    bot.send_message(message.chat.id, '5. Кликай если хочешь купить⭐', reply_markup=markup)

@bot.message_handler(commands=['connectingYOURBOT'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Покдлючить своего бота', url='https://t.me/CrashPack1777'))
    bot.send_message(message.chat.id, 'Хотитие подключить своего бота к нашему коду?')
    bot.send_message(message.chat.id, 'Цена вопроса 150 рублей', reply_markup=markup)

@bot.message_handler(commands=['partner'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Наш партнер на данный момент', url='www.goggle.com'))
    bot.send_message(message.chat.id, 'На данный момент партнерев нету')
    bot.send_message(message.chat.id, 'Вот ссылка', reply_markup=markup)

@bot.message_handler(commands=['function', 'help', 'commands', 'OK', 'menu'])
def main(message):
    bot.send_message(message.chat.id, 'Вы попали в меню упровления функционалом бота!👑')
    bot.send_message(message.chat.id, 'Функции: /programgive (выдать проги)💥')
    bot.send_message(message.chat.id, 'Функции: /crashinghelp (помощь в крашинге)💥')
    bot.send_message(message.chat.id, 'Функции: /captchahelp (помощь по каптчам)💥')
    bot.send_message(message.chat.id, 'Функции: /nonbane (помощь в обходе банов)💥')
    bot.send_message(message.chat.id, 'Функции: /stopcrashing (помощь в защите от краша сервера)💥')
    bot.send_message(message.chat.id, 'Все страницы функций /list 💥 ')
    bot.send_message(message.chat.id, '2 СТРАНИЦА ФУНКЦИЙ /function2 💥')

@bot.message_handler(commands=['function2'])
def main(message):
    bot.send_message(message.chat.id, 'Функция: /WebCaptcha учит обходить вебкаптчи💥')
    bot.send_message(message.chat.id, 'Функции: /stop (остоновить бота)🗨️')
    bot.send_message(message.chat.id, 'Функции: /restart (перезагрузить бота)🗨️')
    bot.send_message(message.chat.id, 'Функции: /version (версия бота)📋')
    bot.send_message(message.chat.id, 'Функция: /techsupport (техническая поддержка)🔥')
    bot.send_message(message.chat.id, 'Функция: /buyad (позволяет купить рекламу)👑')
    bot.send_message(message.chat.id, 'Поддержать проект /donate')

@bot.message_handler(commands=['function3'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Предложить функцию', url='https://t.me/CrashPack1777'))
    bot.send_message(message.chat.id, 'Тут пока-что нечего нету')
    bot.send_message(message.chat.id, 'Ты можешь предложить функцию с помощью кнопки ниже', reply_markup=markup)

@bot.message_handler(commands=['donate', 'Donate', 'Don', 'don'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Поддержать проект копейкой👑', url='https://www.donationalerts.com/r/reallyk'))
    bot.send_message(message.chat.id, 'Каждого донатера упомянем в нашем телеграмм канале')
    bot.send_message(message.chat.id, 'Поддержите нас по кнопке ниже', reply_markup=markup)

@bot.message_handler(commands=['list'])
def main(message):
    bot.send_message(message.chat.id, '1 страница /function ')
    bot.send_message(message.chat.id, '2 страница /function2')
    bot.send_message(message.chat.id, '3 страница /function3')

@bot.message_handler(commands=['techsupport'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Поддержка🔥', url='https://t.me/CrashPack1777'))
    bot.send_message(message.chat.id, 'в главное меню: /restart')
    bot.send_message(message.chat.id, 'вот', reply_markup=markup)

@bot.message_handler(commands=['version'])
def main(message):
    bot.send_message(message.chat.id, '⭐Текущяя версия бота 1.0 Beta')
    bot.send_message(message.chat.id, '⭐Получайте информацию об обновлениях бота в: https://t.me/CrasherMineBot')
    bot.send_message(message.chat.id, '⭐Там также выходят новости про бота')
    bot.send_message(message.chat.id, '⭐Если найдёте баги в боте пишите сюда: @CrashPack1777')
    bot.send_message(message.chat.id, '⭐Перейти в меню функций: /function')
    bot.send_message(message.chat.id, '⭐Релиз через 58 дней')

@bot.message_handler(commands=['programgive'])
def main(message):
    bot.send_message(message.chat.id, '✔️Скачивание: https://ilyxa05.moe/archive/Minecraft/Hacks/')
    bot.send_message(message.chat.id, '👑NeoWare фри бот клиент: https://discord.gg/9KbXuEmXaF')
    bot.send_message(message.chat.id, '❗Возможны вирусы!!!!! Особенно в первой ссылке!!!!')
    bot.send_message(message.chat.id, '⭐Скачивайте все на свой страх и риск')
    bot.send_message(message.chat.id, '💥Советую использовать NeoWare')

@bot.message_handler(commands=['crashinghelp'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('❗Перейти в дискорд сервер', url='https://discord.gg/mCMhWDAXPs'))
    markup.add(types.InlineKeyboardButton('Наш юутб канал', url='https://www.youtube.com/channel/UCcohMrB_cIzJFUbzndDNexg'))
    bot.send_message(message.chat.id, '🔥Помощь в крашинге:')
    bot.send_message(message.chat.id, '🔥Во 1: вам понадобится иметь хороший бот клиент я юзаю NeoWare')
    bot.send_message(message.chat.id, '🔥Во 2: (желательно) иметь CaptchaGuru, дешего но хорошо')
    bot.send_message(message.chat.id, '🔥В 3: вам нужны прокси (желательно платные) купить можно по кнопке ниже')
    bot.send_message(message.chat.id, '🔥В 4: научитесь пользоватся клиентом')
    bot.send_message(message.chat.id, '🔥В 5: не используйте такие софты как Evolution, ExtrimeHack')
    bot.send_message(message.chat.id, '🔥В 6: не используйте кряки (они могут быть заражены)')
    bot.send_message(message.chat.id, '🔥В 7: и крашьте все че можно и нельзя', reply_markup=markup)


@bot.message_handler(commands=['captchahelp'])
def main(message):
    bot.send_message(message.chat.id, '🔥Юзайте сервисы как CaptchaGuru, RuCaptcha (лутше CaptchaGuru)')
    bot.send_message(message.chat.id, '🔥Научитесь использовать AI вашего клиента (если он имеется)')
    bot.send_message(message.chat.id, '🔥В NeoWare есть NeoAI+ он обходит веб каптчи и тд')
    bot.send_message(message.chat.id, '🔥Учитесь своими ручками обходить каптчи, в таких клиентах как Biboran это возможно')

@bot.message_handler(commands=['nonbane', 'nonebane'])
def main(message):
    bot.send_message(message.chat.id, '💬.Что-бы обойти бан на всяких школо атерносах вам нужно')
    bot.send_message(message.chat.id, '☢️1. Скачать ВПН (подойдет как и фри так и платный)')
    bot.send_message(message.chat.id, '☢️2. Подключится к нему')
    bot.send_message(message.chat.id, '☢️3. Зайти (это обходит бан по айпи)')
    bot.send_message(message.chat.id, '☢️4. Это работает иногда даже на крупных проектах')
    bot.send_message(message.chat.id, '☢️5. Все зависит от страны в которой находятся сервера ВПН')

@bot.message_handler(commands=['stopcrashing'])
def main(message):
    bot.send_message(message.chat.id, '⚙️1. Вам надо использзовать BotFilter, Velocity и тд')
    bot.send_message(message.chat.id, '⚙️2. Настраивайте ботфильтр и велосити правильно')
    bot.send_message(message.chat.id, '⚙️3. Запрещайте страны типо Америки чтобы люди не могли зайти с ВПН')
    bot.send_message(message.chat.id, '⚙️4. Настраивайте основные сервера (используйте BungeeGuard,FireWall и так далее)')

@bot.message_handler(commands=['StartCrashing'])
def main(message):
    bot.send_message(message.chat.id, f'🔴В разработке...')

@bot.message_handler(commands=['PlayerSuccess', 'ps', 'player'])
def main(message):
    bot.send_message(message.chat.id, '1. Администрация, и разработчики не несут ответственности за ваши дальнейшии действия✅')
    bot.send_message(message.chat.id, '2. Соблюдайте моральные принцыпы, хотя админам пихуй✅')
    bot.send_message(message.chat.id, '3. Бла бла бла бла бла бла бла бла бла бла бла бла бла бла бла, иди уже бота юзай блять✅')
    bot.send_message(message.chat.id, '4. /function - прописывай✅')
    bot.send_message(message.chat.id, '5. А то тратишь свое время в пустую на это соглошение👥')

@bot.message_handler(commands=['AdminPromocode1267fvnvh'])
def main(message):
    bot.send_message(message.chat.id, '✅успешно активировано')
    bot.send_message(message.chat.id, '🔒откуда код?')
    bot.send_message(message.chat.id, '🔔он нечего не дает но ты топ')

@bot.message_handler(commands=['Stop', 'stop', 'botscrasher', 'crashingbot', 'botscrash', 'crash'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Телеграмм канал', url='https://t.me/CrasherMineBot'))
    bot.send_message(message.chat.id, 'Вы успешно остоновили бота🚀')
    bot.send_message(message.chat.id, 'Пропишите чтобы запустить: /start 🔨')
    bot.send_message(message.chat.id, 'Заходите в наш тг канал по ссылке ниже 📌')
    bot.send_message(message.chat.id, 'Релиз бота через (58 дней) ✅')
    bot.send_message(message.chat.id, 'Не пропустите🔔 Для этого зайдите в тг канал!', reply_markup=markup)

@bot.message_handler(commands=['WebCaptcha', 'wc'])
def main(message):
    bot.send_message(message.chat.id, '✅ Используйте AI (такие как NeoAI+)')
    bot.send_message(message.chat.id, '✅ Блять я хз че придумывать ждите след обнову')
    bot.send_message(message.chat.id, '✅ Ну кароче иди дудось уже, заебал в боте сидеть')
    bot.send_message(message.chat.id, '✅ И сотку на карту скинь')

@bot.message_handler(commands=['NewFunction'])
def main(message):
    bot.send_message(message.chat.id, '📌 не скажу блядь')
    bot.send_message(message.chat.id, 'Иди в очко')
    bot.send_message(message.chat.id, 'На карту сотку не забудь блять')

@bot.message_handler(commands=['social'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Дс серв', url='https://discord.gg/mCMhWDAXPs'))
    markup.add(types.InlineKeyboardButton('Юутб канал', url='https://www.youtube.com/channel/UCcohMrB_cIzJFUbzndDNexg'))
    markup.add(types.InlineKeyboardButton('Наш телеграмм канал', url='https://t.me/CrasherMineBot'))
    bot.send_message(message.chat.id, 'Используйте /menu чтобы перейти обратно✅ ')
    bot.send_message(message.chat.id, 'Наши соц сети📌', reply_markup=markup)

@bot.message_handler(commands=['testadmincommand'])
def main(message):
    bot.send_message(message.chat.id, 'test')
    bot.send_message(message.chat.id, 'нахуя ты зашел')
    bot.send_message(message.chat.id, 'это только админ команда пупсик')
    bot.send_message(message.chat.id, '/restart - вали отсюда давай')

@bot.message_handler(commands=['EN', 'RU'])
def main(message):
    bot.send_message(message.chat.id, 'мне лень делать переключение языков')
    bot.send_message(message.chat.id, 'иди плати 100.000$ или жди релиза')
    bot.send_message(message.chat.id, 'все иди')

@bot.message_handler(content_types=['text'])
def send_text(message):
    global keyId
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, используйте меню или /function')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Пока')
    elif message.text.lower() == '':
            if keyId == '0':
                bot.send_message(message.chat.id, '')
            else:
                bot.send_message(message.chat.id, '')
    else:
        bot.send_message(message.chat.id, 'MineCrashBeta: Не удалось оброботать запрос проверьте на правильность ввода')

bot.polling(none_stop=True)
