import speech_recognition as sr
import time,os,sys,datetime,pyautogui,ssl,smtplib,requests,re
# from weather import Weather
from gtts import gTTS
# from tkinter import Tk,Text,Label,ttk,Button
# from PIL import ImageTk,Image
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import tkinter as tk
import tkinter.ttk as ttk
from ttkthemes import ThemedStyle
you_x, you_y, you_x_img, you_y_img = 2, 7, 2, 8
eva_x, eva_y, eva_x_img, eva_y_img = 3, 2, 3, 1
global first_time
first_time = True
def greet_user():
    first_time = False
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        tts = gTTS(text = 'Good Morning!', lang = 'en')
        tts.save('audio.mp3')
        os.system('mpg321 audio.mp3')
    elif currentH >= 12 and currentH < 18:
        tts = gTTS(text = 'Good Afternoon!', lang = 'en')
        tts.save('audio.mp3')
        os.system('mpg321 audio.mp3')
    elif currentH >= 18 and currentH != 0:
        tts = gTTS(text = 'Good Evening!', lang = 'en')
        tts.save('audio.mp3')
        os.system('mpg321 audio.mp3')


def speak(audioString, flag):
    if flag == 1:
        audioSting = audioString.strip('You said: ')
        you_img.configure(text="you")
        you_img.update()
        you_txt.configure(text = audioString)
        you_txt.update()
    elif flag == 0:
        eva_img.configure(text="eva")
        eva_img.update()
        eva_txt.configure(text = audioString)
        eva_txt.update()    
    print(audioString)
    tts = gTTS(text = audioString, lang = 'en')
    tts.save('audio.mp3')
    os.system('mpg321 audio.mp3')

def recordAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        audio = r.listen(source, phrase_time_limit = 8)
    data = ""
    try:
        data = r.recognize_google(audio, language = 'en')
        print(data)
        speak('You said: ' + data, 1)
    except sr.UnknownValueError:
        print('EVA could not understand the audio')
    except sr.RequestError as e:
        print('Could not request results from service; {0}'.format(e))
    return data

def facebook():
    option = Options()
    option.add_argument("--disable-notifications")
    driver = webdriver.Chrome(chrome_options = option)
    driver.maximize_window()
    driver.get("https://www.facebook.com")
    email = "voiceassistant2479@gmail.com"#pyautogui.prompt("Please enter your email used to make Facebook account")
    password = "ajax@2479"#pyautogui.password("Please enter the password for the Facebook account")
    driver.find_element_by_id('email').send_keys(email)
    driver.find_element_by_id('pass').send_keys(password + "\n")
    choice = pyautogui.prompt('Text or Image?')
    flag = 1
    while flag == 1:
        if choice == "text":
            message = "Hey! How you doing?"
            driver.find_element_by_xpath("//*[@name='xhpc_message']").send_keys(message)
            time.sleep(2)
            buttons = driver.find_elements_by_tag_name('button')
            for button in buttons:
                if 'Post' in button.text:
                    button.click()
                    flag = 0
        elif choice == "image":
            choice = pyautogui.prompt("Enter the exact name of the image with extension you want to upload")
            driver.find_element_by_link_text('Photo/Video').click()
            time.sleep(1)
            search = pyautogui.locateOnScreen('search.png')
            pyautogui.click(search)
            time.sleep(1)
            pyautogui.typewrite(choice + "\n")
            time.sleep(2)
            pyautogui.hotkey('down')
            pyautogui.typewrite('\n')
            time.sleep(2)
            buttons = driver.find_elements_by_tag_name('button')
            for button in buttons:
                if 'Post' in button.text:
                    button.click()
            flag = 0 
    time.sleep(4)
    driver.close()

def google_maps():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://maps.google.com")
    wait = WebDriverWait(driver,20)
    wait.until(EC.visibility_of_element_located((By.ID, 'widget-mylocation')))
    driver.find_element_by_id('widget-mylocation').click()
    place = pyautogui.prompt('Enter the name of place you want to search')
    driver.find_element_by_id('searchboxinput').send_keys(place + '\n')
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'iRxY3GoUYUY__icon')))
    choice = pyautogui.prompt('Would you like to switch to Satellite view?')
    if choice.lower() == 'yes':
        driver.find_element_by_xpath('//*[@id="minimap"]/div/div[2]/button').click()
    choice = pyautogui.prompt('Would you like to switch to Map View?')
    if choice.lower() == 'yes':
        driver.find_element_by_xpath('//*[@id="minimap"]/div/div[2]/button').click()
    choice = pyautogui.prompt('Would you like to see all photos of this place?')
    if choice.lower() == 'yes':
        driver.find_element_by_id('card-label-All').click()
        time.sleep(4)
        buttons = driver.find_elements_by_tag_name('button')
        for button in buttons:
            if button.get_attribute('aria-label') == 'Back':
                button.click()
    wait.until(EC.visibility_of_element_located((By.ID, 'widget-mylocation')))
    choice = pyautogui.prompt('Would you like to see the reviews of this place?')
    time.sleep(4)
    driver.close()

def google_search():
    option = Options()
    option.add_argument("--disable-notifications")
    driver = webdriver.Chrome(chrome_options = option)
    driver.maximize_window()
    driver.get("https://www.google.com")
    search = pyautogui.prompt('Enter what you want to search')
    driver.find_element_by_name('q').send_keys(search + '\n')
    time.sleep(4)
    driver.close()

def mail():
    rec_name = pyautogui.prompt('Enter the name of the receiver')
    def get_mail(filename):
        names = []
        emails = []
        with open(filename, mode='r', encoding='utf-8' ) as contacts_file:
            for a_contact in contacts_file:
                names.append(a_contact.split()[0])
                emails.append(a_contact.split()[1])
        return names, emails
    names, emails = get_mail('contacts.txt')
    email = emails[names.index(rec_name.lower())]
    msg = pyautogui.prompt('Enter the message you want to enter')
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login('voiceassistant2479@gmail.com', 'ajax@2479')
    mail.sendmail('voiceassistant2479@gmail.com',email,msg)
    mail.close()

def EVA(data):
    if 'how are you' in data:
        speak('I am fine. Thank you for asking.', 0)
    if 'time' in data:
        speak(time.ctime(), 0)
    if 'bye-bye' in data or 'bye bye' in data or 'close' in data or 'exit' in data:
        speak('Thank you for letting me help you.', 0)
        sys.exit()
    if 'google search' in data or 'search' in data or 'google' in data:
        google_search()
    if 'joke' in data:
        res = requests.get('https://icanhazdadjoke.com/', headers={"Accept":"application/json"})
        speak(res.json()['joke'], 0)
    if 'current weather in' in data:
        reg_ex = re.search('current weather in (.*)', data)
        if reg_ex:
            city = reg_ex.group(1)
            weather = Weather()
            location = weather.lookup_by_location(city)
            condition = location.condition()
            speak('The Current weather in %s is %s The tempeture is %.1f degree' % (city, condition.text(), (int(condition.temp())-32)/1.8), 0)

    if 'weather forecast in' in data:
        reg_ex = re.search('weather forecast in (.*)', data)
        if reg_ex:
            city = reg_ex.group(1)
            weather = Weather()
            location = weather.lookup_by_location(city)
            forecasts = location.forecast()
            for i in range(0,3):
                speak('On %s will it %s. The maximum temperture will be %.1f degree. The lowest temperature will be %.1f degrees.' % (forecasts[i].date(), forecasts[i].text(), (int(forecasts[i].high())-32)/1.8, (int(forecasts[i].low())-32)/1.8), 0)

def started(*args):
        if first_time == True:
            greet_user()
        micactive.configure(text = 'Listening!')
        micactive.update()
        data = recordAudio()
        micactive.configure(text = 'Not Listening!')
        micactive.update()
        EVA(data)



root = tk.Tk()
root.geometry('500x300')
root.title("EVA")

style = ThemedStyle(root)
style.set_theme("equilux")

frame_cont = tk.Frame(root, width=500, height=250,)
frame_cont.configure(bg='black')
frame_cont.pack()


frame_bottom = tk.Frame(root, width=500, height=50,)
frame_bottom.configure(bg="white")
frame_bottom.pack(side=tk.BOTTOM)


# img_you = ImageTk.PhotoImage(Image.open('C:/Users/Harshid/Downloads/Project Modules-20200331T061028Z-001/Project Modules/YOU.png'))
# img_eva = ImageTk.PhotoImage(Image.open('C:/Users/Harshid/Downloads/Project Modules-20200331T061028Z-001/Project Modules/EVA.png'))

micactive = tk.Label(frame_cont,text = 'Not Listening!', background = "black", foreground = "white")
micactive.grid(row = 1, column =3)

you_img = ttk.Label(frame_cont,
                    background="black", font=('Verdana', 16, 'bold'))
you_img.grid(row=you_x_img, column=you_y_img, padx=10, pady=10)
eva_img = ttk.Label(frame_cont,
                    background="black", font=('Verdana', 16, 'bold'))
eva_img.grid(row=eva_x_img, column=eva_y_img, padx=10, pady=10)


you_txt = ttk.Label(frame_cont, background="black",
                    foreground="white", font=('Verdana', 12))
you_txt.grid(row=you_x, column=you_y, pady=10)
eva_txt = ttk.Label(frame_cont, background="black",
                    foreground="white", font=('Verdana', 12))
eva_txt.grid(row=eva_x, column=eva_y, pady=10)


# img_giffy = ImageTk.PhotoImage(Image.open('C:/Users/Harshid/Downloads/Project Modules-20200331T061028Z-001/Project Modules/giphy.gif'))
giffy_img = ttk.Button(frame_bottom, text="Speak", command = started)
giffy_img.pack()
root.configure(bg='black')
root.mainloop()
