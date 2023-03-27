import telebot

exchanges = {
    'доллар': 'USD',
    'евро': 'EUR',
    'рубль': 'RUB'
}
TOKEN = '5734596114:AAFR5qMVJ6x2jG1RJBncW52IOw0k2yaAMP4'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите комманду боту в следующем формате:\n<имя валюты> \
<в какую валюту перевести> \
<количество переводимой валюты>\nУвидить список всех доступных валют: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for i in exchanges.keys():
        text = '\n'.join((text, i))
    bot.reply_to(message, text)


bot.polling()