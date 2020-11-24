"""
Настройки проекта
"""
from pathlib import Path

# Стандартные расширения файлов
text_extension = '.txt'
wav_extension = 'wav'
base_extension = '.db'
learn_extension = '.bin'

# Каталоги. Распознавание звука
voice_wav_folder = Path.cwd() / 'file_wav'
voice_text_folder = Path.cwd() / 'file_text'
voice_model_folder = 'model_ru'

# Каталоги. Нечёткий поиск
fts_model_folder = Path.cwd() / 'learn_model'

# Модель нечеткого поиска
fst_dim_vector = 50
FST_MODEL_SETTINGS = {
    'model': 'skipgram',
    'dim': fst_dim_vector,
    'epoch': 200,
    'minn': 2,
    'maxn': 6,
    'lr': 0.5,
    'wordNgrams': 2
}