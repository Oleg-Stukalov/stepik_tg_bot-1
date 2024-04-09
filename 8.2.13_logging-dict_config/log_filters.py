import logging


class ErrorLogFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        return record.levelname == 'ERROR'


class DebugWarningLogFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        return record.levelname in ('DEBUG', 'WARNING')


class CriticalLogFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        return record.levelname == 'CRITICAL'
