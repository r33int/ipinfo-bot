import configparser
import telebot

conf = configparser.ConfigParser()
bot = telebot.TeleBot("")

# Read config and set variables
conf.read('bot.cfg')
tgtoken = conf.get('Settings', 'telegram-api-token')
ipinfotoken = conf.get('Settings', 'ipinfo-api-token')

# Connect the bot to Telegram
bot = telebot.TeleBot(tgtoken)
print("Bot connected")

@bot.message_handler(commands=['start', 'help'])
def welcome(message):
    bot.send_message(message.chat.id, 'Welcome to the ipinfo bot! To use me, all you have to do is to enter the command /ipinfo <ip address>, and I will give you all the info I got related to this IP address.')

bot.polling(none_stop=1, interval=0, timeout=100000)