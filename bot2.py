from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import Command
from aiogram import F
from aiogram.types.callback_query import CallbackQuery
import asyncio


API_TOKEN = "yOUR BOT TOKEN"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
# Menu for handler command

@dp.message(Command(commands=['menu']))
async def show_menu(message: types.Message):
    # Creating buttons
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Unit 1', callback_data='unit1')],
        [InlineKeyboardButton(text='Unit 2', callback_data='unit2')]
    ])
    await message.answer('O\'zingizga yoqqan bo\'limni tanlang', reply_markup=markup)
# Unit 1 uchun handler




