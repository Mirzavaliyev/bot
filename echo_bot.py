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

@dp.message(lambda message: message.text.lower() == "salom")
async def greet_user(message: types.Message):
    await message.reply("Salom! Qanday yordam bera olaman?")

RESPONSES = {
    "salom": "Salom! Qanday yordam bera olaman?",
    "hi": "Hi! How can I help you?",
    "hello": "Hello! Need assistance?",
    "assalomu alaykum": "Va alaykum assalom! Nima yordam kerak?",
    "nima gap": "Tinchlik o'zizdachi?",
    "qalaysiz": "Yaxshiman o'zingizchi"
}

@dp.message(lambda message: message.text.lower() in RESPONSES)
async def respond_to_greeting(message: types.Message):
    await message.reply(RESPONSES[message.text.lower()])



#Foydalanuvchiga javob beruvchi handler
@dp.message()
async def echo(message: types.Message):
    await message.answer(f"Siz {message.text} deb yozdingiz")
async def main():
    await dp.start_polling(bot)
if __name__ == '__main__':
    asyncio.run(main())