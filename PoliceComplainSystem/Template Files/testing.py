from tkinter import *
from test_speaking import *
import os
root = Tk()


labelName = Label(root,text="Enter Your Name:")
labelName.grid(row=0,column=0)

entryName = Entry(root)
#entryName.insert(END,"Enter your Name")

entryName.grid(row=0,column=1)


labelRoll = Label(root,text="Enter Your Mobile number:")
labelRoll.grid(row=1,column=0)
entryRoll = Entry(root)
#entryRoll.insert(END,"Enter your Roll Number")

entryRoll.grid(row=1,column=1)


entryName.bind("<1>",lambda event:clicked(labelName.cget("text"),"hi"))
entryRoll.bind("<1>",lambda event:clicked(labelRoll.cget("text"),"hi"))

def rem():
    os.rmdir("songs")
Button(root,text="remove",command=rem).grid(row=2,column=1)
mainloop()
