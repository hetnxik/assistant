import speech_recognition as sr
# import webbrowser
# import subprocess

import spotifylauncher as sf
import Chromelauncher as cr
import disspambot as rich
import FilmoraX as FX
# import timepass as tp
import ss

# tp.greet()
# tp.timex()
qwerty = 0
while qwerty == 0:
    try:
         r = sr.Recognizer()  # Speech Recognition Code
         with sr.Microphone() as source:
             print('speak something')
             audio = r.listen(source, phrase_time_limit = 10)
             b = r.recognize_google(audio)
             a = '{}'.format(b)
             print('you said : {}'.format(b))
             command = a.lower()
             print(command)

        if command == 'open spotify':
            sf.launcher()

        if command == 'open google':
            cr.launcher()

        if command == 'open filmora':
            FX.launcher()
        if command == 'test':
            cr.venge()
        if command == 'open yt':
            cr.youtube()

        if command == 'make me rich in dank':
            rich.exec()

        if command == 'take a screenshot':
            ss.sstake()

        if command == 'play a song':
            cr.playsongonyoutube()
        if command == 'search on wikipedia':
            cr.wiki()

        if command == "google search":
            cr.googlesearch()

        if command == "yt search":
            cr.ytsearch()
        
    except sr.UnknownValueError:
        print("I didn't get you")
