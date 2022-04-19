import telebot
import random
bot = telebot.TeleBot('5384813529:AAFF-OhjVqy0UpRYfE4RV9PuGFSWqNndVOE')

# howareyou = ['How are you?', 'how are you?', 'Как у тебя дела?', "Как дела?", "Как делишки?"]

@bot.message_handler(commands=['start'])
def start(message):
    stickHello = open('hi.webp', 'rb')
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item3 = telebot.types.KeyboardButton('Приветик!😊')
    item1 = telebot.types.KeyboardButton('Как дела? ☺️')
    item2 = telebot.types.KeyboardButton('Random Number🎲')
    item4 = telebot.types.KeyboardButton('Чем занимаешься?🙃')
    markup.add(item3, item1, item2, item4)
    bot.send_sticker(message.chat.id, stickHello)
    bot.send_message(message.chat.id, 'Приветик {0.first_name}'.format(message.from_user), parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, '''Список команд: 
1) /start
2) /help
Писать слово:
1) Приветик!😊
2) Как дела? ☺️
3) Random Number🎲
4)Чем занимаешься?🙃''')

@bot.message_handler(content_types=['text'])
def text(message):
    if message.chat.type == 'private':
        if message.text == 'Приветик!😊':
            bot.send_message(message.chat.id, 'Приветик {0.first_name}'.format(message.from_user))
        elif message.text == 'Как дела? ☺️':
            markup = telebot.types.InlineKeyboardMarkup(row_width=2)
            item1 = telebot.types.InlineKeyboardButton('Все отлично', callback_data='great')
            item2 = telebot.types.InlineKeyboardButton('Хорошо', callback_data='good')
            item3 = telebot.types.InlineKeyboardButton("Не очень", callback_data='notgood')
            item4 = telebot.types.InlineKeyboardButton("Плохо", callback_data='bad')
            item5 = telebot.types.InlineKeyboardButton('Люблю тебя :)', callback_data='loveyou')
            markup.add(item1, item2, item3, item4, item5)
            bot.send_message(message.chat.id, 'У меня все хорошо ☺️. А у тебя как?', reply_markup=markup)
            # stickHowareyou = open('howareyou.webp', 'rb')
            # bot.send_sticker(message.chat.id, stickHowareyou)
        elif message.text == 'Чем занимаешься?🙃':
            randomNumber = random.randint(1, 5)
            # print(randomNumber)
            if randomNumber == 1:
                stick = open('lying.webp', 'rb')
                bot.send_sticker(message.chat.id, stick)
                bot.send_message(message.chat.id, 'Да, так лежу....')
            elif randomNumber == 2:
                stick = open('cardplay.webp', 'rb')
                bot.send_sticker(message.chat.id, stick)
                bot.send_message(message.chat.id, 'Играю карту с подругой :)')
            elif randomNumber == 3:
                stick = open('angry.webp', 'rb')
                bot.send_sticker(message.chat.id, stick)
                bot.send_message(message.chat.id, 'У меня нет настроение....')
            elif randomNumber == 4:
                stick = open('sleeping.webp', 'rb')
                bot.send_sticker(message.chat.id, stick)
                bot.send_message(message.chat.id, 'Спать охота ааах...')
            elif randomNumber == 5:
                stick = open('cry.webp', 'rb')
                bot.send_sticker(message.chat.id, stick)
                bot.send_message(message.chat.id, 'Меня ругали родителей... :(')
        elif message.text == 'Random Number🎲':
            guessNumber = random.randint(0, 100)
            bot.send_message(message.chat.id, str(guessNumber))
            if 0 <= guessNumber < 30:
                bot.send_message(message.chat.id, 'ХАХАХА, Ты неудачник!')
            elif 29 < guessNumber < 66:
                bot.send_message(message.chat.id, "Ох у тебя плохо получается чем я :)")
            elif 65 < guessNumber < 80:
                bot.send_message(message.chat.id, 'МмМмМм, нормально нормально')
            elif 79 < guessNumber <= 100:
                bot.send_message(message.chat.id, 'Черт! Тебе повезло!')
        else:
            bot.send_message(message.chat.id, 'Прости, я тебя не понимаю :(. Напиши /help')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'great':
                stickOk = open('great.webp', 'rb')
                bot.send_sticker(call.message.chat.id, stickOk)
                bot.send_message(call.message.chat.id, 'Я рад :)')
            elif call.data == 'good':
                stickOk = open('verygood.webp', 'rb')
                bot.send_sticker(call.message.chat.id, stickOk)
                bot.send_message(call.message.chat.id, 'Отлично')
            elif call.data == 'notgood':
                stickOk = open('good.webp', 'rb')
                bot.send_sticker(call.message.chat.id, stickOk)
                bot.send_message(call.message.chat.id, 'Жаль :(')
            elif call.data == 'bad':
                stickOk = open('boring.webp', 'rb')
                bot.send_sticker(call.message.chat.id, stickOk)
                bot.send_message(call.message.chat.id, 'Мдаааа')
            elif call.data == 'loveyou':
                stickLove = open('love.webp', 'rb')
                bot.send_sticker(call.message.chat.id, stickLove)
                bot.send_message(call.message.chat.id, 'Люблю тебя💗')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='У меня все хорошо ☺️. А у тебя как?', reply_markup=None)
            bot.answer_callback_query(call.message.chat.id, show_alert=False, text='This alert!')
    except Exception as e:
        print(repr(e))

bot.polling(none_stop=True)