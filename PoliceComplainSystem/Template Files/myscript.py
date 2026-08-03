from gtts import gTTS 
#import winsound 
from googletrans import Translator
import googletrans
import os
languages = googletrans.LANGUAGES



text_list=["Enter Your Name", "Birth date", "Mobile  Number", "Email", "Aadhaar Number",
           "Address","Enter Your Complain Statement","Enter Witness Name","Enter Victim Name","Enter Your OTP"]

translator = Translator()


for langauge in languages:
    l=languages[langauge].lower()
    if(l=="telugu" or l=="tamil" or l=="urdu" or l=="malayalam"
       or l=="bengali" or l=="english" or l=="hindi" or l=="gujarati" or l=="marathi"):
            for text in text_list:
                #translating = translator.translate(text, dest=langauge)
                #text=translating.text
                filename=text.split()
                file=""
                for k in filename:
                    file+=k
                #filename=filename.join(',')
                file+=".mp3"

                file=file.lower()

                if(not os.path.isdir(langauge)):
                    os.mkdir(langauge)
                file=langauge+"/"+file

                translator =Translator()
 
                translated = translator.translate(text, dest=langauge)
                myobj = gTTS(text=translated.text, lang=langauge, slow=False) 
                    
                    
                    
                myobj.save(file) 
               
                



