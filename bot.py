import time
import telebot
import random

TOKEN = "1322615277:AAH-GTPUfDVKF8Z0caF2vTrexJEPRcPl4o8"
bot = telebot.TeleBot(token=TOKEN)
          
def __init__(self, value, emoji, **kwargs):
        self.value = value
        self.emoji = emoji

    DICE = '🎲'
    """:obj:`str`: '🎲'"""
    DARTS = '🎯'
    """:obj:`str`: '🎯'"""
    BASKETBALL = '🏀'
    """:obj:`str`: '🏀'"""
    ALL_EMOJI = [DICE, DARTS, BASKETBALL]
        
@bot.message_handler(commands=['start']) # welcome message handler
def send_welcome(message):
    bot.reply_to(message, 'Type /roll for roll the dice ! ')

@bot.message_handler(commands=['roll'])
def start(message):
        bot.reply_to(message, DICE = '🎲')


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

