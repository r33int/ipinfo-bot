import configparser
import telebot
import socket
import ipinfo

conf = configparser.ConfigParser()
bot = telebot.TeleBot("")

# Read config and set variables
conf.read('bot.cfg')
tgtoken = conf.get('Settings', 'telegram-api-token')
ipinfotoken = conf.get('Settings', 'ipinfo-api-token')

# Connect the bot to Telegram
bot = telebot.TeleBot(tgtoken)
print("Bot connected")

# /start, /help commands
@bot.message_handler(commands=['start', 'help'])
def command_welcome(message):
    bot.send_message(message.chat.id, 'Welcome to the ipinfo bot! To use me, all you have to do is to enter the command /ipinfo <ip address>, and I will give you all the info I got related to this IP address.')

# /source command
@bot.message_handler(commands=['source'])
def command_source(message):
    bot.send_message(message.chat.id, 'This software is fully open-source. Source code is available right there: https://github.com/r33int/ipinfo-bot')

def extract_arg(arg):
    return arg.split()[1:]

# WIP
@bot.message_handler(commands=['ipinfo'])
def command_ipinfo(message):
    status = extract_arg(message.text)
    statusstr = ''.join(str(e) for e in status)

    # Check if the IPv4 address is valid
    def is_valid_ipv4_address(address):
        try:
            socket.inet_pton(socket.AF_INET, address)
        except AttributeError:
            try:
                socket.inet_aton(address)
            except socket.error:
                return False
            return address.count('.') == 3
        except socket.error:
            return False

        return True

    if is_valid_ipv4_address(statusstr):
        print("yes")
        handler = ipinfo.getHandler(ipinfotoken)
        ip_address = (statusstr)
        details = handler.getDetails(ip_address)

        # store info into variables
        det-hostname = details.hostname
        det-city = details.city
        det-region = details.region
        det-country = details.country
        det-location = details.location
        det-postcode = details.postal
        # very dirty, must be cleaned
        bot.send_message(message.chat.id, '- IP info for ' + statusstr +': -\n' + '\nHostname: ' + det-hostname + '\nCity: ' + det-city + '\nRegion: ' + det-region + '\nCountry: ' + det-country + '\nLocation: ' + det-location + '\nPostcode: ' + det-postcode)
    else:
        bot.send_message(message.chat.id, 'This IP address is not valid.')

bot.polling(none_stop=1, interval=0, timeout=100000)