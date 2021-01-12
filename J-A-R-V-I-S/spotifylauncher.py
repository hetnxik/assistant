import os
import pyttsx3
def launcher():
    engine = pyttsx3.init()
    engine.say('Opening Spotify')
    engine.runAndWait()
    os.system("open /Applications/Spotify.app")
