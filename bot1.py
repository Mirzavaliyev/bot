import logging
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage

API_TOKEN = '7840981516:AAEqJNWYSMGXQT1sSgOaZHYCOgCyRkKBVG4'  # O'zingizning bot tokeningizni kiriting

logging.basicConfig(level=logging.INFO)

# Bot va Dispatcher obyektlarini yaratish
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()  # Bot xotirasi
dp = Dispatcher(bot, storage=storage)

# '/start' va '/help' komandalari uchun handler
@dp.message(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer("Salom! Men Telegram botman. Sizga qanday yordam bera olaman?")

# Har qanday xabarni qaytarish uchun handler
@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)

# Pollingni boshlash
if __name__ == '__main__':
    import asyncio
    asyncio.run(dp.start_polling(skip_updates=True))
