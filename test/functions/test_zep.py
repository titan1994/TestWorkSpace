values = [1.34, 3.25, 2.99]
coefficient = [3, 2, 2]

for i, j in zip(values, coefficient):
    print(i * j)


from my_lib.python_run import packege_install

packege_install('pyqtdeploy', 'PyQt5 pyqtdeploy')


scores = [54,67,48,99,27]
for i, score in enumerate(scores):
   print(i, score)

print(enumerate(scores))


rg_test = range(1,20)

print(rg_test)

my_crazy_iterator = iter(rg_test)
print(my_crazy_iterator)
print(next(my_crazy_iterator))

from pathlib import Path

print(Path.cwd().glob('pyvenv.cfg'))
print(Path.cwd())
print(Path.cwd().parts)
print(Path.cwd().parent)

alfa = Path.cwd().parts.index('PycharmProjects')
print(alfa)

# def get_pycharm_project_path

import sys

print(sys.executable)

print('venv' in sys.executable)

all_path = sys.executable.split('venv{}'.format(Path('/')))
work_space, *python_exe = sys.executable.split('venv{}'.format(Path('/')))
print(work_space)

path_pack = Path('{}/{}/{}'.format(work_space, 'virtual_env_name', 'virtual_lib_catalog_name'))
print(path_pack)

# from my_lib.pyrhon_run import lib_install
# lib_install("matplotlib")