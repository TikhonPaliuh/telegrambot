import os
import telebot
from telebot import types


TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["profile"])
def site(message):
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton("Author's website", url="https://github.com/TikhonPaliuh"))
	bot.reply_to(message,"Author's website", reply_markup=markup)
 
@bot.message_handler(commands=["start"])
def main(message):
	bot.send_message(message.chat.id, "This bot is not very useful :), write /profile")

@bot.message_handler()
def info(message):
	bot.send_message(message.chat.id, f"hi {message.from_user.first_name}, write /start :) ")
		
 
bot.polling(none_stop=True)
