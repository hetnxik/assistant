import time
import pyttsx3
engine = pyttsx3.init()

def greet():
    t = time.localtime()
    hour = time.strftime("%H", t)
    hour = int(hour)
    engine.say(" ")
    engine.runAndWait()
    if 23 <= hour <= 24 or 0 < hour < 7:
        engine.say("good evening boss.")
        engine.say("I suggest you to go to sleep")
        engine.runAndWait()
        if 3 <= hour <= 7:
            engine.say("have you slept or are you still awake ?")
            engine.runAndWait()
            r = input("have you slept or are you still awake ?")
            if r == "yes":
                engine.say("ok boss")
                engine.runAndWait()
            elif r == 'no':
                engine.say("I highly recommend you to go to sleep")
                engine.runAndWait()
            else:
                engine.say("answer in yes ro no :/")
    elif 16 < hour < 23:
        engine.say("Good Evening")
        engine.runAndWait()
    elif 13 < hour < 16:
        engine.say("goof afternoon")
        engine.runAndWait()
def hihello():

    engine.say("I'm good, how are you")
    engine.runAndWait()

def timex():
    y = time.strftime("%I %M %P")
    engine.say("The time is " + y)
    engine.runAndWait()
    q = input('Enter something : ')
    print(q)