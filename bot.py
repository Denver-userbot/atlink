import os

from flask import Flask, request

import telebot

TOKEN = "1628306242:AAHk0d_JNtXqc7wAqeRrRs0eb3g9mVtqle0"
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

def izdvojiID(tekst):
    id = ''
    for i in tekst:
        if i.isnumeric():
            id += i
    return id


@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.type == "private":
        bot.reply_to(message, 'Hello This bot is to collect links for [@rrbroadcast_bot]\n, type /register to register your profile, eg "/register [your RR profile link here]\n -<i>A property of Antares Foundatio</i>"')

@bot.message_handler(commands=['register']) # register message handler
def send_welcome(message):
    if message.chat.type == "private":
        if 'rivalregions.com/#slide/profile' in message.text:
            id = izdvojiID(message.text)
            #dodajuFajl(id)
            bot.reply_to(message, 'Link added succesfully!')
            bot.send_message(935046373,id)
        else:
            bot.reply_to(message, 'Wrong format! Type /register [your RR profile link here](without the brackets) like this /register https://rivalregions.com/#slide/profile/1234567')




@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://pacific-hollows-01627.herokuapp.com/' + TOKEN)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
