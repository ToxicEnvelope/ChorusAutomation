import os

root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
class GlobalConfig:
    def get_bin_dir():
        return os.path.join(root_dir, 'bin')


if __name__ == '__main__':
    print('->', GlobalConfig.get_bin_dir())