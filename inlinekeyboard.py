from aiogram import Bot, Dispatcher
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
import asyncio

BOT_TOKEN = "7938805460:AAFi1Y-4PMpRmzednEqPwf4Va7ZCfrEtq_Q"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Reply Keyboardni yaratamiz
@dp.message(Command(commands=["start"]))
async def start_handler(message: Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Salom")],
            [KeyboardButton(text="Qanday ahvolda?")],
            [KeyboardButton(text="Rahmat!")],
        ],
        resize_keyboard=True  # Tugmalarni ekranga moslash uchun
    )
    await message.answer("Quyidagi tugmalardan birini tanlang:", reply_markup=keyboard)

# Tugma bosilganda javob
@dp.message()
async def reply_handler(message: Message):
    if message.text == "Salom":
        await message.answer("Va alaykum assalom!")
    elif message.text == "Qanday ahvolda?":
        await message.answer("Yaxshi, sizda-chi?")
    elif message.text == "Rahmat!":
        await message.answer("Arzimaydi! 😊")
    else:
        await message.answer("Meni tushunmadim. Tugmalardan birini tanlang.")

async def main():
    print("Bot ishga tushmoqda...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
