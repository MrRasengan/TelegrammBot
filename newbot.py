import telebot
from random import *
import json
import requests
films = []
API_URL = 'https://7012.deeppavlov.ai/model'

API_TOKEN ='6489740213:AAEXAGVRLcQ1hm9AgKkvmQnYODEGj1mxwuw'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    films.append("Матрица")
    films.append("Солярис")
    films.append("Властелин колец")
    films.append("Техаччкая резня бензопилой")
    films.append("Санта Барбара")
    bot.send_message(message.chat.id,"Фильмы выгружены")

@bot.message_handler(commands=['all'])
def show_all(message):
    try:
        bot.send_message(message.chat.id,"Вот список всех фильмов")
        bot.send_message(message.chat.id,", " .join(films))
    except:
        bot.send_message(message.chat.id,"Фильмотека пустая")

@bot.message_handler(commands=['save'])
def save_all(message):
    with open("films.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(films, ensure_ascii=False))
        bot.send_message(message.chat.id,"Фильмотека сохранена в файле films.json")

@bot.message_handler(commands=['wiki'])
def wiki(message):
    quest = message.text.split()[1:]
    qq = " ".join(quest)
    data = {'question_raw': [qq]}
    try:
        res = requests.post(API_URL,json=data,verify=False).json()
        bot.send_message(message.chat.id, res)
    except:
        bot.send_message(message.chat.id,"Что-то я ничего не нашёл")


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if "привет" in message.text.lower():
        bot.send_message(message.chat.id, "Здарова")
    if "дела" in message.text.lower():
        bot.send_message(message.chat.id, "Дела нормально, сам как?")
    if "нормально" in message.text.lower():
        bot.send_message(message.chat.id, "Круто рад за тебя!")



bot.polling()