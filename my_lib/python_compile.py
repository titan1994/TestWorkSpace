"""
Библиотеку пайинсталлер ставит ьв основной питон. В вирутальном окружении она не раздупляется
python3 -m pip install --upgrade pip
pip install pypiwin32
pip install pyinstaller
"""

from os import system as system
from pathlib import Path


def compile_exe(python_path_file):
    """
    Быстро скомпилировать любой файл проекта в .exe
    :param python_path_file: путь к файлу относительно каталога проекта
    :return:
    """
    file_path = Path('{}/{}'.format(Path.cwd().parent, python_path_file))
    system('pyinstaller --onefile {}'.format(file_path))


compile_exe('test/test_funct.py')
