from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import Command
from aiogram import F
from aiogram.types.callback_query import CallbackQuery
import asyncio

API_TOKEN = "7840981516:AAGLqHiGM1A-95akL23g4tN_GXjyhMbIqXA"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Menu komandasi uchun handler
@dp.message(Command(commands=['menu']))
async def show_menu(message: types.Message):
    # Tugmachalar yaratamiz
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Unit 1", callback_data="unit1")],
        [InlineKeyboardButton(text="Unit 2", callback_data="unit2")]
    ])

    await message.answer("Iltimos, bo‘limni tanlang:", reply_markup=markup)

# Unit 1 uchun callback handler
@dp.callback_query(F.data == "unit1")
async def process_unit1(callback: CallbackQuery):
    await callback.answer("Siz Unit 1 ni tanladingiz.")
    await callback.message.answer("Unit 1 bo‘limi haqida ma'lumot.")

# Unit 2 uchun callback handler
@dp.callback_query(F.data == "unit2")
async def process_unit2(callback: CallbackQuery):
    await callback.answer("Siz Unit 2 ni tanladingiz.")
    await callback.message.answer("Unit 2 bo‘limi haqida ma'lumot.")

# Botni ishga tushirish
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
