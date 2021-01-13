import os
import pyttsx3

def launcher():
    engine = pyttsx3.init()
    engine.say('Opening Filmora X')
    engine.runAndWait()
    os.system("open /path/to/FilmoraX")



