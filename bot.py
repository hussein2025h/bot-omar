import telebot
import datetime
import os

TOKEN = os.environ.get("5479451736:AAEdA5vB2dtxTWa9psPlv767Ingcpw_FA9U") 

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 مرحباً! أرسل تاريخ ميلادك بصيغة YYYY-MM-DD لحساب عمرك.")

@bot.message_handler(func=lambda m: True)
def calculate_age(message):
    try:
        birth_date = datetime.datetime.strptime(message.text, "%Y-%m-%d").date()
        today = datetime.date.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        bot.reply_to(message, f"🎂 عمرك هو: {age} سنة")
    except:
        bot.reply_to(message, "⚠️ الرجاء إرسال التاريخ بصيغة صحيحة: YYYY-MM-DD")

bot.polling()
