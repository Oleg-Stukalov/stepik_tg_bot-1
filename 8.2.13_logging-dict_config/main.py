import logging.config

from logging_settings import logging_config
from module_1 import main

# Load logging settings from dictionary `logging_config`
logging.config.dictConfig(logging_config)

main()
