import telebot
import os
from dotenv import load_dotenv
from GIFSRCH import search_gif
from IMGSRCH import image_search
from telebot import types

load_dotenv("TOKENS.env")

TELEGRAM_API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')

print(TELEGRAM_API_TOKEN)

if TELEGRAM_API_TOKEN is None:
    print("Помилка: Не знайдено токен Telegram API у файлі .env")
    exit(1)  

bot = telebot.TeleBot(TELEGRAM_API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Привіт, в цьому боті ти зможеш знайти популярні зображення та GIF.')

@bot.message_handler(func=lambda message: True)
def handle_text(message):
    keyboard = types.InlineKeyboardMarkup()
    gif_button = types.InlineKeyboardButton("GIF", callback_data='gif')
    image_button = types.InlineKeyboardButton("Зображення", callback_data='image')
    keyboard.add(gif_button, image_button)
    bot.send_message(message.chat.id, "Виберіть тип пошуку:", reply_markup=keyboard)
    bot.user_data = {}
    bot.user_data[message.chat.id] = {'query': message.text}

@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    query = bot.user_data[call.message.chat.id]['query']
    if call.data == 'gif':
        gif_url = search_gif(query)
        if gif_url:
            bot.send_animation(call.message.chat.id, gif_url)
        else:
            bot.send_message(call.message.chat.id, "Нічого не знайдено.")
    elif call.data == 'image':
        image_url = image_search(query)
        if image_url:
            bot.send_photo(call.message.chat.id, image_url)
        else:
            bot.send_message(call.message.chat.id, "Нічого не знайдено.")
    bot.answer_callback_query(call.id)

if __name__ == '__main__':
    bot.polling(non_stop=True)
