from sys import argv, exit
from os import system
from platform import platform
from time import sleep
from src.core.utils import GlobalConfig


ENV_NAME = u"venvChorus"
DEP_FILE = u"requierments.txt"
WIN = u'win'
CLS = u'cls'
CLEAR = u'clear'
P = platform().lower()

WINDOWS_BUILD_SCRIPT = [f'py -m venv {GlobalConfig.get_root_dir()}\\{ENV_NAME}', f'.\\{ENV_NAME}\\Scripts\\activate', f'py -m pip install -r {DEP_FILE}']
LINUX_BUILD_SCRIPT = [f'python3 -m venv {GlobalConfig.get_root_dir()}\\{ENV_NAME}', f'source {ENV_NAME}/bin/activate', f'pythn3 -m pip install -r {DEP_FILE}']

WINDOWS_CLEAN_SCRIPT = [f'py -m pip freeze > {DEP_FILE}', f'.\\{ENV_NAME}\\Scripts\\deactivate' ,f'rm -rf ./{ENV_NAME}']
LINUX_CLEAN_SCRIPT = [f'python3 -m pip freeze > {DEP_FILE}', f'source {ENV_NAME}/bin/deactivate', f'rm -rf ./{ENV_NAME}']

execute = lambda x, y: system(f'{x}') if WIN in P else system(f'{y}')
clearconsole = lambda: system(f'{CLS}') if WIN in P else system(f'{CLEAR}')
# build = lambda: system(f'{WINDOWS_BUILD_SCRIPT}') if WIN in platform().lower() else system(f'{LINUX_BUILD_SCRIPT}')
# clean = lambda: system(f'{WINDOWS_CLEAN_SCRIPT}') if WIN in platform().lower() else system(f'{LINUX_CLEAN_SCRIPT}')

def help():
    clearconsole()
    a1 = u"\n\n[MANAGE.PY COMMANDS]\n"
    a2 = u"[FLAG]      [EXAMPLE]                    [DESCRIPTION]\n"
    a3 = u"--help      py manage.py -help           display help menu and present information\n"
    a40 = u"deactivate venv and deleted dependencies"
    a41 = f"--clean     py manage.py --clean         clean the project, freeze dependencies, {a40}\n"
    a5 = u"--build     py manage.py --build         build and activate a venv and deploy dependencies\n"
    return f"{a1}{a2}{a3}{a41}{a5}"

def build():
    clearconsole()
    print(u'[+] -- BUILDING ENVIRONMENT --')
    print(f'[$] exec: `{WINDOWS_BUILD_SCRIPT[0]}`') if WIN in P else print(f'[$] exec: `{LINUX_BUILD_SCRIPT[0]}`')
    execute(WINDOWS_BUILD_SCRIPT[0], LINUX_BUILD_SCRIPT[0])
    sleep(5)
    print(f'[$] exec: `{WINDOWS_BUILD_SCRIPT[1]}`') if WIN in P else print(f'[$] exec: `{LINUX_BUILD_SCRIPT[1]}`')
    execute(WINDOWS_BUILD_SCRIPT[1], LINUX_BUILD_SCRIPT[1])
    sleep(5)
    print(f'[$] exec: `{WINDOWS_BUILD_SCRIPT[2]}`') if WIN in P else print(f'[$] exec: `{LINUX_BUILD_SCRIPT[2]}`')
    execute(WINDOWS_BUILD_SCRIPT[2], LINUX_BUILD_SCRIPT[2])
    sleep(5)


def clean():
    clearconsole()
    print(u'[+] -- CLEANING ENVIRONMENT --')
    print(f'[$] exec: `{WINDOWS_CLEAN_SCRIPT[0]}`') if WIN in P else print(f'[$] exec: `{LINUX_BUILD_SCRIPT[0]}`')
    execute(WINDOWS_CLEAN_SCRIPT[0], LINUX_CLEAN_SCRIPT[0])
    sleep(5)
    print(f'[$] exec: `{WINDOWS_CLEAN_SCRIPT[1]}`') if WIN in P else print(f'[$] exec: `{LINUX_BUILD_SCRIPT[1]}`')
    execute(WINDOWS_CLEAN_SCRIPT[1], LINUX_CLEAN_SCRIPT[1])
    sleep(5)
    print(f'[$] exec: `{WINDOWS_CLEAN_SCRIPT[2]}`') if WIN in P else print(f'[$] exec: `{LINUX_BUILD_SCRIPT[2]}`')
    execute(WINDOWS_CLEAN_SCRIPT[2], LINUX_CLEAN_SCRIPT[2])
    sleep(5)


if __name__ == '__main__':
    if len(argv) > 1:
        if argv[1] == '--help':
            print(help())
            exit(0)
        elif argv[1] == '--clean':
            clean()
            exit(0)
        elif argv[1] == '--build':
            build()
            exit(0)
        else:
            clearconsole()
            print(f'[!] `{argv[1]}` is an invalid flag!\n[*] use flags --help for more informantion!')
            exit(0)
    else:
        clearconsole()
        print(u'[+] require arguments!\n[*] use flags --help for more informantion!')
        exit(0)

