import fasttext
import argparse
import sqlite3
from pathlib import Path
from my_lib.sqlite_work import SqlDataConn
from speach_text.path_ext import new_ext_file_path

model_folder = Path.cwd() / 'learn_model'
text_extension = 'txt'
base_extension = 'db'
learn_extension = 'bin'


MODEL_SETTINGS = {
    'model': 'skipgram',
    'dim': 50,
    'epoch': 200,
    'minn': 2,
    'maxn': 6,
    'lr': 0.5,
    'wordNgrams': 2,
    'loss': 'ova'
}


if __name__ == '__main__':
    # 'python demon_learn.py --string demon' - запуск бесконечной обработки

    parser = argparse.ArgumentParser()
    parser.add_argument('--string', type=str, default='', help='')
    opt = parser.parse_args()

    while True:
        all_txt_file = Path(model_folder).rglob('*.{}'.format(text_extension))
        for file_txt in all_txt_file:
            path_base = new_ext_file_path(file_txt, base_extension)
            path_bin = new_ext_file_path(file_txt, learn_extension)

            with SqlDataConn(path_base) as base_model:
                base_model.delete_table(path_base.stem)

                # Обучение
                model = fasttext.train_unsupervised(file_txt, **MODEL_SETTINGS)
                model.save_model(path_bin)

                # Получение векторов

                model = fasttext.load_model(path_bin)

                num = []
                with open('/home/uadmin/Загрузки/fasttext1C/1c/data/os_pochta.txt', 'r') as r:
                    for line in r.readlines():
                        parts = line.split(';')
                        s = parts[1].replace('\n', '')
                        b = [str(x) for x in model.get_word_vector(s)]
                        num.append((parts[0],) + tuple(b))
                print("INSERT INTO nomenclature VALUES (" + ','.join(['?'] * (vector_dim + 1)) + ")")
                print(num)

                # cursor.executemany(, num)
                # conn.commit()


        if opt.string != 'demon':
            break
