import webbrowser
import os,sys,re
import webbrowser
import speech_recognition as sr
import wikipedia
import pyttsx3
import smtplib
import datetime
import random
import requests
import subprocess
import youtube_dl
import tkinter as tk
import sqlite3
import re
#import python-vlc
import urllib3
#import urllib2
import json
import wikipedia
import random
from time import strftime
from pyowm import OWM
from bs4 import BeautifulSoup as soup

# from urllib2 import urlopen
print("s")
#github.com/rajmakhijani
engine = pyttsx3.init()
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice', voices[0].id)
def speak(audio):
    '''for the use of assistant speaking'''
    engine.say(audio)
    engine.runAndWait()

def jarvis(data):
    if "how are you" in data:
        speak("I am fine")    
def wishMe():
    '''when you on jarvis first message is done by this wishme'''
    hour = int(datetime.datetime.now().hour)    
    if hour>=0  and hour<12:
        speak("Hello good morning")
    if hour>=12  and hour<18:
        speak("Hello good afternoon")
    elif hour>=18 and hour<=24:    
        speak("Hello good evening")
    speak("I am assistant how may i help you")

def takeCommand():
    '''/take user voice as an input and return the string of the voice'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("please enter the voice")
        print("listenning.....")
        audio= r.listen(source, phrase_time_limit=6)
     

    try:
        print("recognizing...")
        speak("the voice is recognize")
        query = r.recognize_google(audio,language="en-in")    
        print(f"user said: {query}")
        speak('your input is')
        speak(query)
    except Exception as e:
        print(e)
        speak("say that again please")
        return "None"
    return query
 
def stdown():
    speak("if you want to shutdown your pc then say yes")
    qry = takeCommand().lower()
    if 'yes' in qry:
        speak('your request is accepted and pc is started to shutdown')
        os.system("shutdown /s")
    else:
        speak("ok the pc is not shutdown")    

if __name__ == "__main__":
    wishMe()
    rno = random.randint(0,9)
    
    while True:
        query = takeCommand().lower() 
        if 'wikipedia' in query:
            speak("searching wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif 'youtube' in query:
            speak("youtube is opening thank you") 
            webbrowser.open('www.youtube.com')   
        elif 'email' in query:
            speak('Who is the recipient?')
            recipient = myquery()
            if 'nirav' in recipient:
                speak('What should I say to him?')
                content = myquery()
                mail = smtplib.SMTP('smtp.gmail.com', 587)
                mail.ehlo()
                mail.starttls()
                mail.login('niravprajapati@gecg28.ac.in', 'test@463')
                mail.sendmail('niravprajapati@gecg28.ac.in', 'niravprajapati26998@gmail.com', content)
                mail.close()
                speak('Email has been sent successfuly. You can check your inbox.')
            else:
                speak('I don\'t know what you mean!')
        elif 'instagram' in query: 
            speak("instagram is opening thank you") 
            webbrowser.open('www.instagram.com')  
        elif 'music' in query:
            mdir = "C:\\Users\\Nirav\\Music"
            songs = os.listdir(mdir)
            os.startfile(os.path.join(mdir, songs[rno]))     
        elif 'code' in query:
            mdir1= "C:\\Microsoft VS Code\\Code.exe"
            os.startfile(mdir1)
        elif 'vlc' in query:
            mdir2= "C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe"
            os.startfile(mdir2)
        elif 'gta5' in query:
            mdir3= "D:\\GAMES\\GTA V\\PlayGTAV.exe"
            os.startfile(mdir3)
        elif 'shutdown' in query:
            stdown()           

        elif 'time' in query:
            tm = datetime.datetime.now().strftime(f"the date is %D and the time is %H:%M:%S")
            print(tm)
            speak(tm) 
        elif 'video' in query:
            while True: 
                speak("what do you want to search in youtube")
                qr1 = takeCommand().lower()
                print(f"your request is {qr1}")
                if qr1 != "none":
                    url = "https://www.youtube.com/results?search_query={}"
                    search_url = url.format(qr1)
                #print(search_url)
                    webbrowser.open(search_url)
                    speak("your request is fullfilled")
                    break
                else:
                    speak("cant recognize please say that again for your video")
                    continue

        elif 'google' in query:
                #speak("what do you want to search in google")
                while True:
                    speak("what do you want to search in google")
                    qr2 = takeCommand().lower()
                    print(f"your request is {qr2}")
                    if qr2 != "none":
                        url= "https://www.google.com/search?q={}"
                        search_url= url.format(qr2)
                        webbrowser.open(search_url)
                        speak("your request is fullfilled")
                        break
                    else:
                        speak("cant recognize please say that again for your search")
                        continue
        elif 'setting' in query:
            os.system("start ms-settings:")                
        elif 'close' in query:
            speak("bye bye")
            speak("thank you for considering me have a nice day")
            exit()
        elif 'word' in query:
            os.system("start winword")
            speak("word is opening thank you")                
        elif 'powepoint' in query:
            os.system("start powerpnt")
            speak("microsoft powerpoint is opening thank you")                
        elif 'excel' in query:
            os.system("start excel")
            speak("microsoft excel is opening thank you")                    
        elif 'onenote' in query:
            os.system("start OneNote")
            speak("microsoft onenote is opening thank you")               
        elif 'control' in query:
            os.system("control")
            speak("control panel is opening thank you")
        # elif 'current weather' in query:
        #     reg_ex = re.search('current weather in (.*)', query)
        #     if reg_ex:
        #         city = reg_ex.group(1)
        #         owm = OWM(API_key='ab0d5e80e8dafb2cb81fa9e82431c1fa')
        #         obs = owm.weather_at_place(city)
        #         w = obs.get_weather()
        #         k = w.get_status()
        #         x = w.get_temperature(unit='celsius')
        #         speak('Current weather in %s is %s. The maximum temperature is %0.2f and the minimum temperature is %0.2f degree celcius' % (city, k, x['temp_max'], x['temp_min']))
    #time
        # elif 'launch' in query:
        #     reg_ex = re.search('launch (.*)', query)
        #     if reg_ex:
        #         appname = reg_ex.group(1)
        #         appname1 = appname+".app"
        #         subprocess.Popen(["open", "-n", "/Applications/" + appname1], stdout=subprocess.PIPE)
        # speak('I have launched the desired application')               
             
        """ elif 'defender' in query:
            os.system("cd c:\\windows\\system32")
            os.system("\"%ProgramFiles%\\Windows Defender\\MSASCui.exe\" -UpdateAndQuickScan")
            #speak("word is opening thank you")         """  
conn = sqlite3.connect('name.db')
my_cursor = conn.cursor()


sql = "CREATE TABLE IF NOT EXISTS name (dname varchar(50))"
my_cursor.execute(sql)

data_obj = my_cursor.execute("SELECT dname FROM name")
name_of_user = data_obj.fetchone()

root = tk.Tk()
root.title("voice Assistant")
root.geometry('500x500')


entry_log = tk.Text(root)
entry_log.place(y=150, x=250)
entry_log.pack(fill=tk.BOTH)

print(type(entry_log))


def call_init_by_say(*args):
    entry_log.config(state=tk.NORMAL)
    data_obj = my_cursor.execute("SELECT dname FROM name")
    name_of_user = data_obj.fetchone()
    speak(f"Hi {name_of_user[0]}, what can I do for you?")
    while 1:
        data = takeCommand()
        jarvis(data)


say_btn = tk.Button(root, text="Say Something", width=20,
                    bg='brown', fg='white', command=call_init_by_say)
say_btn.place(y=460, x=170)


def insert_into_text(data):
    entry_log.insert(tk.END, data)
    entry_log.pack(side=LEFT, fill=BOTH)
    # entry_log.bind("<1>", lambda event: clicked("address"))


root.mainloop()
       