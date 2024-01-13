from telebot import TeleBot
from flask import Flask, request
from telebot.types import Update

TOKEN = '123:ABC'
bot = TeleBot(TOKEN, threaded=False)
app = Flask(__name__)

@app.route('/' + TOKEN, methods=['POST'])
def getMessage():
    update = Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])
    return 'ok', 200

@app.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://example.com/' + TOKEN)
    return 'ok', 200

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hi!")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000)