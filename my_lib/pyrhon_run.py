"""
Запуск скриптов и установка библиотек
"""

from os import system as system
from pathlib import Path


def packege_install(name_pack, name_install=''):
    """
    Спасение от всех бед. Ставим пакет, если его нет - в вирутальное окружение

    :param name_pack: имя библиотеки при импорте
    :param name_install: имя библиотеки при установке
    :return:
    """
    try:
        exec('import {}'.format(name_pack))
    except ModuleNotFoundError:
        path_pack = Path.cwd() / 'venv' / 'Lib' / 'site-packages'
        name_install = name_install if len(name_install) > 0 else name_pack
        inst_cmd = 'pip install --upgrade --ignore-installed --target={} {}'.format(path_pack, name_install)
        system(inst_cmd)


def get_python_pass():
    """
    Получает путь к питону в виртуальном окружении Пайчарм
    :return: путь к питону
    """

    if Path('venv').exists():
        python_pass = Path.cwd() / 'venv' / 'Scripts' / 'python.exe'
        return python_pass
    return None


def run_python_file_in_env(python_file, params=''):
    """
    запускает какой-либо скрипт питона, используя питон из виртуального окружения
    :param python_file: путь к скрипту
    :param params: параметры запуска
    :return:
    """
    python_pass = get_python_pass()
    if python_pass is None:
        print('не установлено виртуальное окружение!')
        return None

    file_run_pass = '{} {} {}'.format(Path(python_pass), Path(python_file), params)
    try:
        result_run = system(file_run_pass)
        print(file_run_pass)
        return result_run
    except Exception as info:
        print(info)
        return None
