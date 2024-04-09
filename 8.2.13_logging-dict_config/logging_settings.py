import sys
from log_filters import ErrorLogFilter, DebugWarningLogFilter, CriticalLogFilter


logging_config = {
    'version': 1,
    'disable_existing_config': True,
    'formatters': {
        'default': {
            'format': '#%(levelname)-8s %(name)s:%(funcName)s - %(message)s'
        },
        'formatter_1': {
            'format': '[%(asctime)s] #%(levelname)-8s %(filename)s:%(lineno)d - %(name)s:%(funcName)s - %(message)s'
        },
        'formatter_2': {
            'format': '#%(levelname)-8s [%(asctime)s] - %(filename)s:%(lineno)d - %(name)s:%(funcName)s - %(message)s'
        },
        'formatter_3': {
            'format': '#%(levelname)-8s [%(asctime)s] - %(message)s'
        }
    },
    'filters': {
        'error_filter': {
            '()': ErrorLogFilter  # without '' !!!
        },
        'debug_warning_filter': {
            '()': DebugWarningLogFilter
        },
        'critical_filter': {
            '()': CriticalLogFilter
        }
    },
    'handlers': {
        'default': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        },
        'error_file': {
            'class': 'logging.FileHandler',
            'filename': 'error.log',
            'mode': 'w',
            'encoding': 'utf-8',
            'level': 'DEBUG',
            'filters': ['error_filter'],  # var name, not filter class!!!
            'formatter': 'formatter_1'
        },
        'stdout': {
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
            'filters': ['debug_warning_filter'],
            'formatter': 'formatter_2'
        },
        'stderr': {
            'class': 'logging.StreamHandler'
        },
        'critical_file': {
            'class': 'logging.FileHandler',
            'filename': 'critical.log',
            'mode': 'w',
            'encoding': 'utf-8',
            'filters': ['critical_filter'],
            'formatter': 'formatter_3'
        }
    },
    'loggers': {
        'module_1': {
            'level': 'DEBUG',
            'handlers': ['error_file']
        },
        'module_2': {
            'handlers': ['stdout']
        },
        'module_3': {
            'handlers': ['stderr', 'critical_file']
        }
    },
    'root': {
        'handlers': ['default'],
        'formatter': 'default'
    }
}
