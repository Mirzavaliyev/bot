from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import StatesGroup, State
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import Command
import asyncio

API_TOKEN = "7938805460:AAFi1Y-4PMpRmzednEqPwf4Va7ZCfrEtq_Q"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# Holatlar (States)
class TestStates(StatesGroup):
    waiting_for_user1_question = State()
    waiting_for_user2_question = State()

# Ma'lumotlar
users_data = {}
questions = [
    "<b>1-savol: Bo'sh vaqtingizda nimani afzal ko'rasiz?</b>\nA) Tinch dam olish, kitob o‘qish yoki uyda bo‘lish.\nB) Do‘stlar bilan ko‘ngilxushlik qilish yoki sarguzashtlarga chiqish.",
    "<b>2-savol: Qanday filmlar ko‘proq yoqadi?</b>\nA) Romantik yoki dramatik filmlar.\nB) Triller, jangari yoki ilmiy-fantastik filmlar.",
    "<b>3-savol: Pulni qanday sarflaysiz?</b>\nA) Rejaga muvofiq, tejab-tergab.\nB) O‘sha lahzani zavq bilan o‘tkazishga sarflash.",
    "<b>4-savol: Muloqotda siz uchun nima muhim?</b>\nA) His-tuyg‘ularni muhokama qilish va chuqur suhbatlar.\nB) Kulgu va yengil, qiziqarli suhbatlar.",
    "<b>5-savol: Sayohat qilishda qaysi uslubni tanlaysiz?</b>\nA) Oldindan rejalashtirilgan va tinch dam olish.\nB) Tasodifiy va sarguzashtlarga boy sayohat.",
    "<b>6-savol: Xatolar uchun kechirishni qanchalik oson qabul qilasiz?</b>\nA) Xatolarni uzoq vaqt yodda saqlayman, lekin kechirishga harakat qilaman.\nB) Tez kechiraman va kelajakka qarab harakat qilaman.",
    "<b>7-savol: Qaysi biri sizni xursand qiladi?</b>\nA) Juftingizning kichik, samimiy e'tiborlari (xabar, sovg‘a).\nB) Katta bayramlar yoki maxsus tadbirlar.",
    "<b>8-savol: Ixtilof yuz berganda nima qilasiz?</b>\nA) Gaplashmasdan oldin vaziyatni tinchlantirishga vaqt kerak.\nB) Muammoni darhol hal qilishga harakat qilaman.",
    "<b>9-savol: Ijtimoiy hayot haqida fikringiz qanday?</b>\nA) Kamroq odamlar bilan yaqin bo‘lishni afzal ko'raman.\nB) Ko'p odamlar bilan muloqotda bo'lishni yoqtiraman.",
    "<b>10-savol: Kelajakka bo'lgan qarashingiz qanday?</b>\nA) Barqaror hayot va oilaga e'tibor qaratish.\nB) Tajriba qilish va katta maqsadlarni amalga oshirish."
]

# Start komandasi
@dp.message(Command(commands=['start']))
async def start(message: Message, state: FSMContext):
    if len(message.text.split()) > 1:  # Ikkinchi foydalanuvchi link orqali kirsa
        first_user_id = int(message.text.split()[1])
        if first_user_id in users_data:
            users_data[message.from_user.id] = {'first_user_id': first_user_id, 'answers': []}
            await message.answer("Sevgi testiga hush kelibsiz. Savollarga javob bering!", parse_mode='HTML')

            # Birinchi savol
            keyboard = InlineKeyboardBuilder()
            keyboard.button(text="Variant A", callback_data="q1_a")
            keyboard.button(text="Variant B", callback_data="q1_b")
            keyboard = keyboard.as_markup()
            await message.answer(questions[0], reply_markup=keyboard, parse_mode='HTML')
            await state.set_state(TestStates.waiting_for_user2_question)
        else:
            await message.answer("Kechirasiz, ushbu link noto‘g‘ri yoki muddati o‘tgan.", parse_mode='HTML')
    else:  # Birinchi foydalanuvchi
        users_data[message.from_user.id] = {'answers': []}
        await message.answer("Salom! Savollarga javob berishni boshlash uchun tayyor bo'ling!", parse_mode='HTML')

        # Birinchi savol uchun tugmalar
        keyboard = InlineKeyboardBuilder()
        keyboard.button(text="Variant A", callback_data="q1_a")
        keyboard.button(text="Variant B", callback_data="q1_b")
        keyboard = keyboard.as_markup()
        await message.answer(questions[0], reply_markup=keyboard, parse_mode='HTML')
        await state.set_state(TestStates.waiting_for_user1_question)

# Birinchi foydalanuvchi savollari
@dp.callback_query(TestStates.waiting_for_user1_question)
async def user1_questions(callback: CallbackQuery, state: FSMContext):
    user_id = callback.from_user.id
    users_data[user_id]['answers'].append(callback.data)

    # Agar barcha savollar tugagan bo‘lsa
    if len(users_data[user_id]['answers']) == len(questions):
        link = f"https://t.me/{(await bot.me()).username}?start={user_id}"
        await callback.message.answer(f"Javoblaringiz qabul qilindi! Endi ushbu linkni ikkinchi foydalanuvchiga yuboring: {link}", parse_mode='HTML')
        await state.clear()
    else:
        # Navbatdagi savolni yuborish
        current_question_index = len(users_data[user_id]['answers'])
        keyboard = InlineKeyboardBuilder()
        keyboard.button(text="Variant A", callback_data=f"q{current_question_index+1}_a")
        keyboard.button(text="Variant B", callback_data=f"q{current_question_index+1}_b")
        keyboard = keyboard.as_markup()
        await callback.message.answer(questions[current_question_index], reply_markup=keyboard, parse_mode='HTML')

# Ikkinchi foydalanuvchi savollari
@dp.callback_query(TestStates.waiting_for_user2_question)
async def user2_questions(callback: CallbackQuery, state: FSMContext):
    user_id = callback.from_user.id
    users_data[user_id]['answers'].append(callback.data)

    # Agar barcha savollar tugagan bo‘lsa
    if len(users_data[user_id]['answers']) == len(questions):
        first_user_id = users_data[user_id]['first_user_id']
        first_user_answers = users_data[first_user_id]['answers']
        second_user_answers = users_data[user_id]['answers']

        # Javoblarni solishtirish
        similarity = 0
        for i in range(len(questions)):
            if first_user_answers[i] == second_user_answers[i]:
                similarity += 10  # Har bir mos javob 10%

        await callback.message.answer(f"Sizlar bir birlaringizga {similarity}% mos kelasiz baxtli bo'ling!!", parse_mode='HTML')
        await state.clear()
    else:
        # Navbatdagi savolni yuborish
        current_question_index = len(users_data[user_id]['answers'])
        keyboard = InlineKeyboardBuilder()
        keyboard.button(text="Variant A", callback_data=f"q{current_question_index+1}_a")
        keyboard.button(text="Variant B", callback_data=f"q{current_question_index+1}_b")
        keyboard = keyboard.as_markup()
        await callback.message.answer(questions[current_question_index], reply_markup=keyboard, parse_mode='HTML')

# Botni ishga tushirish
if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))
