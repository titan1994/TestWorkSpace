"""
Запуск скриптов именно тем питоном, которым запущен основной
И установка библиотек в виртуальное окружение
"""

from os import system as system
from pathlib import Path
import sys

virtual_env_name = 'venv'
virtual_lib_catalog_name = 'Lib/site-packages'


def lib_install(name_pack, name_module='pip'):
    """
    Установка пакетов библиотек

    Args:
        name_pack: имя пакета
        name_module: имя модуля pip, pipwin
    """

    if name_module not in ('pip', 'pip3'):
        pip_install_pack(name_module, 'pip')

    pip_install_pack(name_pack, name_module)


def pip_install_pack(name_pack, name_module='pip'):
    """
    Установка пакетов библиотек через указанный модуль

    Args:
        name_pack: имя пакета
        name_module: pip, pipwin
    """

    python_pass = get_python_pass()
    if virtual_env_name not in python_pass:
        print('Внимание! Не настроено виртуальное оркужение!')

        inst_cmd = '{} install --upgrade {}'.format(name_module, name_pack)
    else:
        work_space, *python_exe = python_pass.split('{}{}'.format(virtual_env_name, Path('/')))
        path_pack = Path('{}/{}/{}'.format(work_space, virtual_env_name, virtual_lib_catalog_name))

        inst_cmd = '{} -m {} install --upgrade --target={} {}'.format(python_pass, name_module, path_pack, name_pack)

    print(inst_cmd)
    system(inst_cmd)


def get_python_pass():
    """
    Путь к питону в виртуальной среде
    """
    return sys.executable


def run_python_file(python_file, params=''):
    """
    Args:
        python_file:
        params:
    """
    python_pass = get_python_pass()

    file_run_pass = '{} {} {}'.format(Path(python_pass), Path(python_file), params)
    try:
        result_run = system(file_run_pass)
        return result_run

    except Exception as info:
        print(file_run_pass)
        print(info)
        return None
