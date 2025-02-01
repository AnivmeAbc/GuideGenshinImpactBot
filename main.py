import telebot
from telebot import types
import logging

BOT_API = 'YOUR_API'


bot = telebot.TeleBot(BOT_API)
telebot.logger.setLevel(logging.INFO)

storage = dict()

@bot.message_handler(commands=['start'])
def start(message):
    # создаём клавиатуру
    markup = types.InlineKeyboardMarkup()
    # добавляем на неё две кнопки
    bot1 = types.InlineKeyboardButton("✨Сборки", callback_data="sborki")
    bot2 = types.InlineKeyboardButton("☠️Бездна", callback_data="bezdna")
    btn_akasha = types.InlineKeyboardButton("Akasha", url="https://akasha.cv/")
    markup.add(bot1, bot2, btn_akasha) 
    file = open('превью.jpg', 'rb') 
    caption = 'Привествую Вас, Путешественник/ца! Выберите кнопочку:' 
    bot.send_photo(message.chat.id, file, caption, reply_markup=markup) 
    
    

@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data == "sborki":
        #bot.delete_message(call.message.chat.id, call.message.message_id)
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
        file = open('бездна.jpg', 'rb')
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
            bot.delete_message(call.message.chat.id, call.message.message_id)
            media = [telebot.types.InputMediaPhoto(open('Ayaka1.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('Ayaka2.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('Ayaka3.jpg', 'rb'))]
            bot.send_media_group(call.message.chat.id, media)
            bot.send_message(call.message.chat.id, 'Актуальный гайд на Аяку', reply_markup=markup4)

    elif call.data == 'Eola':
            markup5 = types.InlineKeyboardMarkup() 
            btn20 = types.InlineKeyboardButton('🔙back', callback_data='back') 
            markup5.add(btn20)
            bot.delete_message(call.message.chat.id, call.message.message_id)
            media = [telebot.types.InputMediaPhoto(open('Eola1.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('Eola2.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('Eola3.jpg', 'rb'))]
            bot.send_media_group(call.message.chat.id, media)
            bot.send_message(call.message.chat.id, 'Актуальный гайд на Эолу', reply_markup=markup5) 
        
    elif call.data == 'ShenHe':
        markup6 = types.InlineKeyboardMarkup() 
        btn21 = types.InlineKeyboardButton('🔙back', callback_data='back') 
        markup6.add(btn21) 
        bot.delete_message(call.message.chat.id, call.message.message_id) 
        media = [telebot.types.InputMediaPhoto(open('ShenHe1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('ShenHe2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('ShenHe3.jpg', 'rb'))]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, 'Актульный гайд на сап Шень Хе ',reply_markup=markup6)
    
    elif call.data == 'CiCi':
        markup7 = types.InlineKeyboardMarkup() 
        btn22 = types.InlineKeyboardButton('🔙back', callback_data='back') 
        markup7.add(btn22) 
        bot.delete_message(call.message.chat.id, call.message.message_id) 
        media =[telebot.types.InputMediaPhoto(open('Cici1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('Cici2.jpg', 'rb'))]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, 'Цици подойдет в отряд ко всем крио персонажам ', reply_markup=markup7)

    elif call.data == 'Rizli':
        markup8 = types.InlineKeyboardMarkup() 
        btn23 = types.InlineKeyboardButton('🔙back', callback_data='back') 
        markup8.add(btn23) 
        bot.delete_message(call.message.chat.id, call.message.message_id) 
        media = [telebot.types.InputMediaPhoto(open('Rizli1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('Rizli2.jpg','rb'))]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, 'Ризли играется через заморозку, возможна игра через таяние, но для максимального импакта не хватит пиро статуса', reply_markup=markup8)
    
    elif call.data == 'Koza':
        markup9 = types.InlineKeyboardMarkup() 
        btn24 = types.InlineKeyboardButton('🔙back', callback_data='back') 
        markup9.add(btn24) 
        bot.delete_message(call.message.chat.id, call.message.message_id) 
        media = [telebot.types.InputMediaPhoto(open('Koza1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('Koza2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('Koza3.jpg', 'rb'))]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, 'Актуальный гайд на Гань Юй для двух ролей', reply_markup=markup9)
    
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
        
        btn26 = types.InlineKeyboardButton('Дилюк', callback_data='Diluc')
        btn27 = types.InlineKeyboardButton('Мавуика', callback_data='Mavuika')
        btn28 = types.InlineKeyboardButton('Ёимия', callback_data='Yoimiya')
        btn29 = types.InlineKeyboardButton('Кли', callback_data='Kli')
        btn30 = types.InlineKeyboardButton('Арлекино', callback_data='Arli')
        btn31 = types.InlineKeyboardButton('Лини', callback_data='Lini')
        btn32 = types.InlineKeyboardButton('Ху Тао', callback_data='XyTao')
        btn33 = types.InlineKeyboardButton('Дехья', callback_data='Dexya')
        btn34 = types.InlineKeyboardButton('🔙back', callback_data='back')
        markup10.add(btn26, btn27, btn28, btn29, btn30, btn31, btn32, btn33, btn34)

        bot.send_message(call.message.chat.id, 'Выберете персонажа:', reply_markup=markup10)   

    elif call.data == 'Diluc': 
        markup11 = types.InlineKeyboardMarkup()
        btn35 = types.InlineKeyboardButton('🔙back', callback_data='back')
        markup11.add(btn35)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('Diluc1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('Diluc2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('Diluc3.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('Diluc4.jpg', 'rb'))]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, 'Актуальный гайд на Дилюка', reply_markup=markup11)
    
    elif call.data == 'Yoimiya':
        markup12 = types.InlineKeyboardMarkup()
        btn36 = types.InlineKeyboardButton('🔙back', callback_data='back')
        markup12.add(btn36)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('Eimiya1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('Eimiya2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('Eimiya3.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('Eimiya4.jpg', 'rb'))]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, 'Актуальный гайд на Ёимию', reply_markup=markup12)

    elif call.data == 'Mavuika':
        markup18 = types.InlineKeyboardMarkup()
        btn42 = types.InlineKeyboardButton('🔙back', callback_data='back')
        markup12.add(btn36)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, 'Гайд на Мавуику пока не готов', reply_markup=markup12)
 
    elif call.data == 'Kli':
        markup13 = types.InlineKeyboardMarkup()
        btn37 = types.InlineKeyboardButton('🔙back', callback_data='back')
        markup13.add(btn37)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('Kli1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('Kli2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('Kli3.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('Kli4.jpg', 'rb'))]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, 'Актуальный гайд на Кли' , reply_markup=markup13)

    elif call.data == 'Arli':
        markup14 = types.InlineKeyboardMarkup()
        btn38 = types.InlineKeyboardButton('🔙back', callback_data='back')
        markup14.add(btn38)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('Arli1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('Arli2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('Arli3.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('Arli4.jpg', 'rb'))]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, 'Актуальный гайд на Арлекино', reply_markup=markup14)
    
    elif call.data == 'Lini':
        markup15 = types.InlineKeyboardMarkup()
        btn39 = types.InlineKeyboardButton('🔙back', callback_data='back')
        markup15.add(btn39)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('Lini1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('Lini2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('Lini3.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('Lini4.jpg', 'rb'))]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, 'Актуальный гайд на Лини', reply_markup=markup15)
    
    elif call.data == 'XyTao':
        markup16 = types.InlineKeyboardMarkup()
        btn40 = types.InlineKeyboardButton('🔙back', callback_data='back')
        markup16.add(btn40)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('XyTao1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('XyTao2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('XyTao3.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('XyTao4.jpg', 'rb'))]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, 'Актуальный гайд на Ху Тао', reply_markup=markup16)

    elif call.data == 'Dexya':
        markup17 = types.InlineKeyboardMarkup()
        btn41 = types.InlineKeyboardButton('��back', callback_data='back')
        markup17.add(btn41)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('Dexya1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('Dexya2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('Dexya3.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('Dexya4.jpg', 'rb'))]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, 'Актуальный гайд на Дехью', reply_markup=markup17)
    
    elif call.data == 'gidro':
        markup19 = types.InlineKeyboardMarkup()
        btn43 = types.InlineKeyboardButton('Елань', callback_data='Elan')
        btn44 = types.InlineKeyboardButton('Нёвиллет', callback_data='Neva')
        btn45 = types.InlineKeyboardButton('Фурина', callback_data='Furina')
        btn46 = types.InlineKeyboardButton('Тарталья', callback_data='Tartalya')
        btn47 = types.InlineKeyboardButton('Нилу', callback_data='Nily')
        btn48 = types.InlineKeyboardButton('Мона', callback_data='Mona')
        btn49 = types.InlineKeyboardButton('Сиджвин', callback_data='Sidzvin')
        btn50 = types.InlineKeyboardButton('Аято', callback_data='Ayato')
        btn51 = types.InlineKeyboardButton('Муалани', callback_data='Myalani')
        btn52 = types.InlineKeyboardButton('Кокоми', callback_data='Kokomi')
        btn53 = types.InlineKeyboardButton('🔙back', callback_data='back')
        markup10.add(btn43, btn44, btn45, btn46, btn47, btn48, btn49, btn50, btn51, btn52, btn53)

        bot.send_message(call.message.chat.id, 'Выберете персонажа:', reply_markup=markup19)   

    elif call.data == 'Elan':
        markup20 = types.InlineKeyboardMarkup()
        btn54 = types.InlineKeyboardButton('🔙back', callback_data='back')
        markup19.add(btn54)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('Elan1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('Elan2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('Elan3.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('Elan4.jpg', 'rb'))]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, 'Актуальный гайд на Елань', reply_markup=markup20)
    
    elif call.data == 'Neva':
        markup21 = types.InlineKeyboardMarkup()
        btn55 = types.InlineKeyboardButton('🔙back', callback_data='back')
        markup21.add(btn55)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('Neva1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('Neva2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('Neva3.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('Neva4.jpg', 'rb'))]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, 'Актуальный гайд на Нёвиллета', reply_markup=markup21)
    
    elif call.data =='Furina':
        markup22 = types.InlineKeyboardMarkup()
        btn56 = types.InlineKeyboardButton('🔙back', callback_data='back')
        markup22.add(btn56)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('Furina1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('Furina2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('Furina3.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('Furina4.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('Furina5.jpg', 'rb'))]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, 'Актуальный гайд на Фурину', reply_markup=markup22)

    elif call.data == 'Tartalya':
        markup23 = types.InlineKeyboardMarkup()
        btn57 = types.InlineKeyboardButton('🔙back', callback_data='back')
        markup23.add(btn57)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('Chaild1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('Chaild2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('Chaild3.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('Chaild4.jpg', 'rb'))]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, 'Актуальный гайд на Тарталью', reply_markup=markup23)

    elif call.data == 'Nily':
        markup24 = types.InlineKeyboardMarkup()
        btn58 = types.InlineKeyboardButton('🔙back', callback_data='back')
        markup24.add(btn58)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('Nily1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('Nily2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('Nily3.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('Nily4.jpg', 'rb'))]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, 'Актуальный гайд на Нилу', reply_markup=markup24)
    
    elif call.data == 'Mona':
        markup25 = types.InlineKeyboardMarkup()
        btn59 = types.InlineKeyboardButton('🔙back', callback_data='back')
        markup25.add(btn59)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('Mona1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('Mona2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('Mona3.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('Mona4.jpg', 'rb'))]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, 'Актуальный гайд на Мону', reply_markup=markup25)

    elif call.data == 'Sidzvin':
        markup26 = types.InlineKeyboardMarkup()
        btn60 = types.InlineKeyboardButton('🔙back', callback_data='back')
        markup26.add(btn60)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('Sidzvin1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('Sidzvin2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('Sidzvin3.jpg', 'rb'))]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, 'Актуальный гайд на Сиджвин', reply_markup=markup26)
    
    elif call.data == 'Ayato':
        markup27 = types.InlineKeyboardMarkup()
        btn61 = types.InlineKeyboardButton('🔙back', callback_data='back')
        markup27.add(btn61)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('Ayato1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('Ayato2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('Ayato3.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('Ayato4.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('Ayato5.jpg', 'rb'))]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, 'Актуальный гайд на Аято', reply_markup=markup27)

    elif call.data == 'Myalani':
        markup28 = types.InlineKeyboardMarkup()
        btn62 = types.InlineKeyboardButton('🔙back', callback_data='back')
        markup28.add(btn62)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('Mualani1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('Mualani2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('Mualani3.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('Mualani4.jpg', 'rb'))]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, 'Актуальный гайд на Муалани', reply_markup=markup28)

    elif call.data == 'Kokomi':
        markup29 = types.InlineKeyboardMarkup()
        btn63 = types.InlineKeyboardButton('🔙back', callback_data='back')
        markup29.add(btn63)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('Kokomi1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('Kokomi2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('Kokomi3.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('Kokomi4.jpg', 'rb'))]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, 'Актуальный гайд на Кокоми', reply_markup=markup29) 





def init_storage(user_id):
    storage[user_id] = dict(attempt=None, random_digit=None)

def set_data_storage(user_id, key, value):
    storage[user_id][key] = value

def get_data_storage(user_id):
    return storage[user_id]

bot.polling()
