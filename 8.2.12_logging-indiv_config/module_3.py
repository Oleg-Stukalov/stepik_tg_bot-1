import logging

logger = logging.getLogger(__name__)

class CriticalLogFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        return record.levelname == 'CRITICAL'

formatter_3 = logging.Formatter(fmt='#%(levelname)-8s [%(asctime)s] - %(message)s')

stderr = logging.StreamHandler()
critical_file = logging.FileHandler('critical.log', mode='w', encoding='utf-8')

critical_file.setFormatter(formatter_3)

critical_file.addFilter(CriticalLogFilter())

logger.addHandler(stderr)
logger.addHandler(critical_file)

def square_number(number: int | float) -> float:

    logger.debug('Лог DEBUG-333')
    logger.info('Лог INFO-333')
    logger.warning('Лог WARNING-333')
    logger.error('Лог ERROR-333')
    logger.critical('Лог CRITICAL-333')

    return number ** 2