# 7.4.10-filters-arguments_into_handlers

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
class NumbersInMessage(BaseFilter):
    async def __call__(self, message: Message) -> bool | dict[str, list[int]]:
        numbers = []
        # split message, normalize (delete .,spaces); isdigit() check, append
        for word in message.text.split():
            normalized_word = word.replace('.', '').replace(',', '').strip()
            if normalized_word.isdigit():
                numbers.append(int(normalized_word))
        if numbers:
            return {'numbers': numbers}
        return False


# Handler for updates starting 'find numbers'and have numbers
@dp.message(F.text.lower().startswith('find numbers'), NumbersInMessage):
# except Message get in handler list of numbers from FILTER
async def process_if_numbers(message: Message, numbers: list[int]):
    await message.answer(text=f'Found: {", ".join(str(num) for num in numbers)}')


# Handler for updates starting 'find numbers'and have NO numbers
@dp.message(F.text.lower().startswith('find numbers'))
async def process_if_no_numbers(message: Message):
    await message.answer(text='Did not find numbers')


if __name__ == '__main__':
    dp.run_polling(bot)
