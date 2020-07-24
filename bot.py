import time
import telebot
import telegram
import random
from telegram import TelegramObject

TOKEN = "1392244952:AAG0UbsIJ7rDM-JjLE9XvGPeOi1YBMior5k"
bot = telebot.TeleBot(token=TOKEN)
          
        
@bot.message_handler(commands=['start']) # welcome message handler
def send_welcome(message):
    bot.reply_to(message, '🎲 DiceRoll 🎲  👉 How to play? Add this bot in your favourite telegram group and lets roll your dice with your friends ! ')

@bot.message_handler(commands=['roll'])
def start(message):
        bot.reply_to(message, random.randint(1,6))

@bot.message_handler(commands=['blackjack'])
def start(message):
        bot.reply_to(message, random.randint(1,10))


@bot.message_handler(func=lambda msg: msg.text is not None and '@' in msg.text)
# lambda function finds messages with the '@' sign in them
# in case msg.text doesn't exist, the handler doesn't process it
def at_converter(message):
    texts = message.text.split()
    at_text = findat(texts)
    if at_text == '@': # in case it's just the '@', skip
        pass
    else:
        insta_link = "https://instagram.com/{}".format(at_text[1:])
        bot.reply_to(message, insta_link)

while True:
    try:
        bot.polling(none_stop=True)
        # ConnectionError and ReadTimeout because of possible timout of the requests library
        # maybe there are others, therefore Exception
    except Exception:
        time.sleep(15)

