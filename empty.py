from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio

from inlinekeyboard import BOT_TOKEN

#Connecting api token
BOT_TOKEN = 'YOUR TOKEN '
ADMIN_ID = 123456778
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage()

#FSM uchun qator
class Form(StatesGroup):
    name = State()
    surname = State()
    feedback = State()
# Start komandasi uchun handler
@dp.message(Command(commands=["start",["help"]]))
async def send_welcome(message: Message, state: FSMContext):
    await message.answer("Salom ismingizni kiriting")
    await state.set_state(Form.name)
#Ism bilan ishlash
@dp.message(Form.name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Familyangizni kiriting")
    await state.set_state(Form.surname)

# Familiyani qayta ishlash
@dp.message(Form.surname)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(surname=message.text)
    await message.answer("Bot haqida yozib keting")
    await state.set_state(Form.feedback)

#Feedback qismini qayta ishlash
