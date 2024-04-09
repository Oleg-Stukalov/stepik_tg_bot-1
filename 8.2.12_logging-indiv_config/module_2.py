import logging
import sys

logger = logging.getLogger(__name__)
###
logger.setLevel(logging.DEBUG)

class DebugWarningLogFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        return record.levelname in ('DEBUG', 'WARNING')

formatter_2 = logging.Formatter(fmt='#%(levelname)-8s [%(asctime)s] - %(filename)s:%(lineno)d - %(name)s:%(funcName)s - %(message)s')

stdout = logging.StreamHandler(sys.stdout)

stdout.addFilter(DebugWarningLogFilter())

stdout.setFormatter(formatter_2)

logger.addHandler(stdout)

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
