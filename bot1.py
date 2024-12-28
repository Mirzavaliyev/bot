import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.loggers import dispatcher

API_TOKEN = 'BOT TOKENI'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start','help'])
async def send_welcome(message: types.Message):
