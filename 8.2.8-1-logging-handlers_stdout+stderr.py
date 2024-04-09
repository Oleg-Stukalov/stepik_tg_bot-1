import logging
import sys
logger = logging.getLogger(__name__)

stderr_handler = logging.StreamHandler()
stdout_handler = logging.StreamHandler(sys.stdout)

logger.addHandler(stderr_handler)
logger.addHandler(stdout_handler)

print(logger.handlers)

logger.warning('This is WARNING log')
