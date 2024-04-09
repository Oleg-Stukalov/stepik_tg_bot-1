import logging

from module_2 import devide_number
from module_3 import square_number

# Initialization of logger
logger = logging.getLogger(__name__)

# Set level 'DEBUG' to logger
logger.setLevel(logging.DEBUG)


class ErrorLogFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        return record.levelname == 'ERROR'

# Initialization of formatter
formatter_1 = logging.Formatter(fmt='[%(asctime)s] #%(levelname)-8s %(filename)s:%(lineno)d - %(name)s:%(funcName)s - %(message)s')

# Initialization of handler saving logs to 'error.log'
error_file = logging.FileHandler('error.log', mode='w', encoding='utf-8')
# Set level 'DEBUG' to handler
error_file.setLevel(logging.DEBUG)

# Add filter 'ErrorLogFilter' to handler
error_file.addFilter(ErrorLogFilter())

# Define logs format in handler
error_file.setFormatter(formatter_1)

# Add handler to logger
logger.addHandler(error_file)


def main():
    a, b, c, d = 12, 2, 4, 0

    logger.debug('Лог DEBUG-111')
    logger.info('Лог INFO-111')
    logger.warning('Лог WARNING-111')
    logger.error('Лог ERROR111')
    logger.critical('Лог CRITICAL-111')

    print(devide_number(a, square_number(b)))
    print(devide_number(square_number(c), d))
