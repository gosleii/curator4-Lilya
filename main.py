import telebot

bot = telebot.TeleBot('6728339616:AAGJdhUxMEqfflRhVcAneCWyPJqTAIDY7vE')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Игры в Playstation Store', parse_mode='Markdown')


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id,
                     'Этот бот может помочь вам с поиском и покупкой игр в PlayStation Store. Просто введите /catalog для просмотра доступных игр, /search для поиска определенной игры, /цены для просмотра текущих цен, /discounts для просмотра текущих акций и /buy для покупки игры.',
                     parse_mode='Markdown')


@bot.message_handler(commands=['catalog'])
def main(message):
    bot.send_message(message.chat.id, '''Для покупки доступы следующие игры: 
Цена: 4299 рублей
Название игры: Marvel’s Spider-Man

Цена: 4999 рублей
Название игры: God of War

Цена: 4499 рублей
Название игры: The Last of Us Remastered

Цена: 2899 рублей
Название игры: Uncharted: The Nathan Drake Collection''', parse_mode='Markdown')


@bot.message_handler(commands=['buy'])
def main(message):
    bot.send_message(message.chat.id, 'Покупка удалась!', parse_mode='Markdown')


@bot.message_handler(commands=['search'])
def main(message):
    bot.send_message(message.chat.id, 'Введите название игры, чтобы найти её в каталоге:', parse_mode='Markdown')


bot.infinity_polling()