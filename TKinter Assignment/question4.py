import pycountry
from tkinter import *
import tkinter.messagebox as tkMessageBox


#load tkinter object and give it the title
root = Tk()
root.title("Registration Form")


# submit method called on submission of form
def submit():
    # declaring varible and fetching the values
    empty_feilds = []
    name = full_name_entry.get()
    email = email_entry.get()
    gender = v.get()
    country = country_variable.get()
    java = java_variable.get()
    python = python_variable.get()


    if len(name) == 0: #checking name field is empty or not
        empty_feilds.append("FullName")
    if len(email) == 0: #checking email field is empty or not
        empty_feilds.append("Email")
    if gender == 0: # checking gender is selected or not
        empty_feilds.append("Gender")
    if country == "Select your country": #checking country is selected or not
        empty_feilds.append("Country")
    if java == 0 and python == 0: #checking progamming is selected or not
        empty_feilds.append('Programming')

    #converting gender value integer sign to string 
    if gender == 1:
        gender = "male"
    elif gender == 2:
        gender = "female"

    # getting selected programming language 
    programming_language = ""
    programming_language = "java" if java == 1 else ""
    if len(programming_language) == 0:  
        programming_language += "python" if python == 1 else ""
    else:
        programming_language += ", python" if python == 1 else ""


    if len(empty_feilds) > 0:
        warning_str = "Please fill the below missing feilds,\n" # Error message 
        for x in empty_feilds:
            warning_str += x + ",\n"
        tkMessageBox.showwarning('Error', warning_str, icon="warning") 
    else:
        # Writing form data into .txt file
        with open('Registration_form_data.txt', 'a') as f:
            f.write(f"---------------------------------\n")
            f.write(f"FullName: {name}\n")
            f.write(f"Email: {email}\n")
            f.write(f"Gender: {gender}\n")
            f.write(f"Country: {country}\n")
            f.write(f"Programming: {programming_language}\n")



#creating frame
frame = Frame(root)

# frame title
Label(frame, text="Registration form", font=("bold", 18), height=2).grid(row=0, column=0, columnspan=3)

#name label and input feild
full_name = Label(frame, text="FullName", font=("Arial", 10), height=2)
full_name.grid(row=2, column=0, padx= (5, 0), pady=(5, 5), sticky = W)
full_name_entry = Entry(frame, bg='#FFFFFF', border="1", width=22)
full_name_entry.grid(row=2, column=1, padx= (5, 0), pady=(0, 5), sticky = E, columnspan=2)

# email label and input feild
email = Label(frame, text="Email", font=("Arial", 10), height=2)
email.grid(row=3, column=0, padx= (5, 0), pady=(0, 5), sticky = W)
email_entry = Entry(frame, bg='#FFFFFF', border="1", width=22)
email_entry.grid(row=3, column=1, padx= (5, 0), pady=(0, 5), sticky = E, columnspan=2)


# gender label and radio button
v = IntVar()
gender = Label(frame, text="Gender", font=("Arial", 10), height=2)
gender.grid(row=4, column=0, padx= (5, 0), pady=(0, 5), sticky = W)
Radiobutton(frame, text="Male", variable=v, value=1).grid(row=4, column=1)
Radiobutton(frame, text="Female",  variable=v, value=2).grid(row=4, column=2)


# Country list and it's label and dropdown
COUNTRIES = [
    "Select your country"
]

for x in list(pycountry.countries):
    COUNTRIES.append(x.name)

country = Label(frame, text="Country", font=("Arial", 10), height=2)
country.grid(row=5, column=0, padx= (5, 0), pady=(0, 5), sticky = W)
country_variable = StringVar(frame)
country_variable.set(COUNTRIES[0])
country_dropdown = OptionMenu(frame, country_variable, *COUNTRIES)
country_dropdown.grid(row=5, column=1, padx= (5, 0), pady=(0, 5), sticky = E, columnspan=2)


# programming label and checkbox
programming = Label(frame, text="Programming", font=("Arial", 10), height=2)
programming.grid(row=6, column=0, padx= (5, 10), pady=(0, 5), sticky = E)
java_variable = IntVar()
python_variable = IntVar()
java_checkbox = Checkbutton(frame, text = "java", variable = java_variable, onvalue = 1, offvalue = 0)
java_checkbox.grid(row=6, column=1)
python_checkbox = Checkbutton(frame, text = "python", variable = python_variable, onvalue = 1, offvalue = 0)
python_checkbox.grid(row=6, column=2)

Button(frame, text="Submit", bg='#FF0000',fg="#FFFFFF", border="1", font=("bold", 10), width=18, command= lambda : submit()).grid(row=7, column=0, columnspan=3, pady=(10, 0)) # submit button

#setup grid for frame and configure rows and column
frame.grid(row=0, column=0, padx=100, pady=(50, 75), sticky="NESW")
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

#configure row and column for root window
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

#run loop over main Window
root.mainloop()