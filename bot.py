import telepot
from telepot.loop import MessageLoop
import time
import random
from techlib import *

token = '1277928698:AAGTxjacvBoQ33ouKEiTJoVv9F8b454GJyM' #Token del bot ottenuto da t.me/botfather
repository = 'https://github.com/Davide-Leone/dicebot' #Link al codice sorgente del programma. Se il codice sorgente viene modificato bisogna cambiare questo indirizzo.

#-- BOT -- Inizio vero e proprio del bot
def gestisci(msg):
    chat_id = msg['chat']['id']
    lan = parole(msg['from']['language_code'])[0] #Estrae il valore relativo alla lingua dell'utente
    if lan != 'en' and lan != 'it': #Supporta unicamente italiano ed inglese
        lan = 'en' 
    if list(msg.keys())[-2] == 'text': #Il bot ha ricevuto un comando testuale
        command = msg['text'].lower()
        if estrai(command,-len(username)) == username: #Nei gruppi i comandi sono nella forma /comando@username; questa parte trasforma il comando in /comando
            command = estrai(command,len(command)-len(username))
        if command == '/start' or command == '/help': #Messaggio di benvenuto/aiuto
            if lan == 'it':
                message = """Benvenuto!
Posso aiutarti a lanciare dadi a sei facce.
Per lanciare un dado usa /roll.
Puoi anche aggiungere il bot ad un gruppo per utilizzarlo lì.
\nDistribuito sotto licenza AGPL, questo bot è software libero senza garanzia.
Per info sulla licenza usa /license."""
            if lan == 'en':
                message = """Hi, I can help you rolling a dice.
You have only to use /roll and I'll tell you the result.
You can also add me in a group!
\nThis bot is free software with no warranty, distributed under AGPL license.
You can learn more about the license using /license."""
            bot.sendMessage(chat_id,message,reply_to_message_id=msg['message_id'])
        elif command == '/roll':
            bot.sendMessage(chat_id,random.randint(1,6),reply_to_message_id=msg['message_id']) #Genera un numero da 1 a 6 e lo invia all'utente
        elif command == '/license':
            if lan == 'it':
                message = "Distribuito sotto licenza [Affero GPL](https://www.gnu.org/licenses/). Puoi scaricare il file sorgente del bot a: "+repository
            if lan == 'en':
                message = "Licensed under [Affero GPL license](https://www.gnu.org/licenses/). You can download a copy of the bot's code at: "+repository
    else: #Non è un comando testuale
        if list(msg.keys())[-1] == "new_chat_members": #Il bot è stato aggiunto ad un gruppo
            if msg['new_chat_member']['id'] == bot_id: 
                if lan == 'it':
                    message = "Grazie per avermi aggiunto al gruppo!\nPotete usare /roll per lanciare un dado a sei facce."
                if lan == 'en':
                    message = "Happy to be here!.\nYou can use /roll to roll a dice."
                bot.sendMessage(chat_id,message,reply_to_message_id=msg['message_id'])

#-- Bot's definition -- Costruzione del bot e connessione a Telegram
bot = telepot.Bot(token) #Definizione del bot
#Applico qui le richieste getMe per non doverle eseguire ad ogni messaggio ricevuto
username = '@'+bot.getMe()['username'] #Username del bot
bot_id = bot.getMe()['id'] #ID del bot
MessageLoop(bot,gestisci).run_as_thread() #Riceve i messaggi
while 1:
    time.sleep(5) #Tiene il bot attivo
