from tkinter import *

#load tkinter object and give it the title
root = Tk()
root.title("Form")

# Create frame for white backgroung
frame = Frame(root,bg="#FFFFFF")

# name label and it's entry box for input
Label(frame, text="Name:", bg='#FFFFFF', font=("bold", 10)).grid(row=0, column=0, padx= (5, 0), pady=(0, 5), sticky = W)
namefeild = Entry(frame, bg='#FFFFFF', border="1", width=25)
namefeild.grid(row=0, column=1, padx= (0, 5), pady=(0, 5))

# email label and it's entry box for input
Label(frame, text="Email Address:", bg='#FFFFFF', font=("bold", 10)).grid(row=1, column=0, padx= (5, 0), pady=(0, 10), sticky = W)
emailfeild = Entry(frame, bg='#FFFFFF', border="1", width=25)
emailfeild.grid(row=1, column=1, padx= (0, 5), pady=(0, 5))

Button(frame, text="Quit", bg='#FFFFFF', width=6, border="1", command= lambda : root.quit()).grid(row=2, column=0, padx=(1, 0), pady=(0, 2), sticky = W) #button for quiting the window
Button(frame, text="Show", bg='#FFFFFF', width=6, border="1", command= lambda : print(f"Name: {namefeild.get()} \nEmail: {emailfeild.get()}")).grid(row=2, column=1, pady=(0, 2)) #button for printing the name and email

#setup grid for frame and configure rows and column
frame.grid(row=0, column=0, sticky="NESW")
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

#configure row and column for root window
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

#run loop over main Window
root.mainloop()