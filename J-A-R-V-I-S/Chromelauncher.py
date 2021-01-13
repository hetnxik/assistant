import os
import pyttsx3
import webbrowser as wb
import pywhatkit as pwk

engine = pyttsx3.init()


def launcher():
    engine.say('Opening Chrome')
    engine.runAndWait()
    os.system("open /path/to/chrome")

def venge():
    engine.say('opening venge ')
    engine.runAndWait()
    wb.open('https://venge.io', new = 2)

def youtube():
    wb.open('https://youtube.com')
def playsongonyoutube():
    song = input('Which song/video do you want to watch ? (say video name) : ')
    pwk.playonyt(song)
def googlesearch():
    query = input('What do you want to search ??')
    pwk.search(query)
def ytsearch():
    query = input("what should i search on youtube ? :")
    wb.open('https://www.youtube.com/results?search_query=' + query)
def wiki():
    topic = input("What topic do you want to search on wikipedia ?")
    pwk.info(topic)
