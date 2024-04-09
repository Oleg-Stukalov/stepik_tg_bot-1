import logging
import sys


# Define format_1
format_1 = '#%(levelname)-8s [%(asctime)s] - %(filename)s:%(lineno)d - %(name)s - %(message)s'
# Define format_2
format_2 = '[{asctime}] #{levelname:8} {filename}:{lineno} - {name} - {message}'

# Initialize formatter_1
formatter_1 = logging.Formatter(fmt=format_1)
# Initialize formatter_2
formatter_2 = logging.Formatter(
    fmt=format_2,
    style='{'
)

# Create logger
logger = logging.getLogger(__name__)

# Initialize handler sending logs to stderr
stderr_handler = logging.StreamHandler()
# Initialize handler sending logs to stdout
stdout_handler = logging.StreamHandler(sys.stdout)

# Set formatters to handlers
stderr_handler.setFormatter(formatter_1)
stdout_handler.setFormatter(formatter_2)

# Add handlers to logger
logger.addHandler(stderr_handler)
logger.addHandler(stdout_handler)

# Create log
logger.warning('This is WARNING log')
