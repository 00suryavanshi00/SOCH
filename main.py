from vosk import Model, KaldiRecognizer
import pyaudio

model = Model(r'C:/Users/ssury/Downloads/vosk-model-small-en-in-0.4') #Read model
recognizer = KaldiRecognizer(model, 16000)

#Recognize form microphone

cap = pyaudio.PyAudio()
stream = cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

while True:
    data = stream.read(4096)
    #if len(data) == 0:
    #    break

    if recognizer.AcceptWaveform(data):
        print(recognizer.Result()[14:-3])
