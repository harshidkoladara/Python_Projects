
from gtts import gTTS 
import winsound 
from googletrans import Translator
import os
from pygame import mixer


translator =Translator()
 
mytext = input("ENter TExt")
lan = input("enter language code")
translated = translator.translate(mytext, dest=lan)

print (translated.text)
#print(type(translated))
 
language = lan


myobj = gTTS(text=translated.text, lang=language, slow=False) 


myobj.save("welcome.wav") 


#os.system("welcome.wav") 
winsound.PlaySound('welcome.wav', winsound.SND_ALIAS)
#mixer.init()
#mixer.music.load("welcome.mp3")
#mixer.music.play()
