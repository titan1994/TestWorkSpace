# import fasttext
# import numpy
# import faiss
# import math

from my_lib.sqlite_work import SqlDataConn
from pathlib import Path
import speach_text.global_settings as GST


def find_text_in_models(text):
    """
    По обученным моделям ищет объект
    Args:
        text: анализируемый текст

    Returns:

        dict_result - словарь с найденными объектами
    """
    dict_result = {}

    all_model_file = Path(GST.fts_model_folder).rglob('*{}'.format(GST.base_extension))

    for model_file in all_model_file:

        try:
            with SqlDataConn(model_file) as base_model:

                rows = base_model.select_from(model_file.stem)





        except Exception as info:
            print(info)

    return dict_result


Alfa = find_text_in_models('Вера Николаевна принеси нам пивасик')