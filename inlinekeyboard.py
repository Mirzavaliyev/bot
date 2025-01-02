from aiogram import Bot, Dispatcher, types, Router
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import Command
import asyncio

# Bot token
TOKEN = "7840981516:AAGLqHiGM1A-95akL23g4tN_GXjyhMbIqXA"

bot = Bot(token=TOKEN)
dp = Dispatcher()
router = Router()

# Creating Inline buttons
inline_markup = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Biz haqimizda", callback_data="about_us")],
    [InlineKeyboardButton(text="Web sayt", url="www.newday.uz")]
])

@router.message(Command(commands=["menu"]))
async def show_menu(message: types.Message):
    await message.reply("Quyidagilardan birini tanlang", reply_markup=inline_markup)

@router.callback_query(lambda callback: callback.data == "about_us" )
async def about_us(callback: types.CallbackQuery):
    await callback.answer()
    await bot.send_message(callback.from_user.id, "Salom biz botlar yaratamiz")

#Botni ishga tushurish
async def main():
    dp.include_router(router)
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())
