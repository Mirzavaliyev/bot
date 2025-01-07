from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message

# Bot tokeningizni kiriting
BOT_TOKEN = "7938805460:AAG6wAty8qLllIPIsJaUlZRRsILuIyc-Hl4p"

# Bot va Dispatcher obyektini yaratamiz
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Oddiy handler: /start va /help komandalariga javob beradi
@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: Message):
    await message.answer("Salom! Men Aiogram asosidagi botman. 😊")

# Xabar kelganda javob qaytarish
@dp.message_handler()
async def echo(message: Message):
    await message.answer(message.text)

# Botni ishga tushirish
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
