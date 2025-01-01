from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
import asyncio

from pyexpat.errors import messages

from empty import reply_markup, button1
from main import API_TOKEN

API_TOKEN = "YOUR BOT TOKEN"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Creating bot button
reply_markup = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton('Salom')
button2 = KeyboardButton('Yordam')
button3 = KeyboardButton('Qoshimcha malumot')
reply_markup.add(button1, button2, button3)

@dp.message(Command(commands=["start"]))
async  def welcome_send(message: types.Message):
    await message.reply("Salom hush kelibsiz tugmachalardan birini tanlang", reply_markup=reply_markup)

@dp.message(lambda message: message.text == "Salom")
async def say_hello(message: types.Message):
    await message.reply("Salom qanday yordam bera olaman")

@dp.message(Command(command=["Yordam"]))
async def probide_help(message: types.Message):
    await message.reply_poll("Sizga qanday yordam bera olaman")




