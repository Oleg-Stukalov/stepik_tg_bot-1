import logging


# Define user filter
class ErrorLogFilter(logging.Filter):
    # Redefine method filter
    def filter(self, record):
        return record.levelname == 'ERROR' and 'важно' in record.msg.lower()


# Define logger
logger = logging.getLogger(__name__)

# Create handler
stderr_handler = logging.StreamHandler()

# Connect filter to handler
stderr_handler.addFilter(ErrorLogFilter())


# Connect handler to logger
logger.addHandler(stderr_handler)

logger.warning('Важно! Это лог с предупреждением!')
logger.error('Важно! Это лог с ошибкой!')
logger.info('Важно! Это лог с уровня INFO!')
logger.error('Это лог с ошибкой!')