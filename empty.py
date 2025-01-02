from aiogram import Bot, Dispatcher, Router, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import Command
import asyncio

# Bot tokeni
API_TOKEN = "7840981516:AAGUstjxmAy935OAc-rS9nHuc2L0M0Ky6mg"

# Bot va Router obyektlari
bot = Bot(token=API_TOKEN)
dp = Dispatcher()
router = Router()

# Inline tugmachalarni yaratamiz
inline_markup = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Biz haqimizda", callback_data="about_us")],
    [InlineKeyboardButton(text="Veb-sayt", url="https://example.com")],
    [InlineKeyboardButton(text="Telegram kanal", url="https://t.me/online_english_learners")]
])

@message(Command(commands=["start"]))
async def say_hello(message: types.Message):
    await message.answer("Nima hizmat aka", reply_markup=inline_markup)


@router.message(Command(commands=['menu']))
async def show_menu(message: types.Message):
    await message.reply("Quyidagilardan birini tanlang:", reply_markup=inline_markup)

@router.callback_query(lambda callback: callback.data == "about_us")
async def about_us(callback: types.CallbackQuery):
    await callback.answer()
    await bot.send_message(callback.from_user.id, "Biz Telegram botlar yaratamiz!")



# Botni ishga tushirish
async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
