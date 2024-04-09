import os

from environs import Env


env = Env()  # Create instance of Env
# read_env() method reads file '.env' and load environmental variables from it
env.read_env('C:\\python\\tg_bot\\stepik_tg_bot-1\\.env')
bot_token = env('BOT_TOKEN')  # Get and save value of env variable into var 'bot_token'
admin_id = env.int('ADMIN_ID')  # Get and convert value of env variable to int, save it in var 'admin_id'

# Print to terminal
print(bot_token)
print(admin_id)
print()

# Checking that vars are in environment
print(os.getenv('BOT_TOKEN'))
print(os.getenv('ADMIN_ID'))