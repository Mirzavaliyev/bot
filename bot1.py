from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

from echo_bot import TOKEN
from inlinekeyboard import user_data, reply_markup, handle_choice

# Bot  token
TOKEN = "7938805460:AAG6wAty8qLllIPIsJaUlZRRsILuIyc-Hl4"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Foydalanuvchilar lugatini saqlash uchun lug'at
user_data = {}

reply_markup = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton("Python darslari")
button2 = KeyboardButton("Ingliz tili darslari")
button3 = KeyboardButton("Huquq fani darslari")
reply_markup.add(button1, button2, button3)

# Start buyrug'i handleri
@dp.message(commands=["start"])
async def send_welcome(message: Message):
    await message.reply("Xush kelibsiz ", reply_markup=reply_markup)

# Tugmalarni bosish uchun handler
@dp.message(F.text.in_({"Python darslari", "Ingliz tili darslari", "Huquq fani darslari"}))
async def handle_choice(message: Message):
    #Foydalanuvchi tanlovini korsatish
    user_data[message.from_user.id] = message.txt
    await message.reply("Tanlovingiz saqlandi", {message.text})

# My choice buyrug'i handleri
@dp.message(commmands=['mychoice'])
async def show_choice(message: Message):
    # Foydalanuvchi tanlovini korsatish
    choice = user_data.get(message.from_user.id, "Hech narsa tanlanmagan")
    await message.reply(f"Sizning tanlovingiz {choice}")

# botni ishga tushurish
async def main():
    print("Bot ishlamoqda...")
    dp.include_router(dp)
    await dp.start_polling(bot)
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())