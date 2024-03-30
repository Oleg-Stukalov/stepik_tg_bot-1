# 7.1.6-echobot-universal+send_copy

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
import pprint

# Instead of BOT TOKEN HERE copy your bot token,
# from @BotFather
BOT_TOKEN = '6468393428:AAHH9wSFOiVIpE3ba1uHurJKM1dBhb9_HfA'

# Create Bot and Dispatcher instances
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# This handler will handle "/start" command
@dp.message(Command(commands='start'))
async def process_start_command(message: Message):
    await message.answer('Hello!\nMy name is Echo-bot!\nPlease, write or send me something')


# This handler will handle "/help" command
@dp.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer('Write or send me something and i will send your message to you')


# This handler will handle ANY messages
@dp.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text='This message type is not supported by send_copy method')


if __name__ == '__main__':
    dp.run_polling(bot)
