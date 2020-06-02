import time
import telebot

TOKEN = "1236371364:AAGDTeEkbE-YomK0sF86qAFV8FepauKGdqE"
bot = telebot.TeleBot(token=TOKEN)

def izdvojiID(tekst):
    id = ''
    for i in tekst:
        if i.isnumeric():
            id += i
    return id



@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.type == "private":
        bot.reply_to(message, 'Hi, type /add to add your link in our db Use this format for add your profile /add + link, like this : /add https://m.rivalregions.com/#slide/profile/292833 "')

@bot.message_handler(commands=['add']) # register message handler
def send_welcome(message):
    if message.chat.type == "private":
        if 'rivalregions.com/#slide/profile' in message.text:
            id = izdvojiID(message.text)
            #dodajuFajl(id)
            bot.reply_to(message, 'Link added ! Dont forget to join the Channel: @enclave_mercenaries')
            bot.send_message(-1001425560791,id)
        else:
            bot.reply_to(message, 'Invalid format!')
            


@bot.message_handler(func=lambda msg: msg.text is not None and '@' in msg.text)
# lambda function finds messages with the '@' sign in them
# in case msg.text doesn't exist, the handler doesn't process it
def at_converter(message):
    texts = message.text.split()
    at_text = findat(texts)
    if at_text == '@': # in case it's just the '@', skip
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
