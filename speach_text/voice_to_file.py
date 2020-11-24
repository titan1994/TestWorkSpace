from vosk import Model, KaldiRecognizer
from pathlib import Path
import argparse
import wave
import json

name_model = 'model_ru'
wav_folder = Path.cwd() / 'file_wav'
text_folder = Path.cwd() / 'file_text'
wav_extension = 'wav'
text_extension = 'txt'

model = Model(name_model)


class ErrWav(Exception):
    def __init__(self, text):
        self.txt = text


if __name__ == '__main__':
    # 'python voice_to_file.py --string demon' - запуск бесконечной обработки

    parser = argparse.ArgumentParser()
    parser.add_argument('--string', type=str, default='', help='')
    opt = parser.parse_args()

    while True:
        all_wav_file = Path(wav_folder).rglob('*.{}'.format(wav_extension))
        for file_wav in all_wav_file:

            file_txt = str(file_wav.name).replace(wav_extension, text_extension)
            path_text_file = text_folder.joinpath(text_folder, file_txt)
            if not path_text_file.exists():

                try:
                    wf = wave.open(str(file_wav.absolute()), "rb")
                    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
                        raise ErrWav("Unsupported wav format")
                        continue

                    rec = KaldiRecognizer(model, wf.getframerate())

                    while True:
                        data = wf.readframes(4000)
                        if len(data) == 0:
                            break
                        if rec.AcceptWaveform(data):
                            # print(rec.Result())
                            pass

                    result_dict_json = rec.FinalResult()
                    dict_py = json.loads(result_dict_json)

                    with open(path_text_file, 'w', encoding='utf8') as text_write:
                        text_write.write(dict_py['text'] + '\n')

                    print(dict_py['text'])

                except Exception as err_info:
                    print(err_info)

        if opt.string != 'demon':
            break
