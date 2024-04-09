from config_data.config import load_config

config = load_config()  # without path for privacy


print(bot := config.tg_bot.token)
print(superadmin := config.tg_bot.admin_ids[0])
