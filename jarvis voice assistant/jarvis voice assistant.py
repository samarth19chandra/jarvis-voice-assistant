import pyttsx3 
import speech_recognition as sr
import datetime 
import pyaudio
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')  # windows speech recognition API
voices = engine.getProperty('voices') # To get all the voices from the module
print(voices[1].id)
engine.setProperty('voice',voices[0].id) # To set voice 1

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

speak("Hello I  am  jarvis  Your personal assistant Please tell me how can I help you ")

def takeCommmand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1  # for waiting for how much time to wait after recognizing starts to finally analyze words
        audio = r.listen(source)
    

    try:
        print("recognizing....")
        query = r.recognize_google(audio,language='en-in')

    except Exception as e:
        print(e)
        print("sorry please say that again please....")
        return "none"
    return query

if __name__ == "__main__":
    WishMe()
    while True:
        query = takeCommmand().lower()
        if "wikipedia" in query:
            speak("searching in wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=3)
            speak("according to Wikipedia")
            speak(results)
            print(results)

        elif 'google' in query:
            speak("opening google for you")
            webbrowser.open("google.com")

        elif 'Youtube' in query:
            speak("opening youtube for you")
            webbrowser.open("youtube.com")
            
        elif 'time' in query:
            straTtime = datetime.datetime.now().strftime("%H:%M:%S")
            print(straTtime)
            speak(" Sir the current time is ")

        elif 'quit' in query:
            speak("goodbye sir!")
            exit() 

        elif 'who' in query:
            speak("I am Jarvis Sir. I am build using Python.currently I am in development state. the name of my developer is Mr.Samarth Chandra")
