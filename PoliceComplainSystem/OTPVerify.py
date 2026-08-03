import tkinter as tk

import nexmo
#from pprint import pprint
import random
from complain import *

def check():
    
    if str(entry_otp.get())==secretKey:
        
        print ("User verification successfull. Please Complete the next Coming Form")
        root.destroy()
        complen()
    else:
       
        print("Incorrect OTP")
def verifier(mobileNo):
    global entry_otp
    global secretKey
    global root

    secretPass = str(random.randint(0,9) )+"   " +  str(random.randint(0,9)) +"   " + str(random.randint(0,9)) +"   " + str(random.randint(0,9) )
    
    otp =  " your OTP is ...."+ secretPass
    otp2 = "    .........    I repeat " + otp
    secretPass = secretPass.split()
    secretKey=""
    for i in secretPass:
        if i!=" ":
            secretKey+=i
        
    mobileNo = str(mobileNo)
    
    client = nexmo.Client(
      application_id='619ca1fa-7104-4e90-a72b-ba831956ceb5',
      private_key='private.key',
    )
    ncco = [ {
        'action': 'talk',
        'voiceName': 'Joey',
        'text': otp + otp2
      }]

    response = client.create_call({
      'to': [{
        'type': 'phone',
        'number':  mobileNo
      }],
      'from': {
        'type': 'phone',
        'number': '919726753852'
      },
      'ncco': ncco
    })
    
    root = tk.Tk()
    root.title("Verify OTP")
    #root.state('zoomed')
    root.geometry("350x130")
    root.resizable(0,0)
    f1 = tk.Frame(root)
    f1.grid(row=0,column=0)
    f2 = tk.Frame(root)
    f2.grid(row=1,column=0)
    verifyotp = tk.Label(f1, text="Verify OTP", width=20, font=("bold", 20))
    verifyotp.grid(row=0, column=0)

    otpLabel = tk.Label(f2, text="Enter OTP", width=20, font=("bold", 10),pady=10)
    otpLabel.grid(row=0, column=0)
    entry_otp = tk.Entry(f2,width=25)
    entry_otp.grid(row=0, column=1)

    resendButton = tk.Button(f2, text="Resend OTP",fg='blue',relief="flat")
    resendButton.grid(row=2, column=1)

    submitButton = tk.Button(f2, text="Submit",command = check, bg='brown', fg='white')
    submitButton.grid(row=1, column=1)
    root.mainloop()


