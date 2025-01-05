from aiogram import Bot, Router, types
from aiogram.filters import Command, Text, Regexp
from aiogram.types import Message
from aiogram.utils.executor import start_polling

# Replace with your actual Bot Token
API_TOKEN = "YOUR_BOT_TOKEN"

# List to store group IDs
group_ids = []

# Regular expression for advertisement words
advertisement_words_regex = r"(sale|discount|offer|cheap|free|buy|sell)"

# Initialize bot and router
bot = Bot(token=API_TOKEN)
dp = Router()


# Handle /start command
@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        f"Welcome to {message.chat.title}!\n"
        f"Current members: {message.chat.get_members_count()}"
    )


# Handle new member join
@dp.message(content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def new_member(message: Message):
    new_member = message.new_chat_members[0]
    if new_member:
        await message.delete()  # Delete the "Join" message
        await message.answer(f"Welcome {new_member.first_name} to the group!")


# Handle member leave
@dp.message(content_types=types.ContentType.LEFT_CHAT_MEMBER)
async def member_left(message: Message):
    await message.delete()  # Delete the "Left" message


# Handle messages for advertisement word filtering
@dp.message(Regexp(advertisement_words_regex))
async def filter_messages(message: Message):
    await message.delete()


# Handle /send_ad command (only for admins)
@dp.message(Command("send_ad"))
async def send_ad(message: Message):
    if message.chat.type == 'private':
        ad_message = ' '.join(message.text.split()[1:])  # Get ad message from command
        if ad_message:
            for group_id in group_ids:
                try:
                    await bot.send_message(chat_id=group_id, text=ad_message)
                except Exception as e:
                    print(f"Error sending ad to group {group_id}: {e}")
        else:
            await message.answer("Please provide an advertisement message.")
    else:
        await message.answer("This command can only be used in private chat.")


# Get group ID when bot is added to a group
@dp.message(content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def get_group_id(message: Message):
    chat_id = message.chat.id
    if chat_id not in group_ids:
        group_ids.append(chat_id)
        print(f"Added group ID: {chat_id}")


if __name__ == '__main__':
    start_polling(dp, bot)