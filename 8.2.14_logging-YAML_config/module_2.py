import logging

logger = logging.getLogger(__name__)


def devide_number(dividend: int | float, devider: int | float):
    logger.debug('Лог DEBUG-222')
    logger.info('Лог INFO-222')
    logger.warning('Лог WARNING-222')
    logger.error('Лог ERROR-222')
    logger.critical('Лог CRITICAL-222')

    try:
        return dividend / devider
    except ZeroDivisionError:
        logger.exception('Division by 0')
