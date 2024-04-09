import logging

logger = logging.getLogger(__name__)


def square_number(number: int | float) -> float:

    logger.debug('Лог DEBUG-333')
    logger.info('Лог INFO-333')
    logger.warning('Лог WARNING-333')
    logger.error('Лог ERROR-333')
    logger.critical('Лог CRITICAL-333')

    return number ** 2