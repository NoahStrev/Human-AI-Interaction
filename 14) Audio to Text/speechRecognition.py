# pip install SpeechRecognition

import speech_recognition as sr

recog = sr.Recognizer()
recog.energy_threshold = 300

sample = sr.AudioFile("harvard.wav")

with sample as source:
    recog.adjust_for_ambient_noise(source, duration = .5)
    audio = recog.record(source)
    print(type(audio))
    print(recog.recognize_google(audio))
    
sample2 = sr.AudioFile("noisey.wav")

with sample2 as source:
    recog.adjust_for_ambient_noise(source, duration = .5)
    audio = recog.record(source)
    print(type(audio))
    x = recog.recognize_google(audio, show_all = True)

for a in x['alternative']:
    print(a)
