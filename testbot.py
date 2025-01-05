from aiogram import Dispatcher, Bot, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from telegram import ReplyKeyboardMarkup

from echo_bot import TOKEN
from inlinekeyboard import user_data, reply_markup

# Bot  token
TOKEN = "Your bot token"

bot = Bot(token=TOKEN)

# Foydalanuvchilar lugatini saqlash uchun lug'at
user_data = {}

reply_markup = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton("Python darslari")
button2 = KeyboardButton("Ingliz tili darslari")
button3 = KeyboardButton("Huquq fani darslari")
reply_markup.add(button1, button2, button3)

# Start buyrug'i handleri
@dp.message(commands=["start"])