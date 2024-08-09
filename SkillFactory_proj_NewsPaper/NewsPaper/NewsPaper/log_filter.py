import logging


class DebugInfoFilter(logging.Filter):
    def filter(self, record):
        if record.levelname == 'DEBUG' or record.levelname == 'INFO':
            return True
        return False


class WarningFilter(logging.Filter):
    def filter(self, record):
        if record.levelname == 'WARNING':
            return True
        return False


class ErrorCriticalFilter(logging.Filter):
    def filter(self, record):
        if record.levelname == 'ERROR' or record.levelname == 'CRITICAL':
            return True
        return False
