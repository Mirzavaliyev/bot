from aiogram import Bot, Dispatcher
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor  # Bu hozir kerak emas

API_TOKEN = 'Your_Telegram_Bot_API_Token'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Start command
@dp.message_handler(commands=['start'])
async def start(message: Message):
    await message.answer("Salom! Sevgi testiga xush kelibsiz! Davom etish uchun /test buyrug'ini bering.")

# Test command
@dp.message_handler(commands=['test'])
async def test(message: Message):
    await message.answer("Ismingizni kiriting:")
    await dp.current_state(user=message.from_user.id).set_state('waiting_for_name')

# Foydalanuvchi 1 uchun ma'lumotlarni olish
@dp.message_handler(state='waiting_for_name')
async def process_name_1(message: Message, state):
    async with state.proxy() as data:
        data['name'] = message.text
    await message.answer("Yoshingizni kiriting:")
    await dp.current_state(user=message.from_user.id).set_state('waiting_for_age')

@dp.message_handler(state='waiting_for_age')
async def process_age_1(message: Message, state):
    async with state.proxy() as data:
        data['age'] = message.text
    await message.answer("Qiziqishlaringizni yozing:")
    await dp.current_state(user=message.from_user.id).set_state('waiting_for_interest')

@dp.message_handler(state='waiting_for_interest')
async def process_interest_1(message: Message, state):
    async with state.proxy() as data:
        data['interest'] = message.text
    await message.answer("2-foydalanuvchi uchun link olasiz. Bu link orqali ular o'z javoblarini berishlari mumkin.")
    inline_keyboard = InlineKeyboardMarkup()
    inline_keyboard.add(InlineKeyboardButton(text="2-foydalanuvchi uchun tugma", callback_data="get_second_user_data"))
    await message.answer(f"Bu tugma orqali 2-foydalanuvchi botga kirishi mumkin: ", reply_markup=inline_keyboard)
    await dp.current_state(user=message.from_user.id).set_state('waiting_for_second_user_data')

# 2-foydalanuvchi ma'lumotlarini olish
@dp.callback_query_handler(text="get_second_user_data")
async def process_second_user_data(callback: types.CallbackQuery, state):
    second_user_id = callback.message.chat.id  # 2-foydalanuvchi ID
    await dp.current_state(user=second_user_id).set_state('waiting_for_name')
    await callback.answer("2-foydalanuvchi botga kirdi va javoblarni berish uchun tayyor.")

@dp.message_handler(state='waiting_for_name', user_id='waiting_for_second_user_data')
async def process_name_2(message: Message, state):
    async with state.proxy() as data:
        data['name'] = message.text
    await message.answer("Yoshingizni kiriting:")
    await dp.current_state(user=state.user.id).set_state('waiting_for_age')

@dp.message_handler(state='waiting_for_age', user_id='waiting_for_second_user_data')
async def compare_answers(message: Message, state):
    async with state.proxy() as second_user_data:
        await state.update_data(second_user=second_user_data)
    first_user_data = await state.get_data()
    second_user_data = await dp.current_state(user=second_user_data['id']).get_data()

    # Solishtirish va natijani chiqarish
    similarity = f"{first_user_data['name']} (Age: {first_user_data['age']}) bilan {second_user_data['name']} (Age: {second_user_data['age']}) moslik darajasi: TBD"
    await message.answer(similarity)

if __name__ == '__main__':
    dp.run_polling()  # run_polling ishlatiladi
