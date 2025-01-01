from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio

TOKEN = "7840981516:AAGLqHiGM1A-95akL23g4tN_GXjyhMbIqXA"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Start buyurugi uchun handler
@dp.message(Command(commands=['start']))
async def welcome_send(message: types.Message):
    await message.answer("Salom to\'ti botga hush kelibsiz bot gaplaringizni qaytaradi")

#Help buyrugi uuchun handler
@dp.message(Command(commands=['help']))
async def help(message: types.Message):
    await message.answer("Salom sizga qanday yordam bera olaman?")

#Help buyrugi uuchun handler
@dp.message(Command(commands=['hel']))
async def help1(message: types.Message):
    await message.answer("Salom sizga qanday olaman?")

#Foydalanuvchiga javob beruvchi handler
@dp.message()
async def echo(message: types.Message):
    await message.answer(f"Siz {message.text} deb yozdingiz")
async def main():
    await dp.start_polling(bot)
if __name__ == '__main__':
    asyncio.run(main())