import tkinter as tk
import requests
import sys
import os
from tkinter.filedialog import askopenfile
from sign_log_pyre import LogSign


root = tk.Tk()

root.geometry('500x500')

image_source = str()


def select_img(*a):
    global image_source

    image = askopenfile(title='Open', mode='r',
                        filetypes=[('Image Files', ['.jpeg', '.jpg', '.png', '.gif',
                                                    '.tiff', '.tif', '.bmp'])])
    image_path = os.path.dirname(image.name)
    image_name = os.path.basename(image.name)
    image_source = f'{image_path}/{image_name}'


def sign_in_to_fire(*args):

    if(len(entry_name.get()) == 0):
        global name_msg
        name_msg = tk.Label(root, text="Name Field Must Required",
                            width=20, font=("bold", 8), pady=10, fg='red')
        name_msg.grid(row=3, column=4)
    elif(len(image_source) == 0):

        try:
            name_msg.grid_forget()
        except:
            pass

        global img_msg
        img_msg = tk.Label(root, text="Must select the Image",
                           width=20, font=("bold", 8), pady=10, fg='red')
        img_msg.grid(row=5, column=4)
    elif(len(entry_id.get()) == 0):

        try:
            img_msg.grid_forget()
        except:
            pass

        global id_msg
        id_msg = tk.Label(root, text="Email Field Must Required",
                          width=20, font=("bold", 8), pady=10, fg='red')
        id_msg.grid(row=7, column=4)
    elif(len(entry_password.get()) == 0):

        try:
            id_msg.grid_forget()
        except:
            pass

        global pass_msg
        pass_msg = tk.Label(root, text="Password Field Must reqired",
                            width=20, font=("bold", 8), pady=10, fg='red')
        pass_msg.grid(row=9, column=4)
    else:

        try:
            pass_msg.grid_forget()
        except:
            pass

        sign = LogSign()
        a = sign.signin_method(name=entry_name.get(), email=entry_id.get(
        ), password=entry_password.get(), img_src=image_source)
        msg = tk.Label(root, text=str(a), width=20,
                       font=("bold", 12), pady=10, fg='green')
        msg.grid(row=11, column=4)


def login_module(*args):

    root.destroy()
    import gui_log


login_btn = tk.Button(root, text='Log In', fg='white',
                      bg='brown', command=login_module)
login_btn.grid(row=0, column=5)

name = tk.Label(root, text="Name", width=20, font=("bold", 12), pady=10)
name.grid(row=2, column=2)
entry_name = tk.Entry(root, width=35)
entry_name.grid(row=2, column=4)

upload_img_btn = tk.Button(root, text='Upload Profile',
                           fg='white', bg='brown', command=select_img)
upload_img_btn.grid(row=4, column=4)

id = tk.Label(root, text="Email ID", width=20, font=("bold", 12), pady=10)
id.grid(row=6, column=2)
entry_id = tk.Entry(root, width=35)
entry_id.grid(row=6, column=4)

password = tk.Label(root, text="Password", width=20,
                    font=("bold", 12), pady=10)
password.grid(row=8, column=2)
entry_password = tk.Entry(root, width=35)
entry_password.grid(row=8, column=4)


signin_btn = tk.Button(root, text='Sign In', fg='white',
                       bg='brown', command=sign_in_to_fire)
signin_btn.grid(row=10, column=4)

tk.mainloop()
