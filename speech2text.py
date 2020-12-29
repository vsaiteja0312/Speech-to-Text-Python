# import sounddevice as sd
# import matplotlib
# from matplotlib import pyplot as plt
# import numpy as np
# import tkinter
from scipy.io.wavfile import write
import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source, duration = 0.5)
	print("Heyy Say Something......")
	audio = r.listen(source)

print("Recognizing.......")

try:
	print(r.recognize_google(audio))
except:
	print("wrong")


with open("recordedAudio.wav", "wb") as f:
	f.write(audio.get_wav_data())

# Fs = 44100
# d = 5

# myrecording = sd.rec(int(d*Fs), samplerate = Fs, channels = 2)
# sd.wait()







