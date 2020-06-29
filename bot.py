import time
import telebot

TOKEN = "1277928698:AAGTxjacvBoQ33ouKEiTJoVv9F8b454GJyM"
bot = telebot.TeleBot(token=TOKEN)

def izdvojiID(tekst):
    id = ''
    for i in tekst:
        if i.isnumeric():
            id += i
    return id



@bot.message_handler(commands=['roll'])
def start(message):
    if message.chat.type == "private":
        bot.sendMessage(chat_id,random.randint(1,6),reply_to_message_id=msg['message_id'])

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
