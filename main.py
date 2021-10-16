import cfg
import telebot
from telebot import types

bot = telebot.TeleBot(cfg.token)


@bot.message_handler(commands=['start'])
def start_message(message):
    # keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
    # keyboard.row('english', 'русский')
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text='english', callback_data='language_en'))
    keyboard.add(types.InlineKeyboardButton(text='русский', callback_data='language_ru'))
    bot.send_message(message.chat.id, '''Choose your language /
Выбери язык ''', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def help_message(message):
    if cfg.lang_en:
        bot.send_message(message.chat.id, '''
            You can see a list of command:
/shops - shops, that I support
/add_product - add product to my list: copy product link from one of the supported sites and send it to me
/delete_product_fromlist - delete product: I will not check the price of this thing and you will not see it in your list
/see_my_product_list - see your list: you can ask me about the price of each item
/help - see command list
/info - information about this bot
            ''')
    else:
        bot.send_message(message.chat.id, '''
            Список команд:
/shops - магазины, которые я поддерживаю
/add_product - добавить вещь в лист: скопируй ссылку на продукт с одного из поддерживаемых сайтов и отправь мне
/delete_product_fromlist - удалить продукт: я больше не буду следить за его ценой, ты не сможешь увидеть это в списке
/see_my_product_list - посмотреть мой лист: ты можешь спрашивать меня о цене вещи в текущий момент
/help - увидеть список команд
/info - информация о боте
                    ''')


@bot.message_handler(commands=['info'])
def info_function(message):
    bot.send_message(message.chat.id, '''
    
    ''')


@bot.message_handler(commands=['shops'])
def shops_function(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text='Ebay', callback_data='ebay', url="https://ebay.com"))
    keyboard.add(types.InlineKeyboardButton(text='Amazon', callback_data='amazon', url="https://amazon.com"))
    keyboard.add(
        types.InlineKeyboardButton(text='Aliexpress', callback_data='aliexpress', url="https://aliexpress.com"))
    keyboard.add(types.InlineKeyboardButton(text='Alibaba', callback_data='alibaba', url="https://alibaba.com"))
    keyboard.add(types.InlineKeyboardButton(text='Walmart', callback_data='walmart', url="https://walmart.com"))
    keyboard.add(types.InlineKeyboardButton(text='Asos', callback_data='asos', url="https://asos.com"))
    keyboard.add(types.InlineKeyboardButton(text='Macy\'s', callback_data='macys', url="https://macys.com"))
    keyboard.add(
        types.InlineKeyboardButton(text='Wildberries', callback_data='wildberries', url="https://wildberries.ru"))
    if cfg.lang_en:
        bot.send_message(message.chat.id, 'Shops, that I support (tap to open):', reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, 'Поддерживаемые магазины (нажмите чтобы перейти)', reply_markup=keyboard)


@bot.message_handler(commands=['add_product'])
def add_product_func(message):
    if cfg.lang_en:
        bot.send_message(message.chat.id, 'Copy product link and send it to me')
    else:
        bot.send_message(message.chat.id, 'Скопируй ссылку на товар и пришли мне')


@bot.message_handler(commands=['delete_product_fromlist'])
def delete_product_func(message):
    if cfg.lang_en:
        bot.send_message(message.chat.id, 'Copy product link and send it to me')
    else:
        bot.send_message(message.chat.id, 'Скопируй ссылку на товар и пришли мне')


@bot.message_handler(commands=['see_my_product_list'])
def see_list_func(message):
    if cfg.lang_en:
        bot.send_message(message.chat.id, 'Copy product link and send it to me')
    else:
        bot.send_message(message.chat.id, 'Скопируй ссылку на товар и пришли мне')


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "language_en":
        cfg.lang_en = True
        bot.send_message(call.message.chat.id, 'Hey, ' + '''
I am a bot for tracking discounts on items that you add here.
Follow the algorithm: copy the link to the item in the browser and send it to me.
And I will regularly track the price, warn about discounts, or just tell you about the current situation, if you ask.
It's simple, right? Try it!
P.s. to view functions press /help
''')
    elif call.data == "language_ru":
        cfg.lang_en = False
        bot.send_message(call.message.chat.id, 'Привет! ' + '''
Я - бот отслеживания скидок на вещи, которые ты сюда добавишь.
Алгоритм такой: копируй ссылку на вещь в браузере и присылай её мне.
А я буду регулярно отслеживать цену, предупрежу о скидках или просто расскажу про текущую ситуацию, если спросишь.
Всё просто, правда? Попробуй!
P.s. для просмотра функций нажми /help
            ''')

    types.ReplyKeyboardRemove()
    bot.send_sticker(call.message.chat.id, 'CAACAgUAAxkBAAMQX11FbdjpVkVv8octhdOtBk7BEgUAApADAALpCsgD7SkxFoHpn0cbBA')


@bot.message_handler(content_types='text')
def reply_text(message):
    if message.text == "english":
        cfg.lang_en = True
        bot.send_message(message.chat.id, 'Hey, ' + '''
I am a bot for tracking discounts on items that you add here.
Follow the algorithm: copy the link to the item in the browser and send it to me.
And I will regularly track the price, warn about discounts, or just tell you about the current situation, if you ask.
It's simple, right? Try it!
P.s. to view functions press /help
''')


bot.polling()
