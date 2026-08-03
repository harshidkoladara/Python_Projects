from tkinter import *

#load tkinter object and give it the title
root = Tk()
root.title("A simple GUI")

# Create frame for white backgroung
frame = Frame(root,bg="#FFFFFF")

Label(frame, text="This is our first GUI!", bg='#FFFFFF', font=("bold", 10)).grid(row=0, column=1, padx=100, pady=(0, 5)) # main label
Button(frame, text="Greet", bg='#FFFFFF', width=6, border="1", command= lambda : print("Hello Python!")).grid(row=1, column=1, pady=(0, 2)) #Greet button
Button(frame, text="Close", bg='#FFFFFF', width=6, border="1", command= lambda : root.quit()).grid(row=2, column=1, pady=(0, 20)) #Close button

#setup grid for frame and configure rows and column
frame.grid(row=0, column=0, sticky="NESW")
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

#configure row and column for root window
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

#run loop over main Window
root.mainloop()