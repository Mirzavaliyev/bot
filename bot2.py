from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import Command
from aiogram import F
from aiogram.types.callback_query import CallbackQuery
import asyncio

API_TOKEN = "7840981516:AAGLqHiGM1A-95akL23g4tN_GXjyhMbIqXA"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

#Menu komandasi uchun handler
@dp.message(Command(commands=['menu']))
async def show_menu(message: types.Message):
    # Tugmacha yaratamiz
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Unit 1', callback_data="unit1")],
        [InlineKeyboardButton(text='Unit 2', callback_data='="unit2')]
    ])

    await message.answer('Bolimni tanlang', reply_markup=markup)

# Unit 1 uchun handler
@dp.callback_query(F.data == "unit1")
async def procces_unit1(callback: CallbackQuery):
    await callback.answer("Siz unit 1 tanladingiz")
    await callback.message.answer('Unit 1 haqida malumot')

#Unit 2 uchun handler
@dp.callback_query(F.data == "unit1")
async def procces_unit2(callback: CallbackQuery):
    await callback.answer("Siz unit 2 ni tanladngiz")
    await callback.message.answer("Unit 2 haqida malumot")

# Botni ishga tushurish
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
