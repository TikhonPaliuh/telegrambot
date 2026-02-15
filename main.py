import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def main(message):
	bot.send_message(message.chat.id, "hello")
 
bot.polling(none_stop=True)
