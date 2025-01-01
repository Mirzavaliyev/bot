from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
import asyncio

BOT_TOKEN = "SIZNING_BOT_TOKENINGIZ"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Tugmachalarni yaratamiz
reply_markup = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton("Salom")
button2 = KeyboardButton("Yordam")
button3 = KeyboardButton("Qo'shimcha ma'lumot")
reply_markup.add(button1, button2, button3)

@dp.message(Command(commands=['start']))
async def send_welcome(message: types.Message):
    await message.reply("Xush kelibsiz! Tugmalardan birini tanlang:", reply_markup=reply_markup)

@dp.message(lambda message: message.text == "Salom")
async def say_hello(message: types.Message):
    await message.reply("Salom! Qanday yordam bera olaman?")

@dp.message(lambda message: message.text == "Yordam")
async def provide_help(message: types.Message):
    await message.reply("Men sizga yordam bera olaman. Savollaringizni yuboring!")

@dp.message(lambda message: message.text == "Qo'shimcha ma'lumot")
async def additional_info(message: types.Message):
    await message.reply("Bu bot Aiogram asosida ishlaydi va Telegram uchun mo‘ljallangan.")

# Botni ishga tushirish uchun asyncio.run ishlatamiz
async def main():
    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main())
