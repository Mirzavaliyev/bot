from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
import asyncio

BOT_TOKEN = "7840981516:AAGLqHiGM1A-95akL23g4tN_GXjyhMbIqXA"  # O'zingizning tokeningizni kiriting

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Tugmachalarni to'g'ri formatda yaratamiz
reply_markup = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Salom")],
        [KeyboardButton(text="Yordam")],
        [KeyboardButton(text="Qo'shimcha ma'lumot")],
    ],
    resize_keyboard=True,  # Klaviatura o'lchamini moslashtirish
)

@dp.message(Command("start"))
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

# Botni ishga tushirish
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
