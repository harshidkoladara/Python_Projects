import datetime
import mysql.connector
import ctypes,os
from tkinter import *
import tkinter.messagebox as tkMessageBox
from tkcalendar import Calendar,DateEntry
from PIL import ImageTk, Image

conn = mysql.connector.connect(user='root', password='root', host='localhost', database='hospital')
cursor = conn.cursor()
cursor.execute("USE hospital")
cursor.execute("CREATE TABLE IF NOT EXISTS department(dept_id int NOT NULL AUTO_INCREMENT PRIMARY KEY, name varchar(52), hod varchar(52))")
cursor.execute("CREATE TABLE IF NOT EXISTS doctors(doc_id int NOT NULL AUTO_INCREMENT PRIMARY KEY, name varchar(52), dob DATE, contact varchar(12), specialization varchar(52), department_id varchar(52))")
cursor.execute("CREATE TABLE IF NOT EXISTS patients(patient_id int NOT NULL AUTO_INCREMENT PRIMARY KEY, name varchar(52), dob DATE, contact varchar(12), disease varchar(52), department_id varchar(52), doctor_id varchar(52))")



#load tkinter object and give it the title
window = Tk()
window.title("Hospital Management System")

user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
lt = [w, h]
a = str(lt[0]//2-446)
b= str(lt[1]//2-383)

window.geometry("1214x680+"+a+"+"+b)
window.resizable(0,0)



frame = Frame(window, highlightbackground="orange", highlightthickness=2, bg="#FFFFFF")
doctor_frame = Frame(window, highlightbackground="orange", highlightthickness=2, bg="#FFFFFF")
department_frame = Frame(window, highlightbackground="orange", highlightthickness=2, bg="#FFFFFF")
show_patient_frame = Frame(window, highlightbackground="orange", highlightthickness=2, bg="#FFFFFF")
show_doctor_frame = Frame(window, highlightbackground="orange", highlightthickness=2, bg="#FFFFFF")
show_department_frame = Frame(window, highlightbackground="orange", highlightthickness=2, bg="#FFFFFF")

def clear_all_grids():
    try:
        frame.place_forget()
    except:
        pass
    try:
        doctor_frame.place_forget()
    except:
        pass
    try:
        department_frame.place_forget()
    except:
        pass
    try:
        show_patient_frame.place_forget()
    except:
        pass
    try:
        show_doctor_frame.place_forget()
    except:
        pass
    try:
        show_department_frame.place_forget()
    except:
        pass

def add_patient_operation():
    clear_all_grids()

    def add_patient():
        patient_name_value = patient_full_name_entry.get()
        patient_dob_value = patient_dob.get()
        patient_contact_value = patient_contact.get()
        patient_disease_value = patient_disease.get()
        patient_department_value = patient_department_variable.get()
        patient_doctor_value = patient_doctor_variable.get()

        cursor.execute("INSERT INTO patients (name , dob , contact , disease , department_id , doctor_id) VALUES (%s, %s, %s, %s, %s, %s)", (patient_name_value, patient_dob_value, patient_contact_value, patient_disease_value, patient_department_value, patient_doctor_value))
        conn.commit()
        show_all_patients()

    
    Label(frame, text="Patient Details", fg="orange", font=("Arial", 18), bg="#FFFFFF").grid(row=1, column=0, sticky = W, padx=(5, 20))

    patient_full_name = Label(frame, text="FullName", font=("Arial", 16), height=2, bg="#FFFFFF")
    patient_full_name.grid(row=2, column=0, padx= (5, 0), pady=(5, 5), sticky = W)
    patient_full_name_entry = Entry(frame, bg='#FFFFFF', border="1", width=22, font=("Arial", 16))
    patient_full_name_entry.grid(row=2, column=1, padx= (5, 10), pady=(0, 5), sticky = E, columnspan=2)


    patient_dob_label = Label(frame, text="Date Of Birth", font=("Arial", 16), height=2, bg="#FFFFFF")
    patient_dob_label.grid(row=3, column=0, padx= (5, 0), pady=(5, 5), sticky = W)
    patient_dob = DateEntry(frame,width=20,bg="darkblue",fg="white",year=2021, font=("Arial", 16))
    patient_dob.grid(row=3, column=1, padx= (5, 10), pady=(0, 5), sticky = E, columnspan=2)

    patient_contact_label = Label(frame, text="Contact", font=("Arial", 16), height=2, bg="#FFFFFF")
    patient_contact_label.grid(row=4, column=0, padx= (5, 0), pady=(5, 5), sticky = W)
    patient_contact = Entry(frame, bg='#FFFFFF', border="1", width=22, font=("Arial", 16))
    patient_contact.grid(row=4, column=1, padx= (5, 10), pady=(0, 5), sticky = E, columnspan=2)

    patient_disease_label = Label(frame, text="Disease", font=("Arial", 16), height=2, bg="#FFFFFF")
    patient_disease_label.grid(row=5, column=0, padx= (5, 0), pady=(5, 5), sticky = W)
    patient_disease = Entry(frame, bg='#FFFFFF', border="1", width=22, font=("Arial", 16))
    patient_disease.grid(row=5, column=1, padx= (5, 10), pady=(0, 5), sticky = E, columnspan=2)

    DEPARTMETS = [
        "Select docotor's department"
    ]

    cursor.execute("SELECT name FROM department")

    for x in list(cursor.fetchall()):
        DEPARTMETS.append(x[0])

    patient_department_label = Label(frame, text="Department ", font=("Arial", 16), height=2, bg="#FFFFFF")
    patient_department_label.grid(row=6, column=0, padx= (5, 0), pady=(0, 5), sticky = W)
    patient_department_variable = StringVar(frame)
    patient_department_variable.set(DEPARTMETS[0])
    patient_department_dropdown = OptionMenu(frame, patient_department_variable, *DEPARTMETS)
    patient_department_dropdown.config(font=("Arial Narrow",12,"bold"))
    patient_department_dropdown.config(width=30)
    patient_department_dropdown.config(bg="white")
    patient_department_dropdown.config(fg="black")
    patient_department_dropdown.config(activeforeground="black")
    patient_department_dropdown.config(activebackground="white")
    patient_department_dropdown.grid(row=6, column=1, padx= (5, 10), pady=(0, 5), sticky = E, columnspan=2)

    DOCTOR = [
        "Select docotor"
    ]

    cursor.execute("SELECT name FROM doctors")


    for x in list(cursor.fetchall()):
        DOCTOR.append(x[0])

    patient_doctor_label = Label(frame, text="Doctor", font=("Arial", 16), height=2, bg="#FFFFFF")
    patient_doctor_label.grid(row=7, column=0, padx= (5, 0), pady=(0, 5), sticky = W)
    patient_doctor_variable = StringVar(frame)
    patient_doctor_variable.set(DOCTOR[0])
    patient_doctor_dropdown = OptionMenu(frame, patient_doctor_variable, *DOCTOR)
    patient_doctor_dropdown.config(font=("Arial Narrow",12,"bold"))
    patient_doctor_dropdown.config(width=30)
    patient_doctor_dropdown.config(bg="white")
    patient_doctor_dropdown.config(fg="black")
    patient_doctor_dropdown.config(activeforeground="black")
    patient_doctor_dropdown.config(activebackground="white")
    patient_doctor_dropdown.grid(row=7, column=1, padx= (5, 10), pady=(0, 5), sticky = E, columnspan=2)

    Button(frame, text="Submit", bg='#FF0000',fg="#FFFFFF", border="1", font=("bold", 10), width=18, command= lambda : add_patient()).grid(row=8, column=0, columnspan=3, pady=(10, 20)) # submit button

    frame.place(x=550, y = 100)

def add_doctor_operation():
    clear_all_grids()
    
    def add_doctor():
        full_name_value = doctor_full_name_entry.get()
        dob_value = doctor_dob.get()
        contact_value = doctor_contact.get()
        specialization_value = doctor_specialization.get()
        department_value = doctor_department_variable.get()

        if specialization_value == "Select docotor's department":
            specialization_value = ""
        cursor.execute("INSERT INTO doctors (name , dob, contact , specialization , department_id) VALUES (%s, %s, %s, %s, %s)", (full_name_value, dob_value, contact_value, specialization_value, department_value))
        conn.commit()
        show_all_doctors()

    
    Label(doctor_frame, text="Doctor Details", fg="orange", font=("Arial", 18), bg="#FFFFFF").grid(row=1, column=0, sticky = W, padx=(5, 20))

    doctor_full_name = Label(doctor_frame, text="FullName", font=("Arial", 16), height=2, bg="#FFFFFF")
    doctor_full_name.grid(row=2, column=0, padx= (5, 0), pady=(5, 5), sticky = W)
    doctor_full_name_entry = Entry(doctor_frame, bg='#FFFFFF', border="1", width=22, font=("Arial", 16))
    doctor_full_name_entry.grid(row=2, column=1, padx= (5, 10), pady=(0, 5), sticky = E, columnspan=2)


    doctor_dob_label = Label(doctor_frame, text="Date Of Birth", font=("Arial", 16), height=2, bg="#FFFFFF")
    doctor_dob_label.grid(row=3, column=0, padx= (5, 0), pady=(5, 5), sticky = W)
    doctor_dob = DateEntry(doctor_frame,width=20,bg="darkblue",fg="white",year=2021, font=("Arial", 16))
    doctor_dob.grid(row=3, column=1, padx= (5, 10), pady=(0, 5), sticky = E, columnspan=2)

    doctor_contact_label = Label(doctor_frame, text="Contact", font=("Arial", 16), height=2, bg="#FFFFFF")
    doctor_contact_label.grid(row=4, column=0, padx= (5, 0), pady=(5, 5), sticky = W)
    doctor_contact = Entry(doctor_frame, bg='#FFFFFF', border="1", width=22, font=("Arial", 16))
    doctor_contact.grid(row=4, column=1, padx= (5, 10), pady=(0, 5), sticky = E, columnspan=2)

    doctor_specialization_label = Label(doctor_frame, text="Specialization", font=("Arial", 16), height=2, bg="#FFFFFF")
    doctor_specialization_label.grid(row=5, column=0, padx= (5, 0), pady=(5, 5), sticky = W)
    doctor_specialization = Entry(doctor_frame, bg='#FFFFFF', border="1", width=22, font=("Arial", 16))
    doctor_specialization.grid(row=5, column=1, padx= (5, 10), pady=(0, 5), sticky = E, columnspan=2)


    DEPARTMETS = [
        "Select docotor's department"
    ]

    cursor.execute("SELECT name FROM department")

    for x in list(cursor.fetchall()):
        DEPARTMETS.append(x[0])

    doctor_department_label = Label(doctor_frame, text="Department ", font=("Arial", 16), height=2, bg="#FFFFFF")
    doctor_department_label.grid(row=6, column=0, padx= (5, 0), pady=(0, 5), sticky = W)
    doctor_department_variable = StringVar(doctor_frame)
    doctor_department_variable.set(DEPARTMETS[0])
    doctor_department_dropdown = OptionMenu(doctor_frame, doctor_department_variable, *DEPARTMETS)
    doctor_department_dropdown.config(font=("Arial Narrow",12,"bold"))
    doctor_department_dropdown.config(width=30)
    doctor_department_dropdown.config(bg="white")
    doctor_department_dropdown.config(fg="black")
    doctor_department_dropdown.config(activeforeground="black")
    doctor_department_dropdown.config(activebackground="white")
    doctor_department_dropdown.grid(row=6, column=1, padx= (5, 10), pady=(0, 5), sticky = E, columnspan=2)

    Button(doctor_frame, text="Submit", bg='#FF0000',fg="#FFFFFF", border="1", font=("bold", 10), width=18, command= lambda : add_doctor()).grid(row=7, column=0, columnspan=3, pady=(10, 20)) # submit button

    doctor_frame.place(x = 550, y = 125)

def add_department_operation():
    clear_all_grids()

    def add_dept():
        name = full_name_entry.get()
        doctor = doctor_variable.get()
        if doctor == "Select doctor":
            doctor = ""
        cursor.execute("INSERT INTO department (name, hod) VALUES (%s, %s)", (name, doctor))
        conn.commit()
        show_all_departments()

    
    Label(department_frame, text="Department Details", fg="orange", font=("Arial", 18), bg="#FFFFFF").grid(row=1, column=0, sticky = W, padx=(5, 20))

    full_name = Label(department_frame, text="Name", font=("Arial", 16), height=2, bg="#FFFFFF")
    full_name.grid(row=2, column=0, padx= (5, 0), pady=(5, 5), sticky = W)
    full_name_entry = Entry(department_frame, bg='#FFFFFF', border="1", width=22, font=("Arial", 16))
    full_name_entry.grid(row=2, column=1, padx= (5, 10), pady=(0, 5), sticky = E, columnspan=2)


    DOCTOR = [
        "Select doctor"
    ]

    cursor.execute("SELECT name FROM doctors")


    for x in list(cursor.fetchall()):
        DOCTOR.append(x[0])

    doctor_label = Label(department_frame, text="Doctor", font=("Arial", 16), height=2, bg="#FFFFFF")
    doctor_label.grid(row=3, column=0, padx= (5, 0), pady=(0, 5), sticky = W)
    doctor_variable = StringVar(department_frame)
    doctor_variable.set(DOCTOR[0])
    doctor_dropdown = OptionMenu(department_frame, doctor_variable, *DOCTOR)
    doctor_dropdown.config(font=("Arial Narrow",12,"bold"))
    doctor_dropdown.config(width=30)
    doctor_dropdown.config(bg="white")
    doctor_dropdown.config(fg="black")
    doctor_dropdown.config(activeforeground="black")
    doctor_dropdown.config(activebackground="white")
    doctor_dropdown.grid(row=3, column=1, padx= (5, 10), pady=(0, 5), sticky = E, columnspan=2)

    Button(department_frame, text="Submit", bg='#FF0000',fg="#FFFFFF", border="1", font=("bold", 10), width=18, command= lambda : add_dept()).grid(row=4, column=0, columnspan=3, pady=(10, 20)) # submit button

    department_frame.place(x = 550, y = 250)

def show_all_patients():
    clear_all_grids()
    cursor.execute("SELECT * FROM patients")
    Label(show_patient_frame, text="ID", font=("Arial Narrow",12,"bold"), width=2, bd=1, borderwidth='1', bg="orange", fg="#6444BB").grid(row=4, column=1, ipadx=5, padx=(2, 4), pady=3)
    Label(show_patient_frame, text="NAME", font=("Arial Narrow",12,"bold"), width=10, bd=1, borderwidth='1', bg="orange", fg="#6444BB").grid(row=4, column=2, ipadx=5, pady=3)
    Label(show_patient_frame, text="DOB", font=("Arial Narrow",12,"bold"), width=10, bd=1, borderwidth='1', bg="orange", fg="#6444BB").grid(row=4, column=3, ipadx=5, padx=(4, 2), pady=3)
    Label(show_patient_frame, text="CONTACT", font=("Arial Narrow",12,"bold"), width=10, bd=1, borderwidth='1', bg="orange", fg="#6444BB").grid(row=4, column=4, ipadx=5, padx=(4, 2), pady=3)
    Label(show_patient_frame, text="DISEASE", font=("Arial Narrow",12,"bold"), width=10, bd=1, borderwidth='1', bg="orange", fg="#6444BB").grid(row=4, column=5, ipadx=5, padx=(4, 2), pady=3)
    Label(show_patient_frame, text="DEPARTMENT", font=("Arial Narrow",12,"bold"), width=10, bd=1, borderwidth='1', bg="orange", fg="#6444BB").grid(row=4, column=6, ipadx=5, padx=(4, 2), pady=3)
    Label(show_patient_frame, text="DOCTOR", font=("Arial Narrow",12,"bold"), width=10, bd=1, borderwidth='1', bg="orange", fg="#6444BB").grid(row=4, column=7, ipadx=5, padx=(4, 2), pady=3)

    for i, item in enumerate(cursor.fetchall()):
        Label(show_patient_frame, text=item[0], font=("Arial Narrow",12,"bold"), width=2, bd=1, borderwidth='1', bg="#6444BB", fg="orange").grid(row=i+5, column=1, ipadx=5, padx=(2, 4), pady=(0, 2))
        Label(show_patient_frame, text=item[1], font=("Arial Narrow",12,"bold"), width=10, bd=1, borderwidth='1', bg="#6444BB", fg="orange").grid(row=i+5, column=2, ipadx=5, pady=(0, 2))
        Label(show_patient_frame, text=str(item[2])[2:], font=("Arial Narrow",12,"bold"), width=10, bd=1, borderwidth='1', bg="#6444BB", fg="orange").grid(row=i+5, column=3, ipadx=5, padx=(4, 2), pady=(0, 2))
        Label(show_patient_frame, text=item[3], font=("Arial Narrow",12,"bold"), width=10, bd=1, borderwidth='1', bg="#6444BB", fg="orange").grid(row=i+5, column=4, ipadx=5, padx=(4, 2), pady=(0, 2))
        Label(show_patient_frame, text=item[4], font=("Arial Narrow",12,"bold"), width=10, bd=1, borderwidth='1', bg="#6444BB", fg="orange").grid(row=i+5, column=5, ipadx=5, padx=(4, 2), pady=(0, 2))
        Label(show_patient_frame, text=item[5], font=("Arial Narrow",12,"bold"), width=10, bd=1, borderwidth='1', bg="#6444BB", fg="orange").grid(row=i+5, column=6, ipadx=5, padx=(4, 2), pady=(0, 2))
        Label(show_patient_frame, text=item[5], font=("Arial Narrow",12,"bold"), width=10, bd=1, borderwidth='1', bg="#6444BB", fg="orange").grid(row=i+5, column=7, ipadx=5, padx=(4, 2), pady=(0, 2))
        
    show_patient_frame.place(x = 550, y = 120)

def show_all_doctors():
    clear_all_grids()
    cursor.execute("SELECT * FROM doctors")
    Label(show_doctor_frame, text="ID", font=("Arial Narrow",12,"bold"), width=2, bd=1, borderwidth='1', bg="orange", fg="#6444BB").grid(row=4, column=1, ipadx=5, padx=(2, 4), pady=3)
    Label(show_doctor_frame, text="NAME", font=("Arial Narrow",12,"bold"), width=10, bd=1, borderwidth='1', bg="orange", fg="#6444BB").grid(row=4, column=2, ipadx=5, pady=3)
    Label(show_doctor_frame, text="DOB", font=("Arial Narrow",12,"bold"), width=10, bd=1, borderwidth='1', bg="orange", fg="#6444BB").grid(row=4, column=3, ipadx=5, padx=(4, 2), pady=3)
    Label(show_doctor_frame, text="CONTACT", font=("Arial Narrow",12,"bold"), width=10, bd=1, borderwidth='1', bg="orange", fg="#6444BB").grid(row=4, column=4, ipadx=5, padx=(4, 2), pady=3)
    Label(show_doctor_frame, text="SPECIALIZATION", font=("Arial Narrow",12,"bold"), width=15, bd=1, borderwidth='1', bg="orange", fg="#6444BB").grid(row=4, column=5, ipadx=5, padx=(4, 2), pady=3)
    Label(show_doctor_frame, text="DEPARTMENT", font=("Arial Narrow",12,"bold"), width=10, bd=1, borderwidth='1', bg="orange", fg="#6444BB").grid(row=4, column=6, ipadx=5, padx=(4, 2), pady=3)

    for i, item in enumerate(cursor.fetchall()):
        Label(show_doctor_frame, text=item[0], font=("Arial Narrow",12,"bold"), width=2, bd=1, borderwidth='1', bg="#6444BB", fg="orange").grid(row=i+5, column=1, ipadx=5, padx=(2, 4), pady=(0, 2))
        Label(show_doctor_frame, text=item[1], font=("Arial Narrow",12,"bold"), width=10, bd=1, borderwidth='1', bg="#6444BB", fg="orange").grid(row=i+5, column=2, ipadx=5, pady=(0, 2))
        Label(show_doctor_frame, text=str(item[2])[2:], font=("Arial Narrow",12,"bold"), width=10, bd=1, borderwidth='1', bg="#6444BB", fg="orange").grid(row=i+5, column=3, ipadx=5, padx=(4, 2), pady=(0, 2))
        Label(show_doctor_frame, text=item[3], font=("Arial Narrow",12,"bold"), width=10, bd=1, borderwidth='1', bg="#6444BB", fg="orange").grid(row=i+5, column=4, ipadx=5, padx=(4, 2), pady=(0, 2))
        Label(show_doctor_frame, text=item[4], font=("Arial Narrow",12,"bold"), width=15, bd=1, borderwidth='1', bg="#6444BB", fg="orange").grid(row=i+5, column=5, ipadx=5, padx=(4, 2), pady=(0, 2))
        Label(show_doctor_frame, text=item[5], font=("Arial Narrow",12,"bold"), width=10, bd=1, borderwidth='1', bg="#6444BB", fg="orange").grid(row=i+5, column=6, ipadx=5, padx=(4, 2), pady=(0, 2))
        
    show_doctor_frame.place(x = 550, y = 120)

def show_all_departments():
    clear_all_grids()
    cursor.execute("SELECT * FROM department")
    Label(show_department_frame, text="ID", font=("Arial Narrow",12,"bold"), width=2, bd=1, borderwidth='1', bg="orange", fg="#6444BB").grid(row=4, column=1, ipadx=5, padx=(2, 4), pady=3)
    Label(show_department_frame, text="NAME", font=("Arial Narrow",12,"bold"), width=10, bd=1, borderwidth='1', bg="orange", fg="#6444BB").grid(row=4, column=2, ipadx=5, pady=3)
    Label(show_department_frame, text="HOD", font=("Arial Narrow",12,"bold"), width=20, bd=1, borderwidth='1', bg="orange", fg="#6444BB").grid(row=4, column=3, ipadx=5, padx=(4, 2), pady=3)
    
    for i, item in enumerate(cursor.fetchall()):
        Label(show_department_frame, text=item[0], font=("Arial Narrow",12,"bold"), width=2, bd=1, borderwidth='1', bg="#6444BB", fg="orange").grid(row=i+5, column=1, ipadx=5, padx=(2, 4), pady=(0, 2))
        Label(show_department_frame, text=item[1], font=("Arial Narrow",12,"bold"), width=10, bd=1, borderwidth='1', bg="#6444BB", fg="orange").grid(row=i+5, column=2, ipadx=5, pady=(0, 2))
        Label(show_department_frame, text=str(item[2])[2:], font=("Arial Narrow",12,"bold"), width=20, bd=1, borderwidth='1', bg="#6444BB", fg="orange").grid(row=i+5, column=3, ipadx=5, padx=(4, 2), pady=(0, 2))
        
    show_department_frame.place(x = 650, y = 120)

def operation_buttons():
        global operation_buttons_frame, sort_button
        operation_buttons_frame = Frame(window, highlightbackground="orange", highlightthickness=2, bg="#FFFFFF")
        
        Button(operation_buttons_frame, text="ADD PATIENT", font=("Arial Narrow",16,"bold"), width=15, bd=1, borderwidth='1', bg="#6444BB", fg="white", activebackground="#6444BB", activeforeground="#EDF9FD", command= lambda: add_patient_operation()).grid(row=1, column=1, ipadx=30, padx=50, pady=(50, 10), sticky=W)
        Button(operation_buttons_frame, text="ADD DOCTOR", font=("Arial Narrow",16,"bold"), width=15, bd=1, borderwidth='1', bg="#6444BB", fg="white", activebackground="#6444BB", activeforeground="#EDF9FD", command= lambda: add_doctor_operation()).grid(row=2, column=1, ipadx=30, padx=50, pady=10, sticky=W)
        Button(operation_buttons_frame, text="ADD DEPARTMENT", font=("Arial Narrow",16,"bold"), width=15, bd=1, borderwidth='1', bg="#6444BB", fg="white", activebackground="#6444BB", activeforeground="#EDF9FD", command= lambda: add_department_operation()).grid(row=3, column=1, ipadx=30, padx=50, pady=10, sticky=W)
        Button(operation_buttons_frame, text="SHOW PATIENS", font=("Arial Narrow",16,"bold"), width=15, bd=1, borderwidth='1', bg="#6444BB", fg="white", activebackground="#6444BB", activeforeground="#EDF9FD", command= lambda: show_all_patients()).grid(row=4, column=1, ipadx=30, padx=50, pady=10, sticky=W)
        Button(operation_buttons_frame, text="SHOW DOCTORS", font=("Arial Narrow",16,"bold"), width=15, bd=1, borderwidth='1', bg="#6444BB", fg="white", activebackground="#6444BB", activeforeground="#EDF9FD", command= lambda: show_all_doctors()).grid(row=5, column=1, ipadx=30, padx=50, pady=10, sticky=W)
        Button(operation_buttons_frame, text="SHOW DEPARTMENTS", font=("Arial Narrow",16,"bold"), width=15, bd=1, borderwidth='1', bg="#6444BB", fg="white", activebackground="#6444BB", activeforeground="#EDF9FD", command= lambda: show_all_departments()).grid(row=6, column=1, ipadx=30, padx=50, pady=(10, 50), sticky=W)
        
        operation_buttons_frame.place(x=100, y=100)

operation_buttons()
add_patient_operation()
#run loop over main Window


img = ImageTk.PhotoImage(Image.open("logo.png"))
window.iconphoto(False, img)

  
window.configure(background='#FFFFFF')
window.mainloop()