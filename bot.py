import time
import telebot
import telegram
import random
from telegram import TelegramObject

TOKEN = "1322615277:AAH-GTPUfDVKF8Z0caF2vTrexJEPRcPl4o8"
bot = telebot.TeleBot(token=TOKEN)
          
class Dice(TelegramObject):
    """
    This object represents an animated emoji with a random value for currently supported base
    emoji. (The singular form of "dice" is "die". However, PTB mimics the Telegram API, which uses
    the term "dice".)
    Note:
        If :attr:`emoji` is "🎯", a value of 6 currently represents a bullseye, while a value of 1
        indicates that the dartboard was missed. However, this behaviour is undocumented and might
        be changed by Telegram.
        If :attr:`emoji` is "🏀", a value of 4 or 5 currently score a basket, while a value of 1 to
        3 indicates that the basket was missed. However, this behaviour is undocumented and might
        be changed by Telegram.
    Attributes:
        value (:obj:`int`): Value of the dice.
        emoji (:obj:`str`): Emoji on which the dice throw animation is based.
    Args:
        value (:obj:`int`): Value of the dice. 1-6 for dice and darts, 1-5 for basketball.
        emoji (:obj:`str`): Emoji on which the dice throw animation is based.
    """
    def __init__(self, value, emoji, **kwargs):
        self.value = value
        self.emoji = emoji

    @classmethod
    def de_json(cls, data, bot):
        if not data:
            return None

        return cls(**data)

    DICE = '🎲'
    """:obj:`str`: '🎲'"""
    DARTS = '🎯'
    """:obj:`str`: '🎯'"""
    BASKETBALL = '🏀'
    """:obj:`str`: '🏀'"""
    ALL_EMOJI = [DICE, DARTS, BASKETBALL]
    """List[:obj:`str`]: List of all supported base emoji. Currently :attr:`DICE`,
    :attr:`DARTS` and :attr:`BASKETBALL`."""
        
@bot.message_handler(commands=['start']) # welcome message handler
def send_welcome(message):
    bot.reply_to(message, '🎲 DiceRoll 🎲  👉 How to play? Add this bot in your favourite telegram group and lets roll your dice with your friends ! ')

@bot.message_handler(commands=['roll'])
def start(message):
        bot.reply_to(message, object('🎲'))


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

