import tkinter as tk
import os
from PIL import ImageTk, Image
from sign_log_pyre import LogSign

root = tk.Tk()
root.geometry('500x500')


def log_to_fire(*args):
    if(len(entry_id.get()) == 0):
        global id_msg
        id_msg = tk.Label(root, text="Email Field Must Required",
                          width=20, font=("bold", 8), pady=10, fg='red')
        id_msg.grid(row=5, column=4)
    elif(len(entry_password.get()) == 0):

        try:
            id_msg.grid_forget()
        except:
            pass

        global password_msg
        password_msg = tk.Label(root, text="Password Field Must Required",
                                width=20, font=("bold", 8), pady=10, fg='red')
        password_msg.grid(row=7, column=4)

    else:

        try:
            password_msg.grid_forget()
        except:
            pass

        login = LogSign()
        data_src = login.login_method(email=entry_id.get(),
                                      password=entry_password.get())
        msg = tk.Label(root, text=data_src[0], width=20,
                       font=("bold", 12), pady=10, fg='green')
        msg.grid(row=10, column=4)

        data = data_src[1]

        profile_img = Image.open(data_src[2])
        profile_img = profile_img.resize((100, 100), Image.ANTIALIAS)
        profile_img = ImageTk.PhotoImage(profile_img)
        panel = tk.Label(root, image=profile_img)
        panel.image = profile_img
        panel.grid(row=12, column=2)

        name_msg_show = tk.Label(root, text="Name : " + data['name'], width=20,
                                 font=("bold", 12), pady=10, fg='green')
        name_msg_show.grid(row=14, column=2)

        email_msg_show = tk.Label(root, text="Email : " + data['email'], width=20,
                                  font=("bold", 12), pady=10, fg='green')
        email_msg_show.grid(row=16, column=2)

        # img = ImageTk.PhotoImage(Image.open(data_src[2]))
        # panel = tk.Label(root, image = img)
        # panel.grid(row=14, column=2)
        # panel.pack(side = "bottom")


def signin_module(*args):

    root.destroy()
    import gui_sign_pyre


signin_btn = tk.Button(root, text='Sign In', fg='white',
                       bg='brown', command=signin_module)
signin_btn.grid(row=2, column=5)

id = tk.Label(root, text="Email ID", width=20, font=("bold", 12), pady=10)
id.grid(row=4, column=2)
entry_id = tk.Entry(root, width=35)
entry_id.grid(row=4, column=4)

password = tk.Label(root, text="Password", width=20,
                    font=("bold", 12), pady=10)
password.grid(row=6, column=2)
entry_password = tk.Entry(root, width=35)
entry_password.grid(row=6, column=4)

login_btn = tk.Button(root, text='Log In', fg='white',
                      bg='brown', command=log_to_fire)
login_btn.grid(row=8, column=4)

tk.mainloop()
