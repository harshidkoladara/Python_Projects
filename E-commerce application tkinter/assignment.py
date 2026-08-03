import os
import sys
import ctypes
from tkinter import *
import tkinter.filedialog as filedialog


# Class Items
class Item:
    def __init__(self, item, type, quantity) -> None:
        self.item = item
        self.type = type
        self.quantity = quantity


# Class Ecommerce
class ECommerce:
    def __init__(self, file) -> None:
        self.file = file
        self.items = self.read_file()

    # Read text file and add the items
    def read_file(self):
        with open(self.file, 'r') as fl:
            data = fl.readlines()
        all_items = []
        for i in range(0, len(data), 3):
            all_items.append(Item(data[i].rstrip('\n'), data[i+1].rstrip('\n'), int(data[i+2].rstrip('\n'))))
        return all_items

    # Write into the text file
    def write_item(self):
        with open(self.file, 'w') as fl:
            for x in self.items:
                fl.write(x.item + '\n')
                fl.write(x.type + '\n')
                fl.write(str(x.quantity) + '\n')

    # Store Items, args -> (item, type, quantity)
    def store_item(self, item, type, quantity):
        for x in self.items:
            if x.item.lower() == item.lower() and x.type.lower() == type.lower():
                x.quantity += int(quantity)
                self.write_item()
                break
        else:
            self.items.append(Item(item, type, int(quantity)))
            self.write_item()

    # Display Items, all the items and items by the type
    def display_items(self, type=None):
        if type:
            items = []
            for item in self.items:
                if item.type.lower() == type.lower():
                    items.append(item)
            return items
        else:
            return self.items

    # Edit items, args -> (item, quantity)
    def edit_item(self, item, quantity):
        for current_item in self.items:
            if current_item.item.lower() == item.lower():
                current_item.quantity = quantity
                break
        self.write_item()

    # Delete one item, args -> (item)
    def delete_item(self, item):
        all_items = self.items
        for current_item in all_items:
            if current_item.item.lower() == item.lower():
                self.items.remove(current_item)
        self.write_item()

    # SORT Items, args -> (ascending : bool)
    def sort_items(self, ascending=True):
        if ascending:
            self.items.sort(key=lambda x: x.item, reverse=False)
        else:
            self.items.sort(key=lambda x: x.item, reverse=True)
        self.write_item()

    def get_categories(self):
        categories = []
        for x in self.items:
            categories.append(x.type)
        return categories


if __name__ == '__main__':
    root = Tk()

    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    [w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
    lt = [w, h]
    a = str(lt[0]//2-446)
    b= str(lt[1]//2-383)

    root.title("E-commerce application")
    root.geometry("1264x680+"+a+"+"+b)
    root.resizable(0,0)


    ##################SHOW ALL ITEMS#################### 
    def forget_all_frame_grid():
        global operation_buttons_frame, items_frame, edit_item_frame, delete_item_frame, add_item_frame
        try:
            operation_buttons_frame
        except:
            pass
        try:
            items_frame.place_forget()
        except:
            pass
        try:
            edit_item_frame.place_forget()
        except:
            pass
        try:
            delete_item_frame.place_forget()
        except:
            pass
        try:
            add_item_frame.place_forget()
        except:
            pass

    def all_item_button_data(items_frame, items):
        global items_frame_i
        items_frame_i = Frame(items_frame, highlightbackground="orange", highlightthickness=2, bg="#FFFFFF")
        Label(items_frame_i, text="Item", font=("Arial Narrow",16,"bold"), width=15, bd=1, borderwidth='1', bg="orange", fg="#6444BB").grid(row=4, column=1, ipadx=25, padx=(2, 4), pady=3)
        Label(items_frame_i, text="Type", font=("Arial Narrow",16,"bold"), width=15, bd=1, borderwidth='1', bg="orange", fg="#6444BB").grid(row=4, column=2, ipadx=25, pady=3)
        Label(items_frame_i, text="Quantity", font=("Arial Narrow",16,"bold"), width=15, bd=1, borderwidth='1', bg="orange", fg="#6444BB").grid(row=4, column=3, ipadx=25, padx=(4, 2), pady=3)

        for i, item in enumerate(items):
            Label(items_frame_i, text=item.item, font=("Arial Narrow",16,"bold"), width=15, bd=1, borderwidth='1', bg="#6444BB", fg="orange").grid(row=i+5, column=1, ipadx=25, padx=(2, 4), pady=(0, 2))
            Label(items_frame_i, text=item.type, font=("Arial Narrow",16,"bold"), width=15, bd=1, borderwidth='1', bg="#6444BB", fg="orange").grid(row=i+5, column=2, ipadx=25, pady=(0, 2))
            Label(items_frame_i, text=item.quantity, font=("Arial Narrow",16,"bold"), width=15, bd=1, borderwidth='1', bg="#6444BB", fg="orange").grid(row=i+5, column=3, ipadx=25, padx=(4, 2), pady=(0, 2))
        
        items_frame_i.grid(row=4, column=1, columnspan=3, padx=10)
    
    def all_item_button_event():
        global items_frame
        forget_all_frame_grid()
        items_frame = Frame(root, highlightbackground="orange", highlightthickness=2, bg="#FFFFFF")
        items_frame.place(x=500, y=50, width=700, height=580)
    
        items = e.display_items()

        TYPES = [
        "ALL TYPE"
        ]

        for x in e.get_categories():
            TYPES.append(x)

        type_variable = StringVar(items_frame)
        type_variable.set(TYPES[0])
        type_dropdown = OptionMenu(items_frame, type_variable, *TYPES)
        type_dropdown.config(width=70)
        type_dropdown.config(bg="#6444BB")
        type_dropdown.config(fg="white")
        type_dropdown.config(activeforeground="#6444BB")
        type_dropdown.config(activebackground="orange")
        type_dropdown.grid(row=1, column=1, padx= (5, 0), pady=(25, 40), sticky = E, columnspan=2, rowspan=3)

        Button(items_frame, text="SELECT", font=("Arial Narrow",16,"bold"), width=15, bd=1, borderwidth='1', bg="#6444BB", fg="white", activebackground="#6444BB", activeforeground="#EDF9FD", command= lambda : select_category()).grid(row=1, column=3, pady=(20, 45))

        def select_category():
            global items, items_frame_i
            if type_variable.get() == "ALL TYPE":
                items = e.display_items()
                all_item_button_data(items_frame, items)
            else:
                # Select items by type
                items = e.display_items(type_variable.get())
            items_frame_i.grid_forget()
            all_item_button_data(items_frame, items)

        all_item_button_data(items_frame, items)



    ################EDIT ITEM###############
    def edit_item_button_event():
        global edit_item_frame
        forget_all_frame_grid()
        edit_item_frame = Frame(root, highlightbackground="orange", highlightthickness=2, bg="#FFFFFF") 
        edit_item_frame_data(edit_item_frame)
        edit_item_frame.place(x=550, y=240, width=580, height=220)
        
    def edit_item_frame_data(edit_item_frame):
        ITEMS = []

        for x in e.display_items():
            ITEMS.append(x.item)
        
        Label(edit_item_frame, text="EDIT ITEM", font=("Arial Narrow",12,"bold"), width=15, bd=1, borderwidth='1', bg="white", fg="#6444BB" ).grid(row=0, column=1, columnspan=3)
        Label(edit_item_frame, text="Select Item: ", font=("Arial Narrow",16,"bold"), width=15, bd=1, borderwidth='1', bg="white", fg="#6444BB" ).grid(row=1, column=1,  padx=10)
        item_variable = StringVar(edit_item_frame)
        item_variable.set(ITEMS[0])
        item_dropdown = OptionMenu(edit_item_frame, item_variable, *ITEMS)
        item_dropdown.config(font=("Arial Narrow",16,"bold"))
        item_dropdown.config(width=30)
        item_dropdown.config(bg="#6444BB")
        item_dropdown.config(fg="white")
        item_dropdown.config(activeforeground="#6444BB")
        item_dropdown.config(activebackground="orange")
        item_dropdown.grid(row=1, column=2, padx= 10, pady=(20, 10))

        Label(edit_item_frame, text="Quantity", font=("Arial Narrow",16,"bold"), width=15, bd=1, borderwidth='1', bg="white", fg="#6444BB" ).grid(row=2, column=1)
        weight_entry = Entry(edit_item_frame, font=("Arial Narrow",16,"bold"), width=30, bd=1, borderwidth='2', bg="white", fg="#6444BB")
        weight_entry.grid(row=2, column=2, padx= 10, pady=10)

        def edit_item_quantity():
            # Edit item
            e.edit_item(item_variable.get(), weight_entry.get())
            all_item_button_event()
            
        Button(edit_item_frame, text="EDIT", font=("Arial Narrow",16,"bold"), width=20, bd=1, borderwidth='1', bg="#6444BB", fg="white", activebackground="#6444BB", activeforeground="#EDF9FD", command= lambda : edit_item_quantity()).grid(row=3, column=1, padx= 10, pady=(10, 20), columnspan=2)
    



################ DELETE ITEM ###############
    def delete_item_button_event():
        global delete_item_frame
        forget_all_frame_grid()
        delete_item_frame = Frame(root, highlightbackground="orange", highlightthickness=2, bg="#FFFFFF") 
        delete_item_frame_data(delete_item_frame)
        delete_item_frame.place(x=550, y=240, width=605, height=180)
        
    def delete_item_frame_data(delete_item_frame): 
        ITEMS = []

        for x in e.display_items():
            ITEMS.append(x.item)
            delete_item_frame.grid_forget()
            
        Label(delete_item_frame, text="DELETE ITEM", font=("Arial Narrow",12,"bold"), width=15, bd=1, borderwidth='1', bg="white", fg="#6444BB" ).grid(row=0, column=1, columnspan=3)
        Label(delete_item_frame, text="Select Item: ", font=("Arial Narrow",16,"bold"), width=15, bd=1, borderwidth='1', bg="white", fg="#6444BB" ).grid(row=1, column=1,  padx=10)
        item_variable = StringVar(delete_item_frame)
        item_variable.set(ITEMS[0])
        item_dropdown = OptionMenu(delete_item_frame, item_variable, *ITEMS)
        item_dropdown.config(font=("Arial Narrow",16,"bold"))
        item_dropdown.config(width=30)
        item_dropdown.config(bg="#6444BB")
        item_dropdown.config(fg="white")
        item_dropdown.config(activeforeground="#6444BB")
        item_dropdown.config(activebackground="orange")
        item_dropdown.grid(row=1, column=2, padx= 10, pady=(20, 10))

        
        def delete_item():
            # Delete Item 
            e.delete_item(item_variable.get())
            delete_item_frame.place_forget()
            all_item_button_event()

        Button(delete_item_frame, text="DELETE", font=("Arial Narrow",16,"bold"), width=20, bd=1, borderwidth='1', bg="#6444BB", fg="white", activebackground="#6444BB", activeforeground="#EDF9FD", command= lambda : delete_item()).grid(row=3, column=1, padx= 10, pady=(10, 20), columnspan=2)
    



################ ADD ITEM###############

    def add_item_button_event():
        global add_item_frame
        forget_all_frame_grid()
        add_item_frame = Frame(root, highlightbackground="orange", highlightthickness=2, bg="#FFFFFF") 
        add_item_frame_data(add_item_frame)
        add_item_frame.place(x=550, y=220, width=580, height=250)

    def add_item_frame_data(add_item_frame):
        ITEMS = []

        for x in e.display_items():
            ITEMS.append(x.item)
        
        Label(add_item_frame, text="ADD ITEM", font=("Arial Narrow",12,"bold"), width=15, bd=1, borderwidth='1', bg="white", fg="#6444BB" ).grid(row=0, column=1, columnspan=3)
        
        Label(add_item_frame, text="Item: ", font=("Arial Narrow",16,"bold"), width=15, bd=1, borderwidth='1', bg="white", fg="#6444BB" ).grid(row=2, column=1)
        add_item_entry = Entry(add_item_frame, font=("Arial Narrow",16,"bold"), width=30, bd=1, borderwidth='2', bg="white", fg="#6444BB")
        add_item_entry.grid(row=2, column=2, padx= 10, pady=10)
        
        Label(add_item_frame, text="Type: ", font=("Arial Narrow",16,"bold"), width=15, bd=1, borderwidth='1', bg="white", fg="#6444BB" ).grid(row=3, column=1)
        add_type_entry = Entry(add_item_frame, font=("Arial Narrow",16,"bold"), width=30, bd=1, borderwidth='2', bg="white", fg="#6444BB")
        add_type_entry.grid(row=3, column=2, padx= 10, pady=10)

        Label(add_item_frame, text="Quantity", font=("Arial Narrow",16,"bold"), width=15, bd=1, borderwidth='1', bg="white", fg="#6444BB" ).grid(row=4, column=1)
        add_quantity_entry = Entry(add_item_frame, font=("Arial Narrow",16,"bold"), width=30, bd=1, borderwidth='2', bg="white", fg="#6444BB")
        add_quantity_entry.grid(row=4, column=2, padx= 10, pady=10)

        
        def add_item():
            # Store Item
            e.store_item(add_item_entry.get(), add_type_entry.get(), int(add_quantity_entry.get()))
            all_item_button_event()

        Button(add_item_frame, text="ADD ITEM", font=("Arial Narrow",16,"bold"), width=20, bd=1, borderwidth='1', bg="#6444BB", fg="white", activebackground="#6444BB", activeforeground="#EDF9FD", command= lambda : add_item()).grid(row=5, column=1, padx= 10, pady=(10, 20), columnspan=2)
        

    ################ SORT ITEM ###############
    def sort_items():
        if sort_button['text'] == "SORT ASCENDING":
            # SORT ASCENDING
            e.sort_items(ascending=True)
            sort_button['text'] = 'SORT DESCENDING'
        else:
            # SORT DESCENDING
            e.sort_items(ascending=False)
            sort_button['text'] = 'SORT ASCENDING'

        all_item_button_event()

    ############# OPERATION BUTTON #########
    def operation_buttons():
        global operation_buttons_frame, sort_button
        operation_buttons_frame = Frame(root, highlightbackground="orange", highlightthickness=2, bg="#FFFFFF")
        
        Button(operation_buttons_frame, text="DISPLAY ITEMS", font=("Arial Narrow",16,"bold"), width=15, bd=1, borderwidth='1', bg="#6444BB", fg="white", activebackground="#6444BB", activeforeground="#EDF9FD", command= lambda: all_item_button_event()).grid(row=1, column=1, ipadx=30, padx=50, pady=(50, 10), sticky=W)
        Button(operation_buttons_frame, text="EDIT ITEM", font=("Arial Narrow",16,"bold"), width=15, bd=1, borderwidth='1', bg="#6444BB", fg="white", activebackground="#6444BB", activeforeground="#EDF9FD", command= lambda: edit_item_button_event()).grid(row=2, column=1, ipadx=30, padx=50, pady=10, sticky=W)
        Button(operation_buttons_frame, text="DELETE ITEM", font=("Arial Narrow",16,"bold"), width=15, bd=1, borderwidth='1', bg="#6444BB", fg="white", activebackground="#6444BB", activeforeground="#EDF9FD", command= lambda: delete_item_button_event()).grid(row=3, column=1, ipadx=30, padx=50, pady=10, sticky=W)
        Button(operation_buttons_frame, text="ADD ITEM", font=("Arial Narrow",16,"bold"), width=15, bd=1, borderwidth='1', bg="#6444BB", fg="white", activebackground="#6444BB", activeforeground="#EDF9FD", command= lambda: add_item_button_event()).grid(row=4, column=1, ipadx=30, padx=50, pady=10, sticky=W)
        sort_button = Button(operation_buttons_frame, text='SORT ASCENDING', font=("Arial Narrow",16,"bold"), width=15, bd=1, borderwidth='1', bg="#6444BB", fg="white", activebackground="#6444BB", activeforeground="#EDF9FD", command= lambda: sort_items())
        sort_button.grid(row=5, column=1, ipadx=30, padx=50, pady=(10, 50), sticky=W)
        
        operation_buttons_frame.place(x=100, y=150)


    ##### SELECT FILE ######
    def select_file():
        select_file_frame = Frame(root, bg='#FFFFFF') 
        def select_file_event():
            global e
            filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select file", filetypes=( ("TXT Files",(".txt")),("All Files", "*.*")))
            e = ECommerce(filename)
            select_file_frame.place_forget()
            all_item_button_event()
            operation_buttons()

        Button(select_file_frame, text="SELECT FILE", font=("Arial Narrow",16,"bold"), width=20, bd=1, borderwidth='1', bg="#6444BB", fg="white", activebackground="#6444BB", activeforeground="#EDF9FD", command= lambda : select_file_event()).grid(row=0, column=0)
        select_file_frame.place(x=500, y=300)
        

    ###### LOGIN SCREEN #####
    def login_screen():
        login_frame = Frame(root, highlightbackground="orange", highlightthickness=2, bg="#FFFFFF") 

        Label(login_frame, text="Login", font=("Arial Narrow",20,"bold"), width=15, bd=1, borderwidth='1', bg="white", fg="#6444BB" ).grid(row=0, column=1, columnspan=3)
        
        Label(login_frame, text="Username: ", font=("Arial Narrow",16,"bold"), width=15, bd=1, borderwidth='1', bg="white", fg="#6444BB" ).grid(row=2, column=1)
        username_entry = Entry(login_frame, font=("Arial Narrow",16,"bold"), width=30, bd=1, borderwidth='2', bg="white", fg="#6444BB")
        username_entry.grid(row=2, column=2, padx= 10, pady=10)
        
        Label(login_frame, text="Password: ", font=("Arial Narrow",16,"bold"), width=15, bd=1, borderwidth='1', bg="white", fg="#6444BB" ).grid(row=3, column=1)
        password_entry = Entry(login_frame, font=("Arial Narrow",16,"bold"), width=30, bd=1, borderwidth='2', bg="white", fg="#6444BB")
        password_entry.grid(row=3, column=2, padx= 10, pady=10)

        def login():
            if username_entry.get() == 'admin' and password_entry.get() == 'admin@123':
                login_frame.place_forget()
                select_file()
            else:
                Label(login_frame, text="Invalid Credentials!", font=("Arial Narrow",10,"bold"), width=15, bd=1, borderwidth='1', bg="white", fg="red" ).grid(row=6, column=2, sticky=E)

        Button(login_frame, text="LOGIN", font=("Arial Narrow",16,"bold"), width=20, bd=1, borderwidth='1', bg="#6444BB", fg="white", activebackground="#6444BB", activeforeground="#EDF9FD", command= lambda : login()).grid(row=5, column=1, padx= 10, pady=(10, 20), columnspan=2)
        
        login_frame.place(x=367, y=215, width=530, height=250)


    # login_screen()
    login_screen()

    ####### LOGIN SCREEN #####
    Label(root, text="E-Commerce Application", font=("Arial Narrow",20,"bold"), bd=1, borderwidth='1', bg="white", fg="#6444BB" ).place(x=510, y=10)

    root.configure(background='#FFFFFF')
    root.mainloop()
