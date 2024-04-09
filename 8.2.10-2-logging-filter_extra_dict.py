import logging


# Define user filter
class EvenLogFilter(logging.Filter):
    # Redefine method filter
    def filter(self, record):
        return not record.i % 2


# Define logger
logger = logging.getLogger(__name__)

# Create handler
stderr_handler = logging.StreamHandler()

# Connect filter to handler
stderr_handler.addFilter(EvenLogFilter())

# Connect handler to logger
logger.addHandler(stderr_handler)


for i in range(1, 5):
    logger.warning('Важно! Это лог с предупреждением! %d', i, extra={'i': i})