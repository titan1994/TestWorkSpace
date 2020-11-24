import fasttext
import argparse
import sqlite3
from pathlib import Path
from my_lib.sqlite_work import SqlDataConn

model_folder = Path.cwd() / 'learn_model'
text_extension = 'txt'
base_extension = 'db'


if __name__ == '__main__':
    # 'python demon_learn.py --string demon' - запуск бесконечной обработки

    parser = argparse.ArgumentParser()
    parser.add_argument('--string', type=str, default='', help='')
    opt = parser.parse_args()

    while True:
        all_wav_file = Path(model_folder).rglob('*.{}'.format(text_extension))
        for file_wav in all_wav_file:

            file_txt = str(file_wav.name).replace(base_extension, text_extension)
            path_base_file = model_folder.joinpath(model_folder, file_txt)
            if not path_base_file.exists():

                try:

                    pass

                except Exception as err_info:
                    print(err_info)

        if opt.string != 'demon':
            break
