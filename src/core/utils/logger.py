from time import time
from src.core.utils import GlobalConfig
import logging, coloredlogs
import os

class Logger:
    # constructor
    def __init__(self, namespace):
        self._ = namespace
        logging.basicConfig(format=f'{GlobalConfig.get_logger_format()}',
                            filemode=u'w',
                            filename=f'{GlobalConfig.get_logs_dir()}/runtime-{GlobalConfig.timestamp()}.log',
                            level=logging.DEBUG)
        self._logger = logging.getLogger(self._)
        coloredlogs.install(level=u'DEBUG', logger=self._logger)

    # info level log
    def info(self, msg):
        self._logger.info(msg)

    # warn level log
    def warn(self, msg):
        self._logger.warning(msg)

    # critical level log
    def critical(self, msg):
        self._logger.critical(msg)

    #  debug level
    def debug(self, msg):
        self._logger.debug(msg)

    # error level log
    def error(self, msg):
        self._logger.error(msg)


if __name__ == '__main__':
    l = Logger(__name__)
    l.info('test')
    l.warn('test')
    l.critical('test')
    l.error('test')
    l.debug('test')
