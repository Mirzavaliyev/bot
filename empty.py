from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command
from aiogram.types import Message
import asyncio

# Bot tokenini bu yerga kiriting
BOT_TOKEN = "SIZNING_BOT_TOKENINGIZ"

# Bot va Dispatcher obyektlarini yaratamiz
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
router = Router()

# /start komandasi uchun handler
@router.message(Command(commands=['start']))
async def send_welcome(message: Message):
    await message.reply("Salom! Men Aiogram 3.15.0 asosida ishlaydigan botman.")

# /help komandasi uchun handler
@router.message(Command(commands=['help']))
async def send_help(message: Message):
    await message.reply("Menga savol berishingiz yoki /start tugmasini bosishingiz mumkin.")

# Botni ishga tushirish
async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
