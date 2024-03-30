# 7.2.1-updates-message.model_dump_json

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


# This handler will handle ANY messages
@dp.message()
async def send_echo(message: Message):
    print(message.model_dump_json(indent=4, exclude_none=True))
    print('**********************************************')


if __name__ == '__main__':
    dp.run_polling(bot)
