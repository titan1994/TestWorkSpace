import fasttext
import argparse
from os import remove as del_file
from pathlib import Path
from my_lib.sqlite_work import SqlDataConn
from speach_text.path_ext import new_ext_file_path
import speach_text.global_settings as GST


if __name__ == '__main__':
    # 'python demon_learn.py --string demon' - запуск бесконечной обработки

    parser = argparse.ArgumentParser()
    parser.add_argument('--string', type=str, default='', help='')
    opt = parser.parse_args()

    DICT_COLUMNS = {'uid': 'TEXT', 'search': 'TEXT'}
    for i in range(GST.fst_dim_vector):
        DICT_COLUMNS['vect{}'.format(i)] = 'TEXT'

    while True:
        all_txt_file = Path(GST.fts_model_folder).rglob('*{}'.format(GST.text_extension))
        for file_txt in all_txt_file:

            try:
                path_base = new_ext_file_path(file_txt, GST.base_extension)
                path_bin = new_ext_file_path(file_txt, GST.learn_extension)

                with SqlDataConn(path_base) as base_model:

                    name_table = path_base.stem
                    base_model.delete_table(name_table)
                    base_model.create_table(name_table, **DICT_COLUMNS)

                    GST.FST_MODEL_SETTINGS['input'] = str(file_txt.absolute())
                    model = fasttext.train_unsupervised(**GST.FST_MODEL_SETTINGS)

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
