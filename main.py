import telebot
from telebot import types
import logging

BOT_API = 'API_KEY'


bot = telebot.TeleBot(BOT_API)
telebot.logger.setLevel(logging.INFO)

storage = dict()

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    bot1 = types.InlineKeyboardButton("✨Сборки", callback_data="sborki")
    bot2 = types.InlineKeyboardButton("☠️Бездна", callback_data="bezdna")
    btn_akasha = types.InlineKeyboardButton("Akasha", url="https://akasha.cv/")
    btn_help = types.InlineKeyboardButton('Об игре', callback_data="help")
    markup.add(bot1, bot2, btn_akasha, btn_help) 
    file = open('pic/превью.jpg', 'rb') 
    caption = 'Привет, Путешественник! Этот бот поможет разобраться как собрать своих персонажей для F2P игры, выбери кнопку " Об игре ", чтобы ознакомиться с основами Genshin Impact. К звёздам и безднам!'
    bot.send_photo(message.chat.id, file, caption, reply_markup=markup) 
    
    

@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data == "sborki":
        markup2 = types.InlineKeyboardMarkup(row_width=2)
        btn4 = types.InlineKeyboardButton('Крио', callback_data='krio')
        btn5 = types.InlineKeyboardButton('Пиро', callback_data='piro')
        btn6 = types.InlineKeyboardButton('Гидро', callback_data='gidro')
        btn7 = types.InlineKeyboardButton('Электро', callback_data='electro')
        btn8 = types.InlineKeyboardButton('Гео', callback_data='geo')
        btn9 = types.InlineKeyboardButton('Дендро', callback_data='dendro')
        btn10 = types.InlineKeyboardButton('Анемо', callback_data='anemo')
        btn11 = types.InlineKeyboardButton('🔙back', callback_data='back')
        markup2.add(btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11)    
        bot.send_message(call.message.chat.id, 'Выберете стихию:', reply_markup=markup2)

    elif call.data =='help':
        markup_help = types.InlineKeyboardMarkup()
        btnhelp = types.InlineKeyboardButton('🔙back', callback_data='back')
        markup_help.add(btnhelp)
        bot.send_message(call.message.chat.id,
        ''' 
В игре 7 регионов и 7 соответствуюищх им стихий: 
Монштад, Ли Юэ, Инадзума, Сумеру, Фонтейн, Натлан, Снежная(пока не добавлена в игре) 
и соответственно им стихии: Анемо, Гео, Электро, Дендро, Гидро, Пиро и Крио.
Из гайдов вы сможете узнать лучший набор артефактов и бюджетное оружие, подскажет наулучшую ротацию для максимального урона.
Персонажи выбиваются из временных баннеров, которые меняются раз в 1.5 месяца и делятся на 2 половины версии.
Открывая сундуки, выполняя задания и задания на время, а также загадки Тейвата вы получаете гемы, за которые сможете получить желаемого персонажа.
В игре имеется своя система получения персонажа - шанс 50 на 50.
Вы можете получить временного персонажа, что означает победу или можете проиграть и получать легендарного персонажа из стандартного баннера, который присутсвует в игре постоянно.
В игре имеется свой огромный лор и каждый персонаж имеет свою уникальную историю, сюжет игры будет выходить еще на протяжении минимум 5 лет,
Появиться все больше, а также врагов. Основной сюжет заключается в том что мы ищем своего родственника, по всему Тейвату.(Ищем брата или сестру зависит от того главного героя, которого вы выбрали в начале игры)
Ресурсы прокачки персонажей зависят от того в каком регионе он вышел.
Также бот поможет ознакомиться порядком волн, количеством здоровья и монстрами Витой Бездны.
Кнопка Akasha поможет ознакомиться с рейтингом вашего персонажа, вы сможете сравнить своего персонажа с персонажем другого игрока, сайт также поможет рассчитать максимально выдаваемый урон за один раз ''',
            reply_markup=markup_help
            )

    elif call.data == "bezdna":
        markup1 = types.InlineKeyboardMarkup()
        btn3 = types.InlineKeyboardButton('🔙back', callback_data='back')
        markup1.add(btn3)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        file = open('pic/бездна.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file)
        bot.send_message(call.message.chat.id, 'Актуальная инфрмация по бездне версии 5.3', reply_markup=markup1)        

    
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
        btn19 = types.InlineKeyboardButton('🔙back', callback_data='back_sbor') 
        markup4.add(btn19)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('pic/Ayaka1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Ayaka2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Ayaka3.jpg', 'rb'))]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, '''
Аяка — крио персонаж использующий в качестве оружия одноручный меч. 
Учитывая то что она является наследницей семьи Камисато, довольно известной семьи в Инадзуме, 
стоит ожидать довольно интересную историю связанную с этим персонажем, 
а также красивого и величественного и изящного боевого стиля. Место сбора ресурсов - Инадзума''',
        reply_markup=markup4)

    elif call.data == 'Eola':
        markup5 = types.InlineKeyboardMarkup() 
        btn20 = types.InlineKeyboardButton('🔙back', callback_data='back_sbor') 
        markup5.add(btn20)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('pic/Eola1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Eola2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Eola3.jpg', 'rb'))]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, '''Эола — капитан разведывательного отряда Рыцарей Фавония. 
Эта элегантная девушка с легкостью обращается с тяжелым двуручным мечом. Ее легкие и грациозные движения больше похожи на танец, а ее Крио элементарные навыки заставляют врагов замереть в предвкушении очередного пируэта. 
Место сбора ресурсов - Монштадт.''', reply_markup=markup5) 
        
    elif call.data == 'ShenHe':
        markup6 = types.InlineKeyboardMarkup() 
        btn21 = types.InlineKeyboardButton('🔙back', callback_data='back_sbor') 
        markup6.add(btn21) 
        bot.delete_message(call.message.chat.id, call.message.message_id) 
        media = [telebot.types.InputMediaPhoto(open('pic/ShenHe1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/ShenHe2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/ShenHe3.jpg', 'rb'))]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, 'Шэнь Хэ — милая, но в то же время загадочная и таинственная девушка очень много времени провела с Адептами и была ученицей Хранителя облаков, а ее навыки и сила воли была высоко оценена адептами. Место сбора ресурсов - Ли Юэ. ',reply_markup=markup6)
    
    elif call.data == 'CiCi':
        markup7 = types.InlineKeyboardMarkup() 
        btn22 = types.InlineKeyboardButton('🔙back', callback_data='back_sbor') 
        markup7.add(btn22) 
        bot.delete_message(call.message.chat.id, call.message.message_id) 
        media =[telebot.types.InputMediaPhoto(open('pic/Cici1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Cici2.jpg', 'rb'))]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, '''Ци-ци немного отличается от остальных играбельных персонажей Геншин Импакт. 
Дело в том, что по случайному стечению обстоятельств она погибла, и Адепты даровали ей новую жизнь в виде зомби. 
Несмотря на свое состояние она довольно активно может помогать вам в бою за счет способностей к вампиризму излечивая весь отряд. 
Место сбора ресурсов - Ли Юэ. ''', reply_markup=markup7)

    elif call.data == 'Rizli':
        markup8 = types.InlineKeyboardMarkup() 
        btn23 = types.InlineKeyboardButton('🔙back', callback_data='back_sbor') 
        markup8.add(btn23) 
        bot.delete_message(call.message.chat.id, call.message.message_id) 
        media = [telebot.types.InputMediaPhoto(open('pic/Rizli1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Rizli2.jpg','rb'))]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, '''
Ризли занимает должность управляющего подводной крепостью Меропид, где обитают изгнанные преступники. 
Когда кто-то хвалит Ризли за его способность решать проблемы, он просто ставит чашку чая на стол и берет газету. 
Крио мейн-дд от обычных и заряженных атак с механикой Усии. 
Изменяя собственное HP при выполнении ударов в стойке и имея риск сбить лед с замороженных противников, герой требует грамотной игры и подбора отряда.
Место сбора ресурсов - Фонтейн.
        ''', reply_markup=markup8)
    
    elif call.data == 'Koza':
        markup9 = types.InlineKeyboardMarkup() 
        btn24 = types.InlineKeyboardButton('🔙back', callback_data='back_sbor') 
        markup9.add(btn24) 
        bot.delete_message(call.message.chat.id, call.message.message_id) 
        media = [telebot.types.InputMediaPhoto(open('pic/Koza1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Koza2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Koza3.jpg', 'rb'))]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, '''
Крио лучника, в основном выполняющего роль основного дамагера от заряженных выстрелов. 
Однако, за счет механики своей ульты и встроенного в пассивные способности баффа, 
героиня способна занять позицию саб-дд, особенно при игре с Крио союзниками.
В сюжете игры Гань Юй является генеральным секретарем Цисин(Организация в Ли Юэ).
В ее жилах течет кровь цилиня, мифического зверя, поэтому Гань Юй часто ведет себя отстраненно и во многом отличается от обычных смертных.
Место сбора ресурсов - Ли Юэ.
        ''', reply_markup=markup9)
    
    elif call.data == 'Sitlali':
        markup9 = types.InlineKeyboardMarkup() 
        btn25 = types.InlineKeyboardButton('🔙back', callback_data='back_sbor') 
        markup9.add(btn25) 
        bot.delete_message(call.message.chat.id, call.message.message_id) 
        media = [telebot.types.InputMediaPhoto(open('Sitlali1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Sitlali2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Sitlali3.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Sitlali4.jpg', 'rb'))]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id,'''
Щитовик-баффер Крио стихии, использующего в качестве оружия катализатор.
В рамках боя героиня защищает союзников плотным морозным барьером и наносит ледяной урон по целям с помощью призываемого существа. 
Ситлали — крайне эрудированный шаман из племени Миктлан, который имеет плотную связь с землями Царства Ночи. 
Многие зовут девушку «бабушкой Ицтлан», на что она возмущается, но и сама не брезгует лишний раз использовать данное выражение.
Ситлали увлекается романами и предпочитает сидеть дома, не решаясь использовать свой потенциал для становления главой племени.
Место сбора ресурсов - Натлан.
        ''', reply_markup=markup9)
    
    elif call.data == 'back':
        bot.edit_message_text(call.message.text, call.message.chat.id, call.message.message_id, reply_markup=start(call.message)) 

    elif call.data == 'back_sbor':
        bot.delete_message(call.message.chat.id, call.message.message_id) 
        markup2 = types.InlineKeyboardMarkup(row_width=2)
        btn4 = types.InlineKeyboardButton('Крио', callback_data='krio')
        btn5 = types.InlineKeyboardButton('Пиро', callback_data='piro')
        btn6 = types.InlineKeyboardButton('Гидро', callback_data='gidro')
        btn7 = types.InlineKeyboardButton('Электро', callback_data='electro')
        btn8 = types.InlineKeyboardButton('Гео', callback_data='geo')
        btn9 = types.InlineKeyboardButton('Дендро', callback_data='dendro')
        btn10 = types.InlineKeyboardButton('Анемо', callback_data='anemo')
        btn11 = types.InlineKeyboardButton('🔙back', callback_data='back')
        markup2.add(btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11)    
        bot.send_message(call.message.chat.id, 'Выберете стихию:', reply_markup=markup2)
    
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
        btn35 = types.InlineKeyboardButton('🔙back', callback_data='back_sbor')
        markup11.add(btn35)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('pic/Diluc1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Diluc2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Diluc3.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Diluc4.jpg', 'rb'))]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, '''
Персонаж, который до сих пор не покидает отряды многих игроков, поскольку способен наносить немало урона без особых условий и при минимальных вложениях. 
Хозяин таверны «Доля ангелов» владеет двуручным мечом и Пиро стихией. 
Его таланты и навыки позволяют буквально испепелять всех врагов на пути. 
Данный гайд описываетпрокачку и создания сборки для героя.
Место сбора ресурсов - Монштадт.
        ''', reply_markup=markup11)
    
    elif call.data == 'Yoimiya':
        markup12 = types.InlineKeyboardMarkup()
        btn36 = types.InlineKeyboardButton('🔙back', callback_data='back_sbor')
        markup12.add(btn36)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('pic/Eimiya1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Eimiya2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Eimiya3.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Eimiya4.jpg', 'rb'))]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, '''
Еимия – мастер фейерверков из Инадзумы. Обладает Пиро стихией и уничтожает своих противников из лука. 
По своему геймплею отлично выступает в роли основного дамагера и имеет множество возможных команд, что делает ее гибкой в построении отрядов.
        ''', reply_markup=markup12)

    elif call.data == 'Mavuika':
        markup18 = types.InlineKeyboardMarkup()
        btn42 = types.InlineKeyboardButton('🔙back', callback_data='back_sbor')
        markup18.add(btn42)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('pic/Mavuika1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Mavuika2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Mavuika3.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Mavuika4.jpg', 'rb'))]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, '''
Пиро Архонта из Натлана, которая способна выполнять в команде одновременно роли основного и второстепенного дамагера. 
В зависимости от того, находится ли девушка на поле боя или в «кармане», тип ее атак меняется. 
Это позволяет ей наносить урон практически все время в бою, а также усиливать активного персонажа, включая саму себя.
Мавуика стала Архонтом Пиро региона 500 лет назад, после того, как одолела предыдущего Архонта в честной дуэли на турнире.
До становления божеством девушка была обычной смертной, но сейчас по праву считается сильнейшей в огненном королевстве.
Место сбора ресурсов - Натлан.
        ''', reply_markup=markup18)
 
    elif call.data == 'Kli':
        markup13 = types.InlineKeyboardMarkup()
        btn37 = types.InlineKeyboardButton('🔙back', callback_data='back_sbor')
        markup13.add(btn37)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('pic/Kli1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Kli2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Kli3.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Kli4.jpg', 'rb'))]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id,'''
Кли – маленькая девочка-рыцарь из Мондштадта с пиро элементом, владеющий катализатором. 
Кли очень любит мастерить бомбы и придумывать новые формулы для пороха.
В свободное время она играет со своими друзьями и куклой Додоко, которую ей подарила мать. Рыцарь-искорка легко управляется с Пиро бомбами, 
нанося огромный урон.
        ''' , reply_markup=markup13)

    elif call.data == 'Arli':
        markup14 = types.InlineKeyboardMarkup()
        btn38 = types.InlineKeyboardButton('🔙back', callback_data='back_sbor')
        markup14.add(btn38)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('pic/Arli1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Arli2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Arli3.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Arli4.jpg', 'rb'))]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, '''
Пиро копейщицу, играющую от Долга жизни. 
Ее механики позволяют ей самостоятельно навешивать на себя дебафф и при этом блокирует стороннее исцеление,что вынуждает правильно подбирать саппортов для выживаемости.
Основной урон героини исходит от обычных атак, которые при показателе Долга жизни в 30%+ окрашивают удары ее копья в Пиро инфузию. 
Арлекино может играть как в командах через различные реакции, но на отдает предпочтение щитовикам, а не хилерам, так как в бою не может принимать исцеление.
В сюжете игры Арлекино — четвертая из Предвестников Фатуи, опытный и безжалостный дипломат, известная под титулом Слуга. 
Является управляющей приюта Дом очага, созданного для сирот, которых воспитывают как братьев и сестер.
Место сбора ресурсов - Фонтейн.
        ''', reply_markup=markup14)
    
    elif call.data == 'Lini':
        markup15 = types.InlineKeyboardMarkup()
        btn39 = types.InlineKeyboardButton('🔙back', callback_data='back_sbor')
        markup15.add(btn39)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('pic/Lini1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Lini2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Lini3.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Lini4.jpg', 'rb'))]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, '''
Лини – владелец лука и Пиро стихии. 
Является известным в Кур-де-ля-Фонтейне иллюзионистом, проводящим выступления в оперном театре со своей младшей сестрой Линетт. 
На сцене он – настоящий профессионал, приковывающий тысячи взглядов. 
В то же время за кулисами остается надежным старшим братом и искренним другом. 
Каждое его движение наполнено неожиданностью, а слова и поступки всегда приносят улыбку. 
Лини кажется окруженным ореолом тайны, которую хочется, но невозможность разгадать.
Место сбора ресурсов - Фонтейн.
        ''', reply_markup=markup15)
    
    elif call.data == 'XyTao':
        markup16 = types.InlineKeyboardMarkup()
        btn40 = types.InlineKeyboardButton('🔙back', callback_data='back_sbor')
        markup16.add(btn40)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('pic/XyTao1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/XyTao2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/XyTao3.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/XyTao4.jpg', 'rb'))]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, '''
Ху Тао — управляющая ритуальным бюро «Ваншэн» в семьдесят седьмом поколении, а по совместительству атакующий Пиро персонаж с древковым оружием (копьем).
Со стороны она кажется несерьезной, а некоторых даже пугает. Однако за чудаковатостью скрывается довольно серьезная и мудрая для своих лет девушка. 
На похоронных мероприятиях Ху Тао абсолютно преображается.
В такие моменты становится очевидно, почему она, несмотря на юный возраст, является лучшей кандидатурой на пост владелицы бюро.
Место сбора ресурсов - Ли Юэ.
        ''', reply_markup=markup16)

    elif call.data == 'Dexya':
        markup17 = types.InlineKeyboardMarkup()
        btn41 = types.InlineKeyboardButton('��back', callback_data='back_sbor')
        markup17.add(btn41)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('pic/Dexya1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Dexya2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Dexya3.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Dexya4.jpg', 'rb'))]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, '''
Дэхья – наемница из Пустынников по прозвищу «Пламенная Грива». 
Она смелая и сильная, но, в отличие от своих соплеменников, девушка отнюдь не надменная или невежественная. 
Дэхья всегда готова чем-то пожертвовать ради своих друзей, как, например, ради Дуньярзады.
В игре является двуручником и владеет Пиро стихии.
Место сбора ресурсов - Сумеру.
        ''', reply_markup=markup17)

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
        markup19.add(btn43, btn44, btn45, btn46, btn47, btn48, btn49, btn50, btn51, btn52, btn53)

        bot.send_message(call.message.chat.id, 'Выберете персонажа:', reply_markup=markup19)   

    elif call.data == 'Elan':
        markup20 = types.InlineKeyboardMarkup()
        btn54 = types.InlineKeyboardButton('🔙back', callback_data='back_sbor')
        markup20.add(btn54)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('pic/Elan1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Elan2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Elan3.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Elan4.jpg', 'rb'))]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, '''
Е Лань – таинственная незнакомка, состоящая в департаменте о делах граждан Ли Юэ. 
Загадочная и от этого не менее любопытная личность. Каждый описывает девушку по-разному: начиная с внешнего облика, заканчивая именем.
О ней мало что известно, но многие пытаются добиться ее благосклонности. 
В игре представлена в виде играбельного персонажа легендарной редкости, обладающего Гидро глазом бога и луком.
Место сбора ресурсов - Ли Юэ.
        ''', reply_markup=markup20)
    
    elif call.data == 'Neva':
        markup21 = types.InlineKeyboardMarkup()
        btn55 = types.InlineKeyboardButton('🔙back', callback_data='back_sbor')
        markup21.add(btn55)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('pic/Neva1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Neva2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Neva3.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Neva4.jpg', 'rb'))]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, '''
Невиллет – верховный судья Фонтейна. Поскольку суд в Гидро регионе имеет весьма высокое значение, его можно назвать второй фигурой после Архонта. 
Мужчина славится своей беспристрастностью и суровостью, однако при этом он крайне справедлив.
Является владельцем катализатора и Гидро элемента.
Место сбора ресурсов - Фонтейн.
        ''', reply_markup=markup21)
    
    elif call.data =='Furina':
        markup22 = types.InlineKeyboardMarkup()
        btn56 = types.InlineKeyboardButton('🔙back', callback_data='back_sbor')
        markup22.add(btn56)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('pic/Furina1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Furina2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Furina3.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Furina4.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Furina5.jpg', 'rb'))]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, '''
Фурина, Гидро Архонт Фонтейна (Фокалорс) – персонаж, владеющий Гидро стихией и использующий одноручный меч в качестве оружия.
В народе ее любят за блестящие речи и элегантную стать, которые придают девушке обаяние божества. 
Однако больше всего Фурину почитают за исключительную драматичность. 
Она напоминает самых непредсказуемых театральных героев, чем и завораживает простых людей.
Место сбора ресурсов - Фонтейн.
        ''', reply_markup=markup22)

    elif call.data == 'Tartalya':
        markup23 = types.InlineKeyboardMarkup()
        btn57 = types.InlineKeyboardButton('🔙back', callback_data='back_sbor')
        markup23.add(btn57)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('pic/Chaild1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Chaild2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Chaild3.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Chaild4.jpg', 'rb'))]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, '''
Лучника Гидро стихии с особой стойкой, где он преобразует свое оружие в кинжалы. 
Его взрыв стихий имеет два разных формата со своими особенными механиками.
В отличие от большинства основных дамагеров, герой не закрывает реакции самостоятельно, а скорее обеспечивает стабильным статусом для реакций от саб-дд. 
По этой причине он редко играет в гипер-керри группах, отдавая предпочтение не высокому личному урону, а суммарному от всего отряда.
По сюжету Тарталья – одиннадцатый номер из Предвестников Фатуи, также известный как Чайльд. 
Несмотря на то, что с виду герой очень дружелюбный, с ним необходимо всегда оставаться начеку из-за его весьма неоднозначного характера.
Место сбора ресурсов - Ли Юэ.
        ''', reply_markup=markup23)

    elif call.data == 'Nily':
        markup24 = types.InlineKeyboardMarkup()
        btn58 = types.InlineKeyboardButton('🔙back', callback_data='back_sbor')
        markup24.add(btn58)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('pic/Nily1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Nily2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Nily3.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Nily4.jpg', 'rb'))]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, '''
Нилу – танцовщица из Сумеру, мастерство движений которой способно отправить любого зрителя в сказочные миры. 
И даже после окончания выступления публика, вернувшись в реальность, разбредается восвояси словно опьяненная дурманом. 
Несмотря на всю эфемерность сценического образа, в повседневной жизни Нилу такая же наивная, жизнерадостная и улыбчивая подобно любой девушке ее возраста. 
Как игровой персонаж является Гидро мечницей.
Место сбора ресурсов - Сумеру.
        ''', reply_markup=markup24)
    
    elif call.data == 'Mona':
        markup25 = types.InlineKeyboardMarkup()
        btn59 = types.InlineKeyboardButton('🔙back', callback_data='back_sbor')
        markup25.add(btn59)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('pic/Mona1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Mona2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Mona3.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Mona4.jpg', 'rb'))]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, '''
Мона — Гидро каталист легендарной редкости. 
Таинственный астролог ведет скромный образ жизни и отрабатывает долг под названием «жизнь». Уверена, что простота может открыть истины мира, а роскошь этому только помешает. 
Однажды наставница поручила Моне забрать сундучок, в котором находится нечто ценное, но запретила заглядывать внутрь, если жизнь дорога. 
Не по своей воле, астролог ослушалась приказа старой ведьмы и теперь вынуждена скрываться в Монштадте.
Место сбора ресурсов - Монштадт.
        ''', reply_markup=markup25)

    elif call.data == 'Sidzvin':
        markup26 = types.InlineKeyboardMarkup()
        btn60 = types.InlineKeyboardButton('🔙back', callback_data='back_sbor')
        markup26.add(btn60)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('pic/Sidzvin1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Sidzvin2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Sidzvin3.jpg', 'rb'))]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, '''
Сиджвин — представительница молодой расы мелюзин, работающая врачом в месте заключения осужденных преступников, Крепости Меропид. 
Несмотря на детскую внешность, занимает пост старшей медсестры и управляет тюремным лазаретом. 
В игре представлена легендарным персонажем, который обладает Гидро стихией, а в бою использует лук.
Место сбора ресурсов - Фонтейн.
        ''', reply_markup=markup26)
    
    elif call.data == 'Ayato':
        markup27 = types.InlineKeyboardMarkup()
        btn61 = types.InlineKeyboardButton('🔙back', callback_data='back_sbor')
        markup27.add(btn61)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('pic/Ayato1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Ayato2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Ayato3.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Ayato4.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Ayato5.jpg', 'rb'))]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, '''
Камисато Аято – старший брат Аяки и благородный глава одноименного клана, который не любит появляться на публике, но стремится поддерживать процветание и стабильность региона. 
Как игровой персонаж является мечником, владеющим Гидро стихией.
Хотя герой довольно прост в использовании, его отряды, прокачка и ротации обладают определенными нюансами, которые важно учитывать при составлении сборки Аято. 
Место сбора ресурсов - Инадзума.
        ''', reply_markup=markup27)

    elif call.data == 'Myalani':
        markup28 = types.InlineKeyboardMarkup()
        btn62 = types.InlineKeyboardButton('🔙back', callback_data='back_sbor')
        markup28.add(btn62)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('pic/Mualani1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Mualani2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Mualani3.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Mualani4.jpg', 'rb'))]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, '''
Муалани — проводник из Народа Родников, одного из племён, проживающих в Натлане. 
Несмотря на то, что девушка является представительницей самого молодого поколения племени, она знает Пиро регион как свои пять пальцев и является известным гидом, который покажет все самые интересные места. 
Муалани всегда способна подсказать самые быстрые и безопасные маршруты по Натлану, если необходимо куда-то добраться. 
В игре представлена в качестве Гидро персонажа, обладающего катализатором.
Место сбора ресурсов - Натлан.
        ''', reply_markup=markup28)

    elif call.data == 'Kokomi':
        markup29 = types.InlineKeyboardMarkup()
        btn63 = types.InlineKeyboardButton('🔙back', callback_data='back_sbor')
        markup29.add(btn63)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('pic/Kokomi1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Kokomi2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Kokomi3.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Kokomi4.jpg', 'rb'))]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, '''
Сангономия Кокоми – Божественная жрица и играбельный персонаж из Инадзумы. 
Владеет катализатором и Гидро Глазом Бога. 
Будучи главой острова Ватацуми, девушка очень интересуется политикой и дипломатией. 
Она достигла мастерства в области военного искусства и имеет репутацию гения-тактика.
Несмотря на сложные отношения с сегунатом и Электро Архонтом, героиня заинтересована в благополучии не только собственного острова, но и всего региона.
Место сбора ресурсов - Инадзума.
        ''', reply_markup=markup29) 

    elif call.data == 'electro':
        markup30 = types.InlineKeyboardMarkup()
        bot.delete_message(call.message.chat.id, call.message.message_id)
        btn64 = types.InlineKeyboardButton('Райден', callback_data = 'Ei')
        btn65 = types.InlineKeyboardButton('Яэ Мико', callback_data = 'Miko')
        btn66 = types.InlineKeyboardButton('Клоринда', callback_data ='Klorinda')
        btn67 = types.InlineKeyboardButton('Сайно', callback_data = 'Saino')
        btn68 = types.InlineKeyboardButton('Кэ Цин', callback_data = 'Keka')
        btn69 = types.InlineKeyboardButton('🔙back', callback_data = 'back_sbor')
        markup30.add(btn64, btn65, btn66, btn67, btn68, btn69)

        bot.send_message(call.message.chat.id, 'Выберите персонажа:', reply_markup=markup30)

    elif call.data == 'Ei':
        markup31 = types.InlineKeyboardMarkup()
        btn70 = types.InlineKeyboardButton('🔙back', callback_data = 'back_sbor')
        markup31.add(btn70)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('pic/Raiden1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Raiden2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Raiden3.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Raiden4.jpg', 'rb'))]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, '''
Электро дамагера, который наносит высокий урон в стойке и имеет саппортскую способность к восстановлению энергии. 
Из-за универсальности ее способностей с ней можно по-разному играть и задействовать ее во многих отрядах.
В сюжете игры Райден — Электро Архонт с демоническим именем Вельзевул, пообещавшая неизменную вечность для жителей Инадзумы. 
В народе она также известна под титулом Баал, ранее принадлежавшим ее сестре Макото(Макото умерла).
Место сбора ресурсов - Инадзума.
        ''', reply_markup=markup31)
    
    elif call.data == 'Miko':
        markup32 = types.InlineKeyboardMarkup()
        btn71 = types.InlineKeyboardButton('🔙back', callback_data = 'back_sbor')
        markup32.add(btn71)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('pic/Miko1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Miko2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Miko3.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Miko4.jpg', 'rb'))]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, '''
Яэ Мико – верховная жрица Великого храма Наруками, потомок рода Кицунэ, фамильяр Электро Архонта и главный редактор издательского дома Яэ. 
Игрокам представлена как Электро персонаж, владеющий катализатором. 
Героиня обладает мощным уроном, способна отыгрывать роли как основного дд, так и второстепенного дд с огромным взрывным уроном. 
Естественно, как любой бурстовик, она уверенно займет свое место и в револьверных группах.
Место сбора ресурсов - Инадзума.
        ''', reply_markup=markup32)

    elif call.data == 'Klorinda':
        markup33 = types.InlineKeyboardMarkup()
        btn72 = types.InlineKeyboardButton('🔙back', callback_data = 'back_sbor')
        markup33.add(btn72)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('pic/Klorinda1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Klorinda2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Klorinda3.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Klorinda4.jpg', 'rb'))]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, '''
Основной дамагер Электро стихии, который преобразовывает получаемое лечение в Долг жизни. 
В бою героиня входит в особую стойку и заменяет свой меч на пистолеты, через которые бьет обычными атаками.
Из-за своих навыков Клоринда непривередлива к саппортам и может играть как с хилерами, так и с щитовиками, получая плюсы от каждого варианта персонажа поддержки. 
Ее пассивная способность обеспечивает ее достойным количеством атаки, что позволяет отказаться от сторонних бафферов и взять в группу больше саб-дд для наилучшего суммарного урона.
По сюжету Клоринда является сильнейший судебный дуэлянт из Фонтейна. 
Девушка является подчиненной Невиллета, Верховного судьи, и помогает ему в исполнении приговора. 
Она проводит сражение с теми подсудимыми, которые вместо заключения под стражу решили боем получить свободу.
Место сбора ресурсов - Фонтейн.
        ''', reply_markup=markup33)
    
    elif call.data == 'Saino':
        markup34 = types.InlineKeyboardMarkup()
        btn73 = types.InlineKeyboardButton('🔙back', callback_data = 'back_sbor')
        markup34.add(btn73)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('pic/Saino1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Saino2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Saino3.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Saino4.jpg', 'rb'))]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, '''
Сайно – играбельный Электро персонаж. 
Занимает должность судьи и инспектора в Сумеру, высоконравственный и всегда на чеку. 
Юноша является довольно отстраненным человеком, предпочитающим сохранять ясность и лаконичность.
Место сбора ресурсов - Сумеру.
        ''', reply_markup=markup34)

    elif call.data == 'Keka':
        markup35 = types.InlineKeyboardMarkup()
        btn74 = types.InlineKeyboardButton('🔙back', callback_data = 'back_sbor')
        markup35.add(btn74)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('pic/Keka1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Keka2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Keka3.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Keka4.jpg', 'rb'))]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, '''
Электро дамагера с одноручным мечом. Героиня использует элементальный навык для создания элементальной инфузии на своих обычных и заряженных атаках, а основной урон наносит с руки и взрыва стихий.
За счет частых атак Кэ Цин хорошо играет с Дендро отрядами, постоянно поддерживая реакцию Стимуляции и получая увеличение урона каждого удара. 
В ее механиках нет привязки к определенным стихиям, а в качестве экипировки есть множество различных вариантов, но для закрытия игрового контента необходимы хорошие вложения в виде легендарных саппортов и саб-дд.
В игре Кэ Цин имеет титул Нефритовое равновесие и принадлежит группировке Цисин в Ли Юэ, которая с недоверием относится к Архонтам. 
Несмотря на свое благородное происхождение, девушка привыкла добиваться всего своими силами. 
По этой причине она не любит свой Глаз Бога, поскольку окружающие приписывают все ее достижения именно ему.
Место сбора ресурсов - Ли Юэ.
        ''', reply_markup=markup35)

    elif call.data == 'geo':
        markup36 = types.InlineKeyboardMarkup()
        btn75 = types.InlineKeyboardButton('Навия', callback_data = 'Navia')
        btn76 = types.InlineKeyboardButton('Чжун Ли', callback_data = 'Ded')
        btn77 = types.InlineKeyboardButton('Альбедо', callback_data ='Albedo')
        btn78 = types.InlineKeyboardButton('Итто', callback_data = 'Itto')
        btn79 = types.InlineKeyboardButton('Шилонен', callback_data = 'Shilo')
        btn80 = types.InlineKeyboardButton('Тиори', callback_data = 'Tiori')
        btn81 = types.InlineKeyboardButton('🔙back', callback_data = 'back')
        markup36.add(btn75, btn76, btn77, btn78, btn79, btn80, btn81)
        bot.send_message(call.message.chat.id, 'Выберите персонажа:', reply_markup=markup36)

    elif call.data == 'Navia':
        markup37 = types.InlineKeyboardMarkup()
        btn82 = types.InlineKeyboardButton('🔙back', callback_data = 'back_sbor')
        markup37.add(btn82)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('pic/Navia1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Navia2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Navia3.jpg', 'rb')),]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, '''
Навия – легендарный персонаж, владеющий двуручным мечом и Гео стихией.
Является главой организации Спина-ди-Росула, которая ставит своей целью помогать жителям Фонтейна в различных вопросах. 
Девушка обладает острым умом и невероятной интуицией, что позволяет ей анализировать события под разными углами и докапываться до истины, даже если это кажется невозможным. 
Помимо расследований, она любит выпечку, особенно макароны.
Место сбора ресурсов - Фонтейн.
        ''', reply_markup = markup37)

    elif call.data == 'Ded':
        markup38 = types.InlineKeyboardMarkup()
        btn83 = types.InlineKeyboardButton('🔙back', callback_data = 'back_sbor')
        markup38.add(btn83)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('pic/Ded1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Ded2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Ded3.jpg', 'rb')),]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, '''
Чжун Ли — это персонаж, который представляется консультантом ритуального бюро «Ваншэн», но на самом деле является Гео Архонтом. 
В бою использует копье и Гео стихию, создает самый крепкий щит в игре. 
Чжун Ли можно по праву назвать одним из наиболее разноплановых персонажей, который может облегчить игрокам прохождение самого сложного контента.
Место сбора ресурсов - Ли Юэ.
        ''', reply_markup = markup38)

    elif call.data == 'Albedo':
        markup39 = types.InlineKeyboardMarkup()
        btn84 = types.InlineKeyboardButton('🔙back', callback_data = 'back_sbor')
        markup39.add(btn84)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('pic/Albedo1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Albedo2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Albedo3.jpg', 'rb')),]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, '''
Альбедо – гениальный алхимик с одноручным мечом и Гео Глазом Бога из Мондштадта, служащий в Ордо Фавониус. 
Будучи созданием Рэйндоттир, таит в себе огромную силу и стремится изучать неизведанные тайны, проводя большую часть времени на Драконьем Хребте.        
Но, несмотря на то, что он обладает многими титулами и знаниями, Альбедо не стремится к богатству или известности, и добр и вежлив со всеми. 
Место сбора ресурсов - Монштад.
        ''', reply_markup = markup39)

    elif call.data == 'Itto':
        markup40 = types.InlineKeyboardMarkup()
        btn85 = types.InlineKeyboardButton('🔙back', callback_data = 'back_sbor')
        markup40.add(btn85)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('pic/Itto1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Itto2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Itto3.jpg', 'rb')),]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, '''
Итто – Гео персонаж, владеющий двуручным мечом. 
Является предводителем известной в Инадзуме банды Аратаки. 
Бесстрашный потомок они, несмотря на свою пугающую внешность, по жизни очень оптимистичен и всегда полон радости. 
Итто любит соревноваться, особенно его привлекают жучиные бои и игры с детьми.
Место сбора ресурсов - Инадзума.
        ''', reply_markup = markup40)
    
    elif call.data == 'Shilo':
        markup41 = types.InlineKeyboardMarkup()
        btn86 = types.InlineKeyboardButton('🔙back', callback_data = 'back_sbor')
        markup41.add(btn86)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('pic/Shilo1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Shilo2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Shilo3.jpg', 'rb')),]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, '''
Шилонен — кузнец из Нанацкайана, известная тем, что никогда не возьмется за дело до того, как узнает все подробности о предстоящей работе. 
Девушка очень ответственно относится к процессу изготовления различных предметов в кузнице, поэтому ее известность давно распространилась по всему Натлану. 
Тем не менее Шилонен иногда не хватает организованности, и вместо кузницы ее частенько можно найти спящей где-то среди деревьев. 
В бою Шилонен может совмещать как роль дебаффера за счет элементального скилла, так и баффера благодаря взрыву стихий, открытию созвездий и в зависимости от выбранного сета артефактов.
Место сбора ресурсов - Натлан.
        ''', reply_markup = markup41)

    elif call.data == 'Tiori':
        markup42 = types.InlineKeyboardMarkup()
        btn87 = types.InlineKeyboardButton('🔙back', callback_data = 'back_sbor')
        markup42.add(btn87)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('pic/Tiori1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Tiori2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Tiori3.jpg', 'rb')),]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, '''
Тиори – дизайнер одежды из Инадзумы, которая перебралась в Гидро регион, где в районе Лионез открыла собственный магазин под названием «Дом Тиори». 
Девушка обладает не очень приятным характером: она резкая и непослушная, а также относится с уважением только к тем, кто по ее мнению этого заслуживает. 
Тиори не любит, когда журналисты и просто интересующиеся лезут в ее дела, она стремится просто заниматься любимым делом и отстаивать свои идеалы любыми способами.
В игре является Гео персонажем, владеющим одноручным мечом.
Место сбора ресурсов - Инадзума.
        ''', reply_markup = markup42)
    
    elif call.data == 'anemo':
        markup43 = types.InlineKeyboardMarkup()
        btn88 = types.InlineKeyboardButton('Часка', callback_data = 'Chaska')
        btn89 = types.InlineKeyboardButton('Синь Юнь', callback_data = 'SinYun')
        btn90 = types.InlineKeyboardButton('Странник', callback_data = 'Strannik')
        btn91 = types.InlineKeyboardButton('Кадзуха', callback_data = 'Kadzyxa')
        btn92 = types.InlineKeyboardButton('Сяо', callback_data = 'Xiao')
        btn93 = types.InlineKeyboardButton('Джин', callback_data = 'Jean')
        btn94 = types.InlineKeyboardButton('Венти', callback_data = 'Venti')
        btn95 = types.InlineKeyboardButton('🔙back', callback_data = 'back')
        markup43.add(btn88, btn89, btn90, btn91, btn92, btn93, btn94, btn95)    
        bot.send_message(call.message.chat.id, 'Выберите персонажа:', reply_markup=markup43)
    
    elif call.data == 'Chaska':
        markup44 = types.InlineKeyboardMarkup()
        btn96 = types.InlineKeyboardButton('🔙back', callback_data = 'back_sbor')
        markup44.add(btn96)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('pic/Chaska1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Chaska2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Chaska3.jpg', 'rb')),]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, '''
Часка — миротворец из клана Цветочного пера в Натлане. 
Выросшая среди заврианов и прошедшая через Бездну, девушка имеет достаточно плохой самоконтроль, из-за чего в детстве часто затевала ссоры и драки. 
Однако со временем Часка сумела измениться и стала известна в Пиро регионе как надежный человек, умеющий разрешить практически все конфликты.    
Место сбора ресурсов - Натлан.
        ''', reply_markup = markup44)

    elif call.data == 'SinYun':
        markup45 = types.InlineKeyboardMarkup()
        btn97 = types.InlineKeyboardButton('🔙back', callback_data = 'back_sbor')
        markup45.add(btn97)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('pic/SinYun1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/SinYun2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/SinYun3.jpg', 'rb')),]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, '''
Сянь Юнь – мудрый Адепт, которая известна как Хранитель Облаков. 
Проживает в своей уединенной обители на горе Аоцан в Ли Юэ и впервые предстает перед Путешественником в облике белой цапли. 
Выразив интерес к мирской жизни и местной кулинарии, она решила поселиться среди людей и взяла имя Сянь Юнь. 
Отлично разбирается в механизмах и предпочитает конструировать разнообразные мелкие безделушки. 
Место сбора ресурсов - Ли Юэ.
        ''', reply_markup = markup45)

    elif call.data == 'Strannik':
        markup46 = types.InlineKeyboardMarkup()
        btn98 = types.InlineKeyboardButton('�🔙back', callback_data = 'back_sbor')
        markup46.add(btn98)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('pic/Strannik1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Strannik2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Strannik3.jpg', 'rb')),]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, '''
Странник (Скарамучча) – бывший Предвестник Фатуи и затерявшийся в вечности сосуд, обретший собственную волю. 
Загадочный юноша на протяжении всей истории является антагонистом, вызывая интерес у игроков, следящих за его запутанной судьбой. 
И, хотя его личность претерпевает некоторые изменения после сюжета Сумеру, он все же сохраняет присущие ему уникальные черты.       
Место сбора ресурсов - Сумеру.
        ''', reply_markup = markup46)

    elif call.data == 'Kadzyxa':
        markup47 = types.InlineKeyboardMarkup()
        btn99 = types.InlineKeyboardButton('🔙back', callback_data = 'back_sbor')
        markup47.add(btn99)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('pic/Kadzyxa1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Kadzyxa2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Kadzyxa3.jpg', 'rb')),]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, '''
Каэдэхара Кадзуха – странствующий самурай-ронин из Инадзумы. 
Когда-то он пережил потерю близкого друга и стал изгоем на своей родине, после чего отправился в путешествие на корабле «Южный Крест», которым управляет Бэй Доу. 
Несмотря на тяжелое прошлое, Кадзуха сохранил спокойный и добродушный характер. 
Увлекается поэзией, а также имеет превосходные навыки фехтования, которые не раз помогали ему в странствиях. 
Место сбора ресурсов - Инадзума.
        ''', reply_markup = markup47)

    elif call.data == 'Xiao':
        markup48 = types.InlineKeyboardMarkup()
        btn100 = types.InlineKeyboardButton('🔙back', callback_data = 'back_sbor')
        markup48.add(btn100)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('pic/Xiao1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Xiao2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Xiao3.jpg', 'rb')),]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, '''
Сяо — Адепт из Ли Юэ, а также последний из пяти защитников Якс. 
Сяо занимается защитой Гео региона, а в свое свободное время обитает на постоялом дворе Ваншу. 
Несмотря на свою холодность к людям, он не испытывает к ним неприязни, а лишь старается уберечь их от собственной кармы.         
Место сбора ресурсов - Ли Юэ.
        ''', reply_markup = markup48)

    elif call.data == 'Jean':
        markup49 = types.InlineKeyboardMarkup()
        btn101 = types.InlineKeyboardButton('🔙back', callback_data = 'back_sbor')
        markup49.add(btn101)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('pic/Jean1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Jean2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Jean3.jpg', 'rb')),]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, '''
Джинн – является действующим магистром Ордо Фавониус. 
Джинн с огромной внимательностью относится к своей работе, следя за Мондштадтом, пока магистр Варка отсутствует. 
Она является одним из самых способных и надежных рыцарей Ордо Фавониус, поэтому все жители Анемо региона ее любят и уважают.      
Место сбора ресурсов - Монштадт.
        ''', reply_markup = markup49)

    elif call.data == 'Venti':
        markup50 = types.InlineKeyboardMarkup()
        btn102 = types.InlineKeyboardButton('🔙back', callback_data = 'back_sbor')
        markup50.add(btn102)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('pic/venti1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/venti2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Venti3.jpg', 'rb')),]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, '''
Венти – Анемо Архонт из Мондштадта, живущий под видом простого барда. 
По характеру герой веселый и свободный, очень любит музыку и стихи, а также часто не против выпить.
Но, несмотря на озорной нрав, он очень мудрый и часто помогает Путешественнику советами. 
Сохраняя тайну своей истинной личности, Венти продолжает присматривать за Мондштадтом и оберегать его от бед.     
Место сбора ресурсов - Монштадт.
        ''', reply_markup = markup50)

    elif call.data == 'dendro':
        markup51 = types.InlineKeyboardMarkup()
        btn104 = types.InlineKeyboardButton('Нахида', callback_data = 'Naxida')
        btn105 = types.InlineKeyboardButton('Кинич', callback_data = 'Kinich')
        btn106 = types.InlineKeyboardButton('Эмилия', callback_data = 'Emilia')
        btn107 = types.InlineKeyboardButton('Аль Хайтам', callback_data = 'Xaitam')
        btn108 = types.InlineKeyboardButton('Тигнари', callback_data = 'Tignari')
        btn109 = types.InlineKeyboardButton('Бай Джу', callback_data = 'BaiZhy')
        btn103 = types.InlineKeyboardButton('🔙back', callback_data = 'back')
        markup51.add(btn104, btn105, btn106, btn107, btn108, btn109, btn103)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, 'Выбери персонажа:', reply_markup = markup51)

    elif call.data == 'Naxida':
        markup52 = types.InlineKeyboardMarkup()
        btn110 = types.InlineKeyboardButton('🔙back', callback_data = 'back_sbor')
        markup52.add(btn110)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('pic/Naxida1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Naxida2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Naxida3.jpg', 'rb')),]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, '''
Нахида, Дендро-Архонт мудрости Сумеру – малая властительница Кусанали мудра, добра и очень любит людей. 
Хотя ее почти никогда не упоминают и не воспринимают всерьез, Нахида во что бы то ни стало стремится стать квалифицированным божеством и возглавить свой народ.        
Место сбора ресурсов - Сумеру.
        ''', reply_markup = markup52)
    
    elif call.data == 'Kinich':
        markup53 = types.InlineKeyboardMarkup()
        btn111 = types.InlineKeyboardButton('🔙back', callback_data = 'back_sbor')
        markup53.add(btn111)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('pic/Kinich1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Kinich2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Kinich3.jpg', 'rb')),]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, '''
Кинич — охотник на заврианов, который повсюду передвигается со своим ручным дракончиком по имени Кухул Ахав. 
Юноша часто получает негативные отклики из-за своей работы, ведь в Натлане люди и драконы живут в мире, поэтому многие с недоверием относятся к охотникам и даже презирают их. 
Тем не менее Кинича волнует лишь оплата выданных ему поручений.
Место сбора ресурсов - Натлан.
        ''', reply_markup = markup53)

    elif call.data == 'Emilia':
        markup54 = types.InlineKeyboardMarkup()
        btn112 = types.InlineKeyboardButton('🔙back', callback_data = 'back_sbor')
        markup54.add(btn112)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('pic/Emilia1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Emilia2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Emilia3.jpg', 'rb')),]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, '''
Эмилия — известный парфюмер из Фонтейна. 
Ее изделия настолько популярны в Гидро регионе, что многим приходится занимать очереди в магазине с самой ночи, чтобы успеть купить очередную новинку. 
Помимо парфюмерии, девушка также разбирается в медицине, химии и ботанике, из-за чего в некоторых случаях созданные Эмилией духи могут обладать другими полезными свойствами, кроме приятного аромата.
Место сбора ресурсов - Фонтейн.
        ''', reply_markup = markup54)
    
    elif call.data == 'Xaitam':
        markup55 = types.InlineKeyboardMarkup()
        btn113 = types.InlineKeyboardButton('🔙back', callback_data = 'back_sbor')
        markup55.add(btn113)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('pic/Xaitam1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Xaitam2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Xaitam3.jpg', 'rb')),]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, '''
Аль-Хайтам – ученый и секретарь Академии Сумеру, который полагается исключительно на науку и факты. 
О нем известно мало, но в то же время ему доступны знания, неведомые другим. 
В делах Академии секретарь участвует только в случае необходимости, и даже при этом записывает в протокол лишь те сведения, которые заблагорассудится.       
Место сбора ресурсов - Сумеру.
        ''', reply_markup = markup55)
    
    elif call.data == 'Tignari':
        markup56 = types.InlineKeyboardMarkup()
        btn114 = types.InlineKeyboardButton('🔙back', callback_data = 'back_sbor')
        markup56.add(btn114)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('pic/Tignari1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Tignari2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/Tignari3.jpg', 'rb')),]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, '''
Тигнари – всегда приходит на помощь нуждающимся, решая проблемы быстро и профессионально. 
Однако если беда происходит по вине самого пострадавшего, встреча с лесным стражем может оказаться неоднозначной.      
Место сбора ресурсов - Сумеру.
        ''', reply_markup = markup56)
    
    elif call.data == 'BaiZhy':
        markup57 = types.InlineKeyboardMarkup()
        btn115 = types.InlineKeyboardButton('🔙back', callback_data = 'back_sbor')
        markup57.add(btn115)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        media = [telebot.types.InputMediaPhoto(open('pic/BaiZhy1.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/BaiZhy2.jpg', 'rb')),
        telebot.types.InputMediaPhoto(open('pic/BaiZhy3.jpg', 'rb')),]
        bot.send_media_group(call.message.chat.id, media)
        bot.send_message(call.message.chat.id, '''
Бай Чжу – лекарь из хижины «Бубу» в Ли Юэ. 
В городе ходят слухи, что он способен вылечить любое заболевание, кроме собственного, ведь его целительный дар не распространяется на него самого. 
Лекарства, которые готовит Бай Чжу, очень горькие, но, несмотря на это, дети Ли Юэ хорошо относятся к нему и называют «дядюшкой». 
Он очень любит свою белую змею по имени Чан Шэн, поэтому всегда берет ее с собой, обматывая вокруг шеи. 
Место сбора ресурсов - Ли Юэ.
        ''', reply_markup = markup57)
    
    

        

        
    









def set_data_storage(user_id, key, value):
    storage[user_id][key] = value

def get_data_storage(user_id):
    return storage[user_id]

bot.polling()
