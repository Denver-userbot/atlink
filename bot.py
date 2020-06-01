import time
import telebot

TOKEN = "874505396:AAEQZeIGzcGG3xqZdELzekFU01V1mNaCu6A"
bot = telebot.TeleBot(token=TOKEN)

def findat(msg):
    # from a list of texts, it finds the one with the '@' sign
    for i in msg:
        if '@' in i:
            return i

@bot.message_handler(commands=['start']) # welcome message handler
def send_welcome(message):
    bot.reply_to(message, 'Please type /register to add your account in our database!')

@bot.message_handler(func=lambda msg: msg.text is not None and '/getlink' in msg.text)
# lambda function finds messages with the '@' sign in them
# in case msg.text doesn't exist, the handler doesn't process it
def at_converter(message):
    texts = message.text.split()
    at_text = findat(texts)
    if at_text == '/getlink ': # in case it's just the '@', skip
        pass
    else:
        insta_link = "https://m.rivalregions.com/#slide/profile/{}".format(at_text[1:])
        bot.reply_to(message, insta_link)

while True:
    try:
        bot.polling(none_stop=True)
        # ConnectionError and ReadTimeout because of possible timout of the requests library
        # maybe there are others, therefore Exception
    except Exception:
        time.sleep(15)
