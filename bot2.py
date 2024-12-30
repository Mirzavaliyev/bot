from aiogram Bot, Dispatcher, executor, types
# Bot tokenini ulash
TOKEN = 'Bot token'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
# Start kommandasi uchun hander
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply('Salom qaanday yordam kerak')
# /help komandasi uchun hamdler
@dp.message_handler(command=['help'])
async def send_help(message: types.Message)
    await message.reply('Salom bu qanday yordam bera olaman')
# Botni ishga tushurish
if __name__ == '__name__':
    executor.start_polling(dp,skip_updates=True)
