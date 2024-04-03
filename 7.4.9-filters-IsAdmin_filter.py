# 7.4.9-filters-IsAdmin_filter

from aiogram import Bot, Dispatcher
from aiogram.filters import BaseFilter
from aiogram.types import Message

# Instead of BOT TOKEN HERE copy your bot token from @BotFather
BOT_TOKEN = '6468393428:AAHH9wSFOiVIpE3ba1uHurJKM1dBhb9_HfA'

# Create Bot and Dispatcher instances
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Bots admins list
admin_ids: list[int] = [455325562]


# Filter for checking admin rights
class IsAdmin(BaseFilter):
    def __init__(self, admin_ids: list[int]) -> None:
        self.admin_ids = admin_ids

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admin_ids


# Handler for admin
@dp.message(IsAdmin(admin_ids))
async def answer_if_admins_update(message: Message):
    await message.answer(text='You are admin!!!')


# Handler for not admin
@dp.message()
async def answer_if_not_admins_update(message: Message):
    await message.answer(text='You are not admin')


if __name__ == '__main__':
    dp.run_polling(bot)
