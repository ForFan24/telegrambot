import telebot
import requests
import json
from config import *

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


@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):
    base, sym, amount = message.text.split()
    r = requests.get(f"https://api.exchangeratesapi.io/latest?base={base}&symbols={sym}")
    resp = json.loads(r.content)
    new_price = resp['rates'][sym] * float(amount)
    bot.reply_to(message, f"Цена {amount} {base} в {sym} : {new_price}")


bot.polling()