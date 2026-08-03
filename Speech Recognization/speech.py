import speech_recognition as sr
from time import ctime
import time
import os,sys
from gtts import gTTS
import datetime

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        tts = gTTS(text='Good Morning!', lang='en')
        tts.save("audio.mp3")
        os.system("mpg321 audio.mp3")

    if currentH >= 12 and currentH < 18:
        tts = gTTS(text='Good Afternoon!', lang='en')
        tts.save("audio.mp3")
        os.system("mpg321 audio.mp3")

    if currentH >= 18 and currentH !=0:
        tts = gTTS(text='Good Evening!', lang='en')
        tts.save("audio.mp3")
        os.system("mpg321 audio.mp3")

greetMe()


def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")

def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source, phrase_time_limit=6)

    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio , language="en")
        print("You said: " + data)
        speak("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data

def jarvis(data):
    if "how are you" in data:
        speak("I am fine")

    if "what time is it" in data:
        speak(ctime())

    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on Raj, I will show you where " + location + " is.")
        os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")
    
    if "search" in data:
        data = data.split(" ")
        data2 = str(data[1])
        os.system("chromium-browser 'https://www.google.co.in/search?q='"+ data2  )
 
    if 'bye bye' in data or 'nothing' in data or 'abort' in data or 'stop' in data:
            speak('Bye Sir, have a good day.')
            sys.exit()       


# initialization
time.sleep(2)
speak("Hi Raj, what can I do for you?")
while 1:
    data = recordAudio()
    jarvis(data)



