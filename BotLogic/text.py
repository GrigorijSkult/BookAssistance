import telebot
#from telebot import types
from bs4 import BeautifulSoup
import requests
import text

#https://www.youtube.com/watch?v=HodO2eBEz_8
#https://www.youtube.com/watch?v=a0VVDMGwS0k&list=PL0lO_mIqDDFUdlTc097-1A9IBchtJEggp&index=2
# https://towardsdatascience.com/how-to-collect-data-from-any-website-cb8fad9e9ec5 - enter the web data

bot = telebot.TeleBot('5504177687:AAFQbIHAhbJzgSU1ZT1jJNSH-JLy7rnF0L4')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name}!</b>'
    bot.send_message(message.chat.id, mess)

def buy_one_book(message):
    bot.send_message(message.chat.id, "TBD - one book", parse_mode='html')


@bot.message_handler(commands=['buy_book'])
def buy_one_book(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Buy", url="www.google.com"))
    bot.send_message(message.chat.id, "TBD - one book", parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['help'])
def buy_one_book(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    start = types.KeyboardButton('Start')
    buy = types.KeyboardButton('Buy one book')

    markup.add(start, buy)
    bot.send_message(message.chat.id, "TBD - one book", parse_mode='html', reply_markup=markup)

# @bot.message_handler(content_types=['text'])
# def get_user_text(message):
#     if message.text == "id":
#         a = 'слышал что ' + str(message.from_user.first_name) + ' под номером ' + str(message.from_user.id) +' пидр...'
#         bot.send_message(message.chat.id, a, parse_mode='html')
#     else:
#         bot.send_message(message.chat.id, "Not understand", parse_mode='html')


bot.polling(none_stop=True)
