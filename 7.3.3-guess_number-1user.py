# 7.3.3-guess_number-1user

import random

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

# Instead of BOT TOKEN HERE copy your bot token from @BotFather
BOT_TOKEN = '6468393428:AAHH9wSFOiVIpE3ba1uHurJKM1dBhb9_HfA'

# Create Bot and Dispatcher instances
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Quantity of user attempts to guess the secret number
ATTEMPTS = 5

# Dict for saving user data
user_dct = {'in_game': False,
            'secret_number': None,
            'attempts': None,
            'total_games': 0,
            'wins': 0}


# Function returning random integer from 1 to 100
def get_random_number() -> int:
    return random.randint(1, 100)


# Handler for '/start' command
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        'Hello!\nLets play in game "Guess the number"?\n\n'
        'To get the game rules and list of commands - '
        'send command /help'
    )


# Handler for '/help' command
@dp.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(
        f'The game rules:\nI guess a number from 1 to 100, '
        f'you need to guess it.\nYou have {ATTEMPTS} '
        f'attempts.\n\nAvailable commands:\n/help - the game rules'
        f'and list of commands\n/cancel - exit from the game\n'
        f'/stat - see statistics\n\nLets play now?'
    )


# Handler for '/stat' command
@dp.message(Command(commands='stat'))
async def process_stat_command(message: Message):
    await message.answer(
        f'Total games played: {user_dct["total_games"]}\n'
        f'Games won: {user_dct["wins"]}'
    )


# Handler for '/cancel' command
@dp.message(Command(commands='cancel'))
async def process_cancel_command(message: Message):
    if user_dct['in_game']:
        user_dct['in_game'] = False
        await message.answer(
            'You are out of the game. If you will want '
            'to play again - write me!'
        )
    else:
        await message.answer(
            'We are not playing now.'
            'Lets play again?'
        )


# Handler will trigger if the user agrees to play the game
@dp.message(F.text.lower().in_(['y', 'yes', 'lets play', 'play']))
async def process_positive_answer(message: Message):
    if not user_dct['in_game']:
        user_dct['in_game'] = True
        user_dct['secret_number'] = get_random_number()
        user_dct['attempts'] = ATTEMPTS
        await message.answer(
            'I guessed number from 1 to 100, '
            'guess it!'
        )
    else:
        await message.answer(
            'While we are playing i can '
            'react on numbers from 1 to 100'
            'and commands /cancel and /stat'
        )


# Handler will trigger if the user refuses to play the game
@dp.message(F.text.lower().in_(['n', 'no', 'do not want', 'will not']))
async def process_negative_answer(message: Message):
    if not user_dct['in_game']:
        await message.answer(
            'What a pity.\n\nIf you will want to play - '
            'write me!'
        )
    else:
        await message.answer(
            'We are playing now. Please, send'
            'number from 1 to 100'
        )


# Handler handling user numbers 1 - 100
@dp.message(lambda x: x.text and x.text.isdigit() and 1 <= int(x.text) <= 100)
async def process_numbers_answer(message: Message):
    if user_dct['in_game']:
        if int(message.text) == user_dct['secret_number']:
            user_dct['in_game'] = False
            user_dct['total_games'] += 1
            user_dct['wins'] += 1
            await message.answer(
                'Congratulations! You guessed the number!\n\n'
                'Lets play again?'
            )
        elif int(message.text) > user_dct['secret_number']:
            user_dct['attempts'] -= 1
            await message.answer(f'The guessed number is less.\nAttempts left: {user_dct["attempts"]}')
        elif int(message.text) < user_dct['secret_number']:
            user_dct['attempts'] -= 1
            await message.answer(f'The guessed number is greater.\nAttempts left: {user_dct["attempts"]}')

        if user_dct['attempts'] == 0:
            user_dct['in_game'] = False
            user_dct['total_games'] += 1
            await message.answer(
                f'Unfortunately you have no attempts more.'
                f'Game over!\n\nGuessed number is {user_dct["secret_number"]}. '
                f'Lets play again?'
            )
    else:
        await message.answer('We are not playing now. Do you want to play?')


# Handler for any other messages
@dp.message()
async def process_other_answers(message: Message):
    if user_dct['in_game']:
        await message.answer(
            'We are playing now.'
            'Please, send number from 1 to 100.'
        )
    else:
        await message.answer(
            'I do not understand your answer. Lets play the game?'
        )

if __name__ == '__main__':
    dp.run_polling(bot)
    welcome_message = """
    Hello!\nLets play in game "Guess the number"?\n
    To get the game rules and list of commands -
    send command /help"""
#   message.answer(welcome_message)
