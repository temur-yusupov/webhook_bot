# This code is built in the pyTelegramBotAPI library to set a webhook using Flask.

import telebot
from flask import Flask, request

TOKEN = '123:ABC'
bot = telebot.TeleBot(TOKEN, threaded=False)
app = Flask(__name__)

@app.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode('UTF-8'))])
    return ''

@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://example.com/" + TOKEN)
    return ''

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello")

@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.reply_to(message, message.text)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000)