import tkinter as tk
from mainfile import *

from googletrans import Translator
from tkcalendar import DateEntry

from OTPVerify import verifier
from QRScanner import capture
import playsound,os
root = tk.Tk()
translator = Translator()

tags = ["Select Language", "Registration form", "Enter Your Name", "Birth date", "Mobile  Number", "Email", "Aadhaar Number", "Gender",
        "Address", "Male", "Female", "Scan Aadhaar", 'Get OTP']
tanslated = ["Select Language", "Registration form", "Enter Your Name", "Birth date", "Mobile Number", "Email", "Aadhaar Number",
             "Gender", "Address", "Male", "Female", "Scan Aadhaar", 'Get OTP']
state = ['Gujarat', 'Maharastra', 'UP']

root.title("Complain Register")
#root.state('zoomed')
root.geometry("650x500")
root.resizable(0,0)
f1 = tk.Frame(root)
f1.grid(row=0,column=0)
f2 =tk.Frame(root)
f2.grid(row=1,column=0)
def qrscanner_and_datafiller():
    xmldict = capture()
    datadict = xmldict['PrintLetterBarcodeData']
    udi_d = datadict['@uid']
    name_d = datadict['@name']
    gender_d = datadict['@gender']
    yob_d = datadict['@yob']
    
    house_d = datadict['@house']
    street_d = datadict['@street']
    
    loc_d = datadict['@loc']
    vtc_d = datadict['@vtc']
    po_d = datadict['@po']
    dist_d = datadict['@dist']
    subdist_d = datadict['@subdist']
    state_d = datadict['@state']
    pc_d = datadict['@pc']
    dob_d = datadict['@dob']

    entry_name.insert(0, name_d)
    entry_aadhaar.insert(0, udi_d)

    if gender_d == 'M':
        var.set(1)
    else:
        var.set(2)

    address_d = f"{house_d}, {street_d}," \
                f" \n {vtc_d}, {dist_d}," \
                f" \n{state_d} - {pc_d}"
    entry_address.insert(tk.END, address_d)

    cal_entry.set_date(dob_d)


def config_label():
    lang.config(text=tanslated[0])
    registrationForm.config(text=tanslated[1])
    name.config(text=tanslated[2])
    cal.config(text=tanslated[3])
    phone.config(text=tanslated[4])
    email.config(text=tanslated[5])
    adhaar_no.config(text=tanslated[6])
    sex.config(text=tanslated[7])
    address.config(text=tanslated[8])
    radio_male.config(text=tanslated[9])
    radio_female.config(text=tanslated[10])
    scanButton.config(text=tanslated[11])
    get_otp_btn.config(text=tanslated[12])

listOfLangCode = ["bn", "en", "gu", "hi", "ml", "mr", "ta","te","ur"]
listOfLang = ["Bengali","English","Gujarati","Hindi","Malayalam","Marathi","Tamil","Telagu","Urdu"]
def lang_changed(*a):
    global code
    i = 0
    change= 0
    
    for j in range(0,len(listOfLang)):
        if variable.get() == listOfLang[j]:
            change = j
            code = listOfLangCode[j]
        
    for x in tags:
        translating = translator.translate(x, src='en', dest=listOfLangCode[change])
        a = tags.index(x)
        tanslated.insert(a, translating.text)
        lang.config(text=tanslated[0])
    root.update_idletasks()
    config_label()

def clicked(text):

    
    lang=variable.get()
    for i in range(len(listOfLang)):
        if(lang == listOfLang[i]):
            lang=listOfLangCode[i]
    
    
    #print(translating.text)
    fil=""
    
    file=(text).split()
    
    for i in file:
        fil+=i
    file="speaker/"+lang+"/"+fil+".mp3"
    
    
    file=file.lower()
    playsound.playsound(file,True)
    






lang = tk.Label(f2, text="Select Language", width=20, font=("bold", 12),pady=10)
lang.grid(row=2, column=2)
variable = tk.StringVar(root)
variable.set('English')
entry_lang = tk.OptionMenu(f2, variable, "Bengali","English","Gujarati","Hindi","Malayalam","Marathi","Tamil","Telagu","Urdu")
entry_lang.grid(row=2, column=6)
entry_lang.config(width=10, font=('Helvetica', 12))
variable.trace('w', lang_changed)

registrationForm = tk.Label(f1, text=tanslated[1], width=20, font=("Algerian", 20, "bold"))
registrationForm.grid(row=1, column=1)

scanButton = tk.Button(f2, text="Scan Aadhaar", width=20, bg='brown', fg='white', command=qrscanner_and_datafiller)
scanButton.grid(row=2, column=7)

name = tk.Label(f2, text="Enter Your Name", width=20, font=("bold", 12),pady=10)
name.grid(row=3, column=2)
entry_name = tk.Entry(f2,width=35)
entry_name.grid(row=3, column=6)

entry_name.bind("<1>",lambda event:clicked("enter your name"))

cal = tk.Label(f2, text="Birth date", width=20, font=("bold", 12),pady=10)
cal.grid(row=4, column=2)
cal_entry = DateEntry(f2, width=30, background='darkblue', foreground='white', borderwidth=2)
cal_entry.grid(row=4, column=6)

phone = tk.Label(f2, text="Mobile number", width=20, font=("bold", 12),pady=10)
phone.grid(row=5, column=2)
entry_phone = tk.Entry(f2,width=35)
entry_phone.grid(row=5, column=6)
entry_phone.bind("<1>",lambda event:clicked("mobile number"))

email = tk.Label(f2, text="Email", width=20, font=("bold", 12),pady=10)
email.grid(row=7, column=2)
entry_email = tk.Entry(f2,width=35)
entry_email.grid(row=7, column=6)
entry_email.bind("<1>",lambda event:clicked("email"))

adhaar_no = tk.Label(f2, text="Aadhaar Number", width=20, font=("bold", 12),pady=10)
adhaar_no.grid(row=8, column=2)
entry_aadhaar = tk.Entry(f2,width=35)
entry_aadhaar.grid(row=8, column=6)
entry_aadhaar.bind("<1>",lambda event:clicked("aadhaar number"))

f3 = tk.Frame(f2)
f3.grid(row=9,column=6)
sex = tk.Label(f2, text="Gender", width=20, font=("bold", 12),pady=10)
sex.grid(row=9, column=2)
var = tk.IntVar()
radio_male = tk.Radiobutton(f3, text="Male", variable=var, value=1)
radio_male.grid(row=0, column=0)
tk.Label(f3,text="  ").grid(row=0,column=1)
radio_female = tk.Radiobutton(f3, text="Female", variable=var, value=2)
radio_female.grid(row=0, column=2)

address = tk.Label(f2, text="Address", width=20, font=("bold", 12),pady=10)
address.grid(row=11, column=2)
entry_address = tk.Text(f2,height=5,width=27)
entry_address.grid(row=11, column=6)
entry_address.bind("<1>",lambda event:clicked("address"))
tk.Label(f2,text="").grid(row=12,column=6)



get_otp_btn = tk.Button(f2, text='Get OTP', width=20, bg='brown', fg='white', command=lambda : verifier(entry_phone.get()))
get_otp_btn.grid(row=13, column=6)
root.mainloop()

