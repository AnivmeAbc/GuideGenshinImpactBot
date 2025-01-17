import telebot
from telebot import types
import logging

BOT_API = '7262313311:AAHa0BEw81CPtmQvUdljNfE4EI67oQf0BpA'


bot = telebot.TeleBot(BOT_API)
from telebot import types
telebot.logger.setLevel(logging.INFO)


@bot.message_handler(commands=['start'])
def start(message):
    # создаём клавиатуру
    markup = types.InlineKeyboardMarkup()
    # добавляем на неё две кнопки
    bot1 = types.InlineKeyboardButton("✨Сборки", callback_data="sborki")
    bot2 = types.InlineKeyboardButton("☠️Бездна", callback_data="bezdna")
    markup.add(bot1, bot2,)
    bot.send_message(message.chat.id, f'Привествую Вас, Путешественник/ца! Выберите кнопочку:', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data == "sborki":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        markup2 = types.InlineKeyboardMarkup()
        btn4 = types.InlineKeyboardButton('Крио', callback_data='krio')
        btn5 = types.InlineKeyboardButton('Пиро', callback_data='piro')
        btn6 = types.InlineKeyboardButton('Гидро', callback_data='gidro')
        btn7 = types.InlineKeyboardButton('Электро', callback_data='electro')
        btn8 = types.InlineKeyboardButton('Гео', callback_data='heo')
        btn9 = types.InlineKeyboardButton('Дендро', callback_data='dendro')
        btn10 = types.InlineKeyboardButton('Анемо', callback_data='anemo')
        btn11 = types.InlineKeyboardButton('🔙back', callback_data='back')
        markup2.row(btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11)
        
        #bot.send_photo(call.message.chat.id)
        bot.send_message(call.message.chat.id, 'Выберете стихию:', reply_markup=markup2)        

    #elif call.data == 'back':
        #bot.edit_message_text(call.message.text, call.message.chat.id, call.message.message_id, reply_markup=start(call.message))

    elif call.data == "bezdna":
        markup1 = types.InlineKeyboardMarkup()
        btn3 = types.InlineKeyboardButton('🔙back', callback_data='back')
        markup1.row(btn3)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        file = open('pic\бездна.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file)
        bot.send_message(call.message.chat.id, 'Актуальная инфрмация по бездне версия 5.2', reply_markup=markup1)        

    elif call.data == 'back':
        bot.edit_message_text(call.message.text, call.message.chat.id, call.message.message_id, reply_markup=start(call.message))







storage = dict()

def init_storage(user_id):
    storage[user_id] = dict(attempt=None, random_digit=None)

def set_data_storage(user_id, key, value):
    storage[user_id][key] = value

def get_data_storage(user_id):
    return storage[user_id]

bot.polling()







































'''  
@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data == "bezdna":
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        mar = types.neKeyboardButton("Назад")
        markup1.add(mar)
        file = open('pic\бездна.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file, 'Актуальная инфрмация по бездне версия 5.2')
        # Удаляем предыдущее сообщение 
        bot.delete_message(call.message.chat.id, call.message.message_id)
    elif call.data == "back":
        bot.edit_message_text(call.message.text, call.message.chat.id, call.message.message_id, reply_markup=start(call.message))
 '''



















'''
@bot.message_handler(func=lambda message: message.text.lower() == "привет")
def command_text_hi(m):
    bot.send_message(m.chat.id, "Ну привет)")
    bot.send_message(m.chat.id, "Давай поиграем?")
    bot.send_message(m.chat.id, "Напиши в какую игру будем играть (число, кнб)")


@bot.message_handler(func=lambda message: message.text.lower() == "число")
def digitgames(message):
    init_storage(message.chat.id) ### Инициализирую хранилище

    attempt = 10
    set_data_storage(message.chat.id, "attempt", attempt)

    bot.send_message(message.chat.id, f'Игра "угадай число"!\nКоличество попыток: {attempt}')

    random_digit=random.randint(1, 50)
    print(random_digit)

    set_data_storage(message.chat.id, "random_digit", random_digit)
    print(get_data_storage(message.chat.id))
 
    bot.send_message(message.chat.id, 'Готово! Загадано число от 1 до 50!')
    bot.send_message(message.chat.id, 'Введите число')
    bot.register_next_step_handler(message, process_digit_step)

def process_digit_step(message):
    user_digit = message.text
    
    if not user_digit.isdigit():
            msg = bot.reply_to(message, 'Вы ввели не цифры, введите пожалуйста цифры')
            bot.register_next_step_handler(msg, process_digit_step)
            return

    attempt = get_data_storage(message.chat.id)["attempt"]
    random_digit = get_data_storage(message.chat.id)["random_digit"]

    if int(user_digit) == random_digit:
        bot.send_message(message.chat.id, f'Ура! Ты угадал число! Это была цифра: {random_digit}')
        init_storage(message.chat.id) ### Очищает значения из хранилище
        return
    elif attempt > 1:
        attempt-=1
        set_data_storage(message.chat.id, "attempt", attempt)
        bot.send_message(message.chat.id, f'Неверно, осталось попыток: {attempt}')
        bot.register_next_step_handler(message, process_digit_step)
    else:
        bot.send_message(message.chat.id, 'Вы проиграли!')
        init_storage(message.chat.id) ### Очищает значения из хранилище
        return

@bot.message_handler(func=lambda message: message.text.lower() == "кнб")
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=3)
    markup.add(types.KeyboardButton('🗿'), types.KeyboardButton('✂️'), types.KeyboardButton('📄'))
    bot.reply_to(message, "Добро пожаловать в игру 'Камень, ножницы, бумага'! Для игры используйте кнопки ниже:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def digitgames(message):
    init_storage(message.chat.id) ### Инициализирую хранилище
    user_choice = message.text
    bot_choice = random.choice(['🗿', '✂️', '📄'])

    if user_choice not in ['🗿', '✂️', '📄']:
        bot.reply_to(message, "Пожалуйста, используйте кнопки для выбора камня, ножниц или бумаги.")
        return

    if user_choice == bot_choice:
        bot.reply_to(message, f"Вы выбрали {user_choice}, а я выбрал {bot_choice}. Ничья!")
    elif (user_choice == '🗿' and bot_choice == '✂️') or (user_choice == '✂️' and bot_choice == '📄') or (user_choice == '📄' and bot_choice == '🗿'):
        bot.reply_to(message, f"Вы выбрали {user_choice}, а я выбрал {bot_choice}. Вы победили! 🎉")
    else:
        bot.reply_to(message, f"Вы выбрали {user_choice}, а я выбрал {bot_choice}. Я победил! 😄")
'''























#@bot.message_handler(commands=['start'])
#def start(message):
#    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-помошник!", reply_markup = markup)

#@bot.message_handler(content_types=['text'])
#def get_text_messages(message):

#    if message.text == '👋 Поздороваться':
#        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
#        btn1 = types.KeyboardButton('Давай поиграем?')
#        
#        markup.add(btn1)
#        bot.send_message(message.from_user.id, '❓ Задайте интересующий вас вопрос', reply_markup = markup) #ответ бота


#    elif message.text == 'Давай поиграем?':
#        bot.send_message(message.from_user.id, 'давай', parse_mode='Markdown')