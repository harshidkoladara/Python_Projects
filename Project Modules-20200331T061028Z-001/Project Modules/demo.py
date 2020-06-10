from tkinter import Tk,Text,Label
from tkinter import ttk
from PIL import ImageTk,Image
t = Tk()
t.title('EVA')
t.geometry('500x300')
img1 = ImageTk.PhotoImage(Image.open('YOU.png'))
img2 = ImageTk.PhotoImage(Image.open('EVA.png'))
you_tn = Label(t,image = img1)
eva_tn = Label(t,image = img2)
you_txt = Label(t,text = 'hello how are you? this is a tkinter program for dummy content please bear with me', background = 'grey', height = 7, width = 50, wraplength = 250)
eva_txt = Label(t, background = 'grey', height = 7, width = 50)
mic_active = Label(t, text = 'Sound Not Detected!')
mic_active.grid(column = 1, row = 0)
you_tn.grid(column = 0, row = 1)
eva_tn.grid(column = 2, row = 2)
you_txt.grid(column = 1, row = 1)
eva_txt.grid(column = 1, row = 2, pady = 1)
t.mainloop()