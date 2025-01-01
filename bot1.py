from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio

BOT_TOKEN = "SIZNING_BOT_TOKENINGIZ"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# /start buyrug'i uchun handler
@dp.message(Command(commands=["start"]))
async def send_welcome(message: types.Message):
    await message.answer("Salom! Men Aiogram 3.x asosida ishlaydigan botman.")

# /help buyrug'i uchun handler
@dp.message(Command(commands=["help"]))
async def send_help(message: types.Message):
    await message.answer("Menga savol berishingiz yoki /start tugmasini bosishingiz mumkin.")

# Foydalanuvchi yuborgan matnga javob beruvchi handler
@dp.message()
async def echo_message(message: types.Message):
    await message.answer(f"Siz yozdingiz: {message.text}")

# Botni ishga tushirish
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
