import fasttext
import argparse
from os import remove as del_file
from pathlib import Path
from my_lib.sqlite_work import SqlDataConn
from speach_text.path_ext import new_ext_file_path

model_folder = Path.cwd() / 'learn_model'
text_extension = '.txt'
base_extension = '.db'
learn_extension = '.bin'

dim_vector = 50
MODEL_SETTINGS = {
    'model': 'skipgram',
    'dim': dim_vector,
    'epoch': 200,
    'minn': 2,
    'maxn': 6,
    'lr': 0.5,
    'wordNgrams': 2
}

if __name__ == '__main__':
    # 'python demon_learn.py --string demon' - запуск бесконечной обработки

    parser = argparse.ArgumentParser()
    parser.add_argument('--string', type=str, default='', help='')
    opt = parser.parse_args()

    DICT_COLUMNS = {'uid': 'TEXT', 'search': 'TEXT'}
    for i in range(dim_vector):
        DICT_COLUMNS['vect{}'.format(i)] = 'TEXT'

    while True:
        all_txt_file = Path(model_folder).rglob('*{}'.format(text_extension))
        for file_txt in all_txt_file:

            try:
                path_base = new_ext_file_path(file_txt, base_extension)
                path_bin = new_ext_file_path(file_txt, learn_extension)

                with SqlDataConn(path_base) as base_model:

                    name_table = path_base.stem
                    base_model.delete_table(name_table)
                    base_model.create_table(name_table, **DICT_COLUMNS)

                    MODEL_SETTINGS['input'] = str(file_txt.absolute())
                    model = fasttext.train_unsupervised(**MODEL_SETTINGS);

                    str_path_bin = str(path_bin.absolute())
                    try:
                        del_file(str_path_bin)
                        model.save_model(str_path_bin)

                    except Exception as info:
                        print('ошибка сохранения модели')
                        raise

                    # Получение векторов
                    model = fasttext.load_model(str_path_bin)

                    list_vectors = []
                    with open(file_txt, 'r', encoding='utf-8') as read_file:

                        for line in read_file.readlines():
                            parts = line.split(';')

                            str_uid = parts[0].strip()
                            str_uid.replace('\n', '')
                            string_analyze = parts[1].strip()
                            string_analyze.replace('\n', '')

                            this_vector = model.get_word_vector(string_analyze)
                            vector_string = [str(x) for x in this_vector]

                            list_vectors.append((str_uid, string_analyze) + tuple(vector_string))

                    # Сохранение векторов в базу данных
                    str_scene = ',?' * (len(DICT_COLUMNS))
                    str_scene = str_scene[1:]

                    str_req = "INSERT INTO {} VALUES ({})".format(name_table, str_scene)

                    cursor_obj = base_model.conn.cursor()
                    cursor_obj.executemany(str_req, list_vectors)
                    base_model.conn.commit()

                    del_file(str(file_txt))

            except Exception as info:
                print(info)

        if opt.string != 'demon':
            break
