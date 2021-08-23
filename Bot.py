import telebot
from telebot.types import Message
import wikipedia

wikipedia.set_lang("uz")
bot  = telebot.TeleBot("1944710014:AAE61RR8Hezjj3irPgPMgj2kHBNzit2qcag")
@bot.message_handler(commands=['start'])

def start(message):
    bot.send_message(message.chat.id, 'Salom')


@bot.message_handler(content_types=['text'])
def text(message):
    final = message.text
    try:
        matn = wikipedia.summary(final)

        bot.send_message(message.chat.id, matn)

    except:
        bot.send_message(message.chat.id, 'Error')

bot.polling()