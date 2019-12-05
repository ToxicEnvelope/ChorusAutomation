import logging, coloredlogs
from time import time
import os
log_format = '%(asctime)s - %(levelname)s - %(message)s'
my_project_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class Logger:

    # constructor
    def __init__(self, namespace):
        self._ = namespace
        logging.basicConfig(format=f'{log_format}',
                            filemode='w',
                            filename=f'{my_project_dir}/runtime/runtime-{time().__str__()[:10]}.log'.format(),
                            level=logging.DEBUG)
        self._logger = logging.getLogger(self._)
        coloredlogs.install(level='DEBUG', logger=self._logger)

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

