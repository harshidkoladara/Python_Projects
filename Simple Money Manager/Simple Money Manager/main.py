import tkinter as tk
from tkinter import ttk
from moneymanager import MoneyManager
import tkinter.messagebox

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np

global x_axis
global y_axis
LARGEFONT = ("Verdana", 35)
MEDIUMFONT = ("Verdana", 22)
SMALLFONT = ("Verdana", 10)


class tkinterApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        self.winfo_toplevel().title("FedUni Money Manager")

        title_frame = tk.Frame(self)
        title_frame.pack(side="top")
        title = ttk.Label(
            title_frame, text="FedUni Money Manager", font=MEDIUMFONT)
        title.grid(row=0, padx=10, pady=50)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.geometry('500x600')
        for F in (StartPage, Page1):

            frame = F(container, self)

            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global pin_number
        pin_number = tk.StringVar()

        def only_numbers(char):
            return char.isdigit() or "*"

        validation = parent.register(only_numbers)

        label = ttk.Label(self, text="User Number / PIN",
                          width=19, font=SMALLFONT)
        label.grid(row=1, column=0)
        global account_id
        account_id = ttk.Entry(self, font="12", width=19,
                               validate="key", validatecommand=(validation, '%S'))
        account_id.grid(row=1, column=1, ipady=10)
        global pin
        pin = ttk.Entry(self, font="12", width=19, validate="key",
                        validatecommand=(validation, '%S'))
        pin.grid(row=1, column=2, ipady=10)
        pin.bind("<Key>", lambda e: "break")

        def pin_insert(pin_e):
            pin_number.set(pin_number.get() + str(pin_e))
            try:
                pin.insert(tk.END, "*")
            except:
                pin.insert(tk.END, "*")

        def login():
            file = f"{account_id.get()}.txt"

            try:
                with open(file, 'r') as f:
                    file_data = f.read()

                data = list(file_data.split("\n"))
                global transaction_list

                transaction_list = []
                if str(data[1]) == str(pin_number.get()):
                    try:
                        for x in range(3, len(data), 2):
                            transaction_list.append((data[x], data[x+1]))  
                    except:
                        pass        
                    global moneyManager
                    moneyManager = MoneyManager(
                        data[0], data[1], data[2], transaction_list)

                    
                    user_number.config(text="User Number: {}".format(data[0]))
                    balance.config(text="Balance: ${}".format(data[2]))
                    for x in range(3, len(data)):
                        entries.insert(tk.END, data[x]+ '\n')
                    controller.show_frame(Page1)
                    controller.geometry('660x700')

                    x , y = [], []
                    x.append(0)
                    y.append(float(moneyManager.balance))
                    p = 1
                    lst = transaction_list[::-1]
                    for i in lst:
                        x.append(p)
                        p = p+ 1
                        if x == 'Deposit':
                            y.append(float(moneyManager.balance) - float(i[1]))
                        else:
                            y.append(float(moneyManager.balance) + float(i[1]))    
                        
                    else:
                        y = y[::-1]
                        line[0].set_data(x, y)
                        ax = canvas.figure.axes[0]
                        ax.set_xlim(0, len(x))
                        ax.set_ylim(0, max(y)+200)  
                        fig_subplot.relim()
                        fig_subplot.autoscale_view()
                        canvas.draw()

                else:
                    tkinter.messagebox.showinfo(
                        'FedUni Money Manager', 'Wrong PIN!                    ')

            except Exception as e:
                print(e)
                tkinter.messagebox.showinfo(
                    'FedUni Money Manager', 'User doesn\'t Exist!            ')

        tk.Button(self, text="1", fg="black",  height=5, bg="#fff", cursor="hand2",
                  command=lambda: pin_insert("1")).grid(row=3, column=0, sticky=tk.E+tk.W)
        tk.Button(self, text="2", fg="black",  height=5, bg="#fff", cursor="hand2",
                  command=lambda: pin_insert("2")).grid(row=3, column=1, sticky=tk.E+tk.W)
        tk.Button(self, text="3", fg="black",  height=5, bg="#fff", cursor="hand2",
                  command=lambda: pin_insert("3")).grid(row=3, column=2, sticky=tk.E+tk.W)

        tk.Button(self, text="4", fg="black",  height=5, bg="#fff", cursor="hand2",
                  command=lambda: pin_insert("4")).grid(row=4, column=0, sticky=tk.E+tk.W)
        tk.Button(self, text="5", fg="black",  height=5, bg="#fff", cursor="hand2",
                  command=lambda: pin_insert("5")).grid(row=4, column=1, sticky=tk.E+tk.W)
        tk.Button(self, text="6", fg="black",  height=5, bg="#fff", cursor="hand2",
                  command=lambda: pin_insert("6")).grid(row=4, column=2, sticky=tk.E+tk.W)

        tk.Button(self, text="7", fg="black",  height=5, bg="#fff", cursor="hand2",
                  command=lambda: pin_insert("7")).grid(row=5, column=0, sticky=tk.E+tk.W)
        tk.Button(self, text="8", fg="black",  height=5, bg="#fff", cursor="hand2",
                  command=lambda: pin_insert("8")).grid(row=5, column=1, sticky=tk.E+tk.W)
        tk.Button(self, text="9", fg="black",  height=5, bg="#fff", cursor="hand2",
                  command=lambda: pin_insert("9")).grid(row=5, column=2, sticky=tk.E+tk.W)

        def pin_delete():
            pin.delete(0, tk.END)
            pin_number.set('')

        tk.Button(self, text="Cancel/Clear", fg="black",  height=5, bg="#f00",
                  cursor="hand2", command=lambda: pin_delete()).grid(row=6, column=0, sticky=tk.E+tk.W)
        tk.Button(self, text="0", fg="black",  height=5, bg="#fff", cursor="hand2",
                  command=lambda: pin_insert("0")).grid(row=6, column=1, sticky=tk.E+tk.W)
        tk.Button(self, text="Log In", fg="black",  height=5, bg="#0f0", cursor="hand2",
                  command=lambda: login()).grid(row=6, column=2, sticky=tk.E+tk.W)

        
class Page1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global x_axis
        global y_axis
        x_axis = tk.StringVar(self)
        y_axis = tk.StringVar(self)
        x_axis.set([])
        y_axis.set([])

        def logout():
            controller.show_frame(StartPage)
            controller.geometry('500x600')
            pin_number.set('')
            pin.delete(0, tk.END)
            account_id.delete(0, tk.END)
            moneyManager.save_to_file()

        global user_number
        user_number = ttk.Label(
            self, text="User Number: ", width=25, font=SMALLFONT)
        user_number.grid(row=1, column=0, padx=10)
        global balance
        balance = ttk.Label(self, text="Balance: $",
                            width=25, font=SMALLFONT)
        balance.grid(row=1, column=1, ipady=10, padx=10)
        tk.Button(self, text="Log Out", fg="black", height=3, width=20, cursor="hand2",
                  command=lambda: logout()).grid(row=1, column=2, sticky=tk.E+tk.W, padx=10)

        amount = ttk.Label(self, text="Amount ($)", width=25, font=SMALLFONT)
        amount.grid(row=2, column=0, padx=10)
        value = tk.Text(self, height=4, width=2)
        value.grid(row=2, column=1, sticky=tk.E+tk.W, padx=10)

        def add_fund():
            amount = value.get("1.0", "end-1c")
            moneyManager.deposite_funds(amount)
            transaction_list.append(('Deposit', amount))
            balance.config(text="Balance: ${}".format(moneyManager.balance))
            value.delete('1.0', tk.END)
            entries.insert(tk.END, 'Deposit' + '\n')
            entries.insert(tk.END, str(float(amount)) + '\n')

            x , y = [], []
            x.append(0)
            y.append(float(moneyManager.balance))
            p = 1
            lst = transaction_list[::-1]
            for i in lst:
                x.append(p)
                p = p+ 1
                if x == 'Deposit':
                    y.append(float(moneyManager.balance) - float(i[1]))
                else:
                    y.append(float(moneyManager.balance) + float(i[1]))    
                
            else:
                y = y[::-1]
                line[0].set_data(x, y)
                ax = canvas.figure.axes[0]
                ax.set_xlim(0, len(x))
                ax.set_ylim(0, max(y)+200)  
                fig_subplot.relim()
                fig_subplot.autoscale_view()
                canvas.draw()

        tk.Button(self, text="Deposit", fg="black", height=3, width=20, cursor="hand2",
                             command=lambda: add_fund()).grid(row=2, column=2, sticky=tk.E+tk.W, padx=10)

        tkvar = tk.StringVar(self)
        choices = {'Rent', 'Food', 'Bills', 'Entertainment', 'Other'}
        tkvar.set('Rent')

        entry_type_lable = ttk.Label(
            self, text="Entry Type", width=25, font=SMALLFONT)
        entry_type_lable.grid(row=3, column=0, padx=10)
        entry_type = tk.OptionMenu(self, tkvar, *choices)
        entry_type.grid(row=3, column=1, sticky=tk.E+tk.W, padx=10)

        def add_entry_type():
            amount = value.get("1.0", "end-1c")
            if float(moneyManager.balance) - float(amount) > 0:
                transaction_list.append((tkvar.get(), amount))
                moneyManager.add_entry(amount, tkvar.get())
                balance.config(text="Balance: ${}".format(
                    moneyManager.balance))
                value.delete('1.0', tk.END)
                entries.insert(tk.END, tkvar.get() + '\n')
                entries.insert(tk.END, str(float(amount)) + '\n')

                x , y = [], []
                x.append(0)
                y.append(float(moneyManager.balance))
                p = 1
                lst = transaction_list[::-1]
                for i in lst:
                    x.append(p)
                    p = p+ 1
                    if x == 'Deposit':
                        y.append(float(moneyManager.balance) - float(i[1]))
                    else:
                        y.append(float(moneyManager.balance) + float(i[1]))    
                    
                else:
                    y = y[::-1]
                    line[0].set_data(x, y)
                    ax = canvas.figure.axes[0]
                    ax.set_xlim(0, len(x))
                    ax.set_ylim(0, max(y)+200)  
                    fig_subplot.relim()
                    fig_subplot.autoscale_view()
                    canvas.draw()

            else:
                tkinter.messagebox.showinfo(
                    'FedUni Money Manager', 'Expenditure amount is greter then balance!')
        tk.Button(self, text="Add Entry", fg="black", height=3, width=20, cursor="hand2",
                  command=lambda: add_entry_type()).grid(row=3, column=2, sticky=tk.E+tk.W, padx=10)

        
        fig = Figure(figsize=(4, 2), dpi=100)
        # t = np.arange(0, 3, .01)
        global fig_subplot
        fig_subplot = fig.add_subplot(111)
        global line
        global canvas
        line = fig_subplot.plot([], [])

        canvas = FigureCanvasTkAgg(fig, master=self) 
        # canvas.draw()
        canvas.get_tk_widget().grid(column=0, row=6, columnspan=4)

        global entries
        entries = tk.Text(self, height=10, width=2)
        entries.grid(row=4, column=0, pady=5, columnspan=4,
                     sticky=tk.E+tk.W, padx=10)

        
app = tkinterApp()
app.mainloop()
