from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import Command
from aiogram.types import Message
import asyncio

from main import API_TOKEN

# connect bot token
API_TOKEN = "Your bot token"
bot = Bot(token=API_TOKEN)
dp = Dispatcher()
router = Router()

@router.message(Command(commands=["start"]))
async def send_welcome(message: Message):
    await message.reply("Salom men kuchli dasturchii tomonidan yozilgan botman")


