# 7.1.4-echobot-universal+photo

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
async def process_start_command(message: Message):
    await message.answer('Hello!\nMy name is Echo-bot!\nPlease, write or send me something')


# This handler will handle "/help" command
async def process_help_command(message: Message):
    await message.answer('Write or send me something and i will send your message to you')


# This handler will handle photos
async def send_photo_echo(message: Message):
    pprint.pprint(message)
    await message.reply_photo(message.photo[0].file_id)


# This handler will handle audio
async def send_audio_echo(message: Message):
    await message.reply_audio(message.audio.file_id)


# This handler will handle voice (non text message)
async def send_voice_echo(message: Message):
    await message.reply_voice(message.voice.file_id)


# This handler will handle documents
async def send_document_echo(message: Message):
    await message.reply_document(message.document.file_id)


# This handler will handle any messages except "/start" and "/help" commands
async def send_echo(message: Message):
    await message.reply(text=message.text)


# Register our handlers
dp.message.register(process_start_command, Command(commands='start'))
dp.message.register(process_help_command, Command(commands='help'))
dp.message.register(send_photo_echo, F.photo)
dp.message.register(send_audio_echo, F.audio)
dp.message.register(send_voice_echo, F.voice)
dp.message.register(send_document_echo, F.document)
dp.message.register(send_echo)

if __name__ == '__main__':
    dp.run_polling(bot)
