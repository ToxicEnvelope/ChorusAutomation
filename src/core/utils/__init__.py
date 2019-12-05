import os
from time import time

root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

class GlobalConfig:
    def get_root_dir():
        return root_dir
    def get_bin_dir():
        return os.path.join(root_dir, r'bin')
    def get_logs_dir():
        return os.path.join(root_dir, r'src\runtime')
    def get_logger_format():
        return r'%(asctime)s - %(levelname)s - %(message)s'
    def timestamp():
        return time().__str__()[:10]

if __name__ == '__main__':
    print('->', GlobalConfig.get_root_dir())
    # print('->', GlobalConfig.get_bin_dir())
    # print('->', GlobalConfig.get_logs_dir())
    # print('->', GlobalConfig.get_logs_dir())
    # print('->', GlobalConfig.get_logger_format())
    # print('->', GlobalConfig.timestamp())
