from aiogram import Bot, Dispatcher
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.filters import Command
import asyncio

#Bot token
TOKEN = "YOUR TOKEN"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Start handler
@dp.message(Command(commands="start"))
async def send_welcome(message: Message):
    await message.answer("Salom botga hush kelibsiz")
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Birinchi tugma", callback_data="button1")],
            [InlineKeyboardButton(text="Ikkinchi tugma", callback_data="button2")]
        ]
    )
    await message.answer()
@dp.callback_query()
async def callback_query(callback: CallbackQuery):
    if callback.data == "button1":
        await callback.message.answer("Siz 1 ni tanladingiz ")
    elif callback.data == "button2":
        await callback.message.answer("Siz ikkini taladiz")
    await callback.answer()

async def main():
    print("Bot ishga tushyapti")
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())


