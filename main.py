import telebot
from telebot import types
import logging

BOT_API = 'YOUR_API'


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
    file = open('pic\превью.jpg', 'rb')
    bot.send_photo(message.chat.id, file)
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
        markup2.add(btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11)
        
        #bot.send_photo(call.message.chat.id)
        bot.send_message(call.message.chat.id, 'Выберете стихию:', reply_markup=markup2)        

    #elif call.data == 'back':
        #bot.edit_message_text(call.message.text, call.message.chat.id, call.message.message_id, reply_markup=start(call.message))

    elif call.data == "bezdna":
        markup1 = types.InlineKeyboardMarkup()
        btn3 = types.InlineKeyboardButton('🔙back', callback_data='back')
        markup1.add(btn3)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        file = open('pic\бездна.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file)
        bot.send_message(call.message.chat.id, 'Актуальная инфрмация по бездне версия 5.2', reply_markup=markup1)        

    
    elif call.data == "krio": 
        markup3 = types.InlineKeyboardMarkup()
        btn12 = types.InlineKeyboardButton('Аяка', callback_data='Ayka')
        btn13 = types.InlineKeyboardButton('Эола', callback_data= 'Eola')
        btn14 = types.InlineKeyboardButton('Шень Хэ', callback_data= 'ShenHe')
        btn15 = types.InlineKeyboardButton('ЦиЦи', callback_data = 'CiCi')
        btn16 = types.InlineKeyboardButton('Ризли', callback_data = 'Rizli') 
        btn17 = types.InlineKeyboardButton('Гань Юй', callback_data= 'Koza')
        btn18 = types.InlineKeyboardButton('🔙back', callback_data='back')
        markup3.add(btn12, btn13, btn14, btn15, btn16, btn17, btn18)
        bot.send_message(call.message.chat.id, 'Выберите персонажа:', reply_markup=markup3)
        
    elif call.data  == 'Ayka': 
            markup4 = types.InlineKeyboardMarkup() 
            btn19 = types.InlineKeyboardButton('🔙back', callback_data='back') 
            markup4.add(btn19) 
            file = open('Ayaka1.jpg', 'rb')
            file1 = open('Ayaka2.jpg', 'rb')
            caption = 'Актульный гайд на Аяку'
            bot.send_photo(call.message.chat.id, file,file1, caption, reply_markup=markup4)

    elif call.data == 'Eola':
        markup5 = types.InlineKeyboardMarkup() 
        btn20 = types.InlineKeyboardButton('🔙back', callback_data='back') 
        markup5.add(btn20) 
        bot.delete_message(call.message.chat.id, call.message.message_id) 
        file = open('pic\Eoula1.jpg', 'rb') 
        caption = 'Актульный гайд на Эолу'
        bot.send_photo(call.message.chat.id, file, caption, reply_markup=markup5)
    
        
    elif call.data == 'ShenHe':
        markup6 = types.InlineKeyboardMarkup() 
        btn21 = types.InlineKeyboardButton('🔙back', callback_data='back') 
        markup6.add(btn21) 
        bot.delete_message(call.message.chat.id, call.message.message_id) 
        file = open('pic\Shenya.jpg', 'rb') 
        caption = 'Актульный гайд на Шень Хэ'
        bot.send_photo(call.message.chat.id, file, caption,reply_markup=markup6)
    
    elif call.data == 'CiCi':
        markup7 = types.InlineKeyboardMarkup() 
        btn22 = types.InlineKeyboardButton('🔙back', callback_data='back') 
        markup7.add(btn22) 
        bot.delete_message(call.message.chat.id, call.message.message_id) 
        file = open('pic\Cici1.jpg', 'rb') 
        caption = 'Актульный гайд на ЦиЦи'
        bot.send_photo(call.message.chat.id, file, caption,reply_markup=markup7)

    elif call.data == 'Rizli':
        markup8 = types.InlineKeyboardMarkup() 
        btn23 = types.InlineKeyboardButton('🔙back', callback_data='back') 
        markup8.add(btn23) 
        bot.delete_message(call.message.chat.id, call.message.message_id) 
        file = open('pic\Rizli1.jpg', 'rb') 
        caption = 'Актульный гайд на Ризли'
        bot.send_photo(call.message.chat.id, file, caption,reply_markup=markup8)
    
    elif call.data == 'Koza':
        markup9 = types.InlineKeyboardMarkup() 
        btn24 = types.InlineKeyboardButton('🔙back', callback_data='back') 
        markup9.add(btn24) 
        bot.delete_message(call.message.chat.id, call.message.message_id) 
        file = open('pic\Koza1.jpg', 'rb') 
        caption = 'Актульный гайд на Гань Юй'
        bot.send_photo(call.message.chat.id, file, caption,reply_markup=markup9)
    
    elif call.data == 'Sitlali':
        markup9 = types.InlineKeyboardMarkup() 
        btn25 = types.InlineKeyboardButton('🔙back', callback_data='back') 
        markup9.add(btn25) 
        bot.delete_message(call.message.chat.id, call.message.message_id) 
        bot.send_message(call.message.chat.id, 'Полноценный гайд пока не вышел', reply_markup=markup9)
    
    
    elif call.data == 'back': 
        bot.edit_message_text(call.message.text, call.message.chat.id, call.message.message_id, reply_markup=start(call.message)) 

    elif call.data == 'piro':
        markup10 = types.InlineKeyboardMarkup()
        btn26 = types.InlineKeyboardButton('🔙back', callback_data='back')




storage = dict()

def init_storage(user_id):
    storage[user_id] = dict(attempt=None, random_digit=None)

def set_data_storage(user_id, key, value):
    storage[user_id][key] = value

def get_data_storage(user_id):
    return storage[user_id]

bot.polling()
