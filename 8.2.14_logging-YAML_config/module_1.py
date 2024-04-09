import logging

from module_2 import devide_number
from module_3 import square_number

# Initialization of logger
logger = logging.getLogger(__name__)


def main():
    a, b, c, d = 12, 2, 4, 0

    logger.debug('Лог DEBUG-111')
    logger.info('Лог INFO-111')
    logger.warning('Лог WARNING-111')
    logger.error('Лог ERROR111')
    logger.critical('Лог CRITICAL-111')

    print(devide_number(a, square_number(b)))
    print(devide_number(square_number(c), d))
