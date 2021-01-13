import os
import time
import pyttsx3
import shutil

engine = pyttsx3.init()
def sstake():
    engine.say('You have 10 seconds to open the screen of which you want to take the screenshot')
    engine.runAndWait()
    time.sleep(5)
    engine.say('5')
    engine.say('4')
    engine.say('3')
    engine.say('2')
    engine.say('1')
    engine.say('0')
    engine.runAndWait()
    os.system("screencapture ss/screen.png")

    source_dir = '/directory/till/J-A-R-V-S/J-A-R-V-I-S/ss/screen.png'
    target_dir = '/path/to/save/the/screenshot'

    shutil.copy(source_dir, target_dir)
    engine.say('Screenshot saved on desktop as screen.png please change its name before taking another screenshot else it will get deleted.')
    engine.runAndWait()
