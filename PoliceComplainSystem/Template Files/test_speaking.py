
from gtts import gTTS 
import winsound 
from googletrans import Translator
import os
#from pygame import mixer
import playsound
import datetime


def clicked():
    
    
    translator =Translator()
 
    
    
    #translated = translator.translate("A, dest=language)
    myobj = gTTS(text="Aadhaaar number", lang="en", slow=False) 
    
    
    myobj.save("aadhaarnumber.mp3") 


    #os.system("welcome.wav") 
    #winsound.PlaySound('welcome.wav', winsound.SND_ALIAS)
    '''mixer.init()
    mixer.music.load("welcome.mp3")
    mixer.music.play()
    mixer.quit()'''
    #playsound.playsound("welcome.mp3",True)
    #os.remove("welcome.mp3")
    #myobj.close("welcome.mp3")

    
clicked()
