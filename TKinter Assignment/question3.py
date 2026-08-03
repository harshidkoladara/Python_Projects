from tkinter import *
import tkinter.messagebox as tkMessageBox


#load tkinter object and give it the title
root = Tk()
root.title("Calculator")


# Add method for adding the values
def add():
    try:
        value =  inputfeild.get()
        if len(value) == 0: #check feild is empty or not
            raise ValueError()
        if value.isdigit() == False: # check entered value is number or not
            tkMessageBox.showwarning('Error', 'Please enter the number only', icon="warning") # error message 
        else:
            value = int(total_value['text']) + int(value) 
            total_value.config(text = value) # add value to the total feild
    except:
        tkMessageBox.showwarning('Error', 'Please enter the value', icon="warning") # error message
    finally:
        inputfeild.delete(0,END)

def subtract():
    try:
        value =  inputfeild.get()
        if len(value) == 0: #check feild is empty or not
            raise ValueError()
        if value.isdigit() == False: # check entered value is number or not
            tkMessageBox.showwarning('Error', 'Please enter the number only', icon="warning") # error message
        else:
            value = int(total_value['text']) - int(value)
            total_value.config(text = value) # add value to the total feild
    except:
        tkMessageBox.showwarning('Error', 'Please enter the value', icon="warning") # error message
    finally:
        inputfeild.delete(0,END)

# Create frame for white backgroung
frame = Frame(root,bg="#FFFFFF")

# Total label
total_label = Label(frame, text="Total:", bg='#FFFFFF', font=("bold", 10))
total_label.grid(row=0, column=0, padx= (5, 0), pady=(0, 5), sticky = W)

# Total Value
total_value = Label(frame, text="0", bg='#FFFFFF', font=("bold", 10))
total_value.grid(row=0, column=2, padx= (5, 10), pady=(0, 5), sticky = E)

# Input field entry box
inputfeild = Entry(frame, bg='#FFFFFF', border="1", width=40)
inputfeild.grid(row=1, column=0, padx= (5, 10), pady=(0, 5), columnspan=3)

Button(frame, text="+", bg='#FFFFFF', width=2, border="1", command= lambda : add()).grid(row=2, column=0, padx=(1, 0), pady=(0, 10)) # add button
Button(frame, text="-", bg='#FFFFFF', width=2, border="1", command= lambda : subtract()).grid(row=2, column=1, padx=(20, 20), pady=(0, 10)) # substract button
Button(frame, text="Reset", bg='#FFFFFF', width=6, border="1", command= lambda : total_value.config(text=0)).grid(row=2, column=2, padx= (5, 10), pady=(0, 10)) # reset button

#setup grid for frame and configure rows and column
frame.grid(row=0, column=0, sticky="NESW")
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

#configure row and column for root window
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

#run loop over main Window
root.mainloop()