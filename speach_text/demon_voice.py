from vosk import Model, KaldiRecognizer
from pathlib import Path
import argparse
import wave
import json
from os import remove as del_file
from speach_text.smart_search import find_text_in_models
import speach_text.global_settings as GST

model = Model(GST.voice_model_folder)


class ErrWav(Exception):
    def __init__(self, text):
        self.txt = text


if __name__ == '__main__':
    # 'python demon_voice.py --string demon' - запуск бесконечной обработки

    parser = argparse.ArgumentParser()
    parser.add_argument('--string', type=str, default='', help='')
    opt = parser.parse_args()

    while True:
        all_wav_file = Path(GST.voice_wav_folder).rglob('*.{}'.format(GST.wav_extension))
        for file_wav in all_wav_file:

            file_txt = str(file_wav.name).replace(GST.wav_extension, GST.text_extension)
            path_text_file = GST.voice_text_folder.joinpath(GST.voice_text_folder, file_txt)

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

                    wf.close()
                    # Получаем json и сохраняем в папку
                    data_found = find_text_in_models(dict_py['text'])

                    with open(path_text_file, 'w', encoding='utf8') as text_write:
                        json.dump(data_found, text_write)
                        # text_write.write(dict_py['text'] + '\n')

                    # Удаляем файлик звука. Чтобы не захламлять систему. Возможно закинуть это на плечи 1С?
                    del_file(str(file_wav))

                except Exception as err_info:
                    print(err_info)

        if opt.string != 'demon':
            break
