import time
import telebot

TOKEN = "874505396:AAEQZeIGzcGG3xqZdELzekFU01V1mNaCu6A"
bot = telebot.TeleBot(token=TOKEN)

def findat(msg):
    # from a list of texts, it finds the one with the '@' sign
    for i in msg:
        if '@' in i:
            return i

@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.type == "private":
        bot.reply_to(message, 'Hello, type /register to register your profile, eg "/register [your RR profile link here]"')

@bot.message_handler(commands=['register']) # register message handler
def send_welcome(message):
    if message.chat.type == "private":
        if 'rivalregions.com/#slide/profile' in message.text:
            id = izdvojiID(message.text)
            #dodajuFajl(id)
            bot.reply_to(message, 'Profile added to our register!')
            bot.send_message(-475614130,id)
        else:
            bot.reply_to(message, 'Wrong format! Type /register [your RR profile link here](without the brackets) like this /register https://rivalregions.com/#slide/profile/1234567')

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
