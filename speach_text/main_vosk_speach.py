from my_lib.python_run import lib_install

# lib_install('vosk')
# lib_install('pyaudio', 'pipwin')


from vosk import Model, KaldiRecognizer
import pyaudio

model_folder = 'model_ru'

model = Model(model_folder)
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

while True:
    data = stream.read(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        print(rec.Result())
    else:
        print(rec.PartialResult())

print(rec.FinalResult())