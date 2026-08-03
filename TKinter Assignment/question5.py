from tkinter import *
import tkinter.messagebox as tkMessageBox


#load tkinter object and give it the title
root = Tk()
root.title("Pizza Shop")

# submit order method
def order():
    if tomato.get() == 0 and green_peppper.get() == 0 and black_olives.get() == 0 and mushrooms.get() == 0 and extra_cheese.get() == 0 and pepproni.get() == 0 and sausage.get() == 0: #checking toppings are selected or not
        tkMessageBox.showwarning('Missing Field', "Plase select atleast one toping...", icon="warning") 
    elif pizza_size.get() == 0: #checking pizza size are selected or not
        tkMessageBox.showwarning('Missing Field', "Plase select the pizza size...", icon="warning") 
    elif pizza_type.get() == 0: #checking pizza type selected or not
        tkMessageBox.showwarning('Missing Field', "Plase select the pizza type...", icon="warning") 
    else:
        text_feild.delete("1.0","end") # clear text feild
        amount = 0.0

        # checking pizza size and calculating amount for ir
        pizza_size_str = str()
        if pizza_size.get() == 1:
            amount += 6.50
            pizza_size_str = "small"
        elif pizza_size.get() == 2:
            amount += 8.50
            pizza_size_str = "medium"
        elif pizza_size.get() == 3:
            amount += 10.00
            pizza_size_str = "large"

        # checking pizza crust
        pizza_type_str = str()
        if pizza_type.get() == 1:
            pizza_type_str = "thin crust"
        elif pizza_type.get() == 2:
            pizza_type_str = "medium crust"
        elif pizza_type.get() == 3:
            pizza_type_str = "pan"

        # checking pizza toppings and calculating amount for it
        toppings = ""
        if tomato.get() == 1:
            amount += 1.50
            toppings += "tomato, "
        if green_peppper.get() == 1:
            amount += 1.50
            toppings += "green pappper, "
        if black_olives.get() == 1:
            amount += 1.50
            toppings += "black olives, "
        if mushrooms.get() == 1:
            amount += 1.50
            toppings += "mushrooms, "
        if extra_cheese.get() == 1:
            amount += 1.50
            toppings += "extra cheese, "
        if pepproni.get() == 1:
            amount += 1.50
            toppings += "pepproni, "
        if sausage.get() == 1:
            amount += 1.50
            toppings += "sausage,"

        # inserting data into text field
        text_feild.insert(INSERT, f"Pizza type: {pizza_type_str}\n")
        text_feild.insert(END, f"Pizza size: {pizza_size_str}\n")
        text_feild.insert(END, f"Toppings: {toppings}\n")
        text_feild.insert(END, f"Amount Due: {amount}")


# main label
Label(root, text="Welcome to Home Style Pizza Shop", fg="orange", font=("bold", 18)).grid(row=0, column=0, columnspan=3, padx=20, pady=(0, 20), sticky=W)


# create first frame for toppings 
frame = Frame(root, highlightbackground="orange", highlightthickness=2)
Label(frame, text="Each Topping: $1.50", fg="orange", font=("Arial", 10)).grid(row=0, column=0, sticky = W, padx=(5, 20))

# adding checkbox for all the toppings
tomato, green_peppper, black_olives, mushrooms, extra_cheese, pepproni, sausage = IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar() 
Checkbutton(frame, text = "Tomato", variable = tomato, onvalue = 1, offvalue = 0).grid(row=1, column=0, sticky = W, padx=10)
Checkbutton(frame, text = "Green Peppper", variable = green_peppper, onvalue = 1, offvalue = 0).grid(row=2, column=0, sticky = W, padx=10)
Checkbutton(frame, text = "Black Olives", variable = black_olives, onvalue = 1, offvalue = 0).grid(row=3, column=0, sticky = W, padx=10)
Checkbutton(frame, text = "Mushrooms", variable = mushrooms, onvalue = 1, offvalue = 0).grid(row=4, column=0, sticky = W, padx=10)
Checkbutton(frame, text = "Extra Cheese", variable = extra_cheese, onvalue = 1, offvalue = 0).grid(row=5, column=0, sticky = W, padx=10)
Checkbutton(frame, text = "Pepproni", variable = pepproni, onvalue = 1, offvalue = 0).grid(row=6, column=0, sticky = W, padx=10)
Checkbutton(frame, text = "Sausage", variable = sausage, onvalue = 1, offvalue = 0).grid(row=7, column=0, sticky = W, padx=10)

frame.grid(row=1, column=0,  rowspan=2, padx=(20, 0))


# create second frame for pizza size 
frame1 = Frame(root, highlightbackground="orange", highlightthickness=2)
Label(frame1, text="Pizza Size:", fg="orange", font=("Arial", 10)).grid(row=0, column=0, sticky = W, padx=(5, 20))

#adding radiobuttons for pizza size
pizza_size = IntVar()
Radiobutton(frame1, text="Small: $6.50", variable=pizza_size, value=1, height=2).grid(row=1, column=0, sticky = W, padx=10)
Radiobutton(frame1, text="Medium: $8.50",  variable=pizza_size, value=2, height=2).grid(row=2, column=0, sticky = W, padx=10)
Radiobutton(frame1, text="Large: $10.00", variable=pizza_size, value=3, height=2).grid(row=3, column=0, sticky = W, padx=10)

frame1.grid(row=1, column=1, sticky=N, padx=(20, 0))


# create third frame for pizza type 
frame2 = Frame(root, highlightbackground="orange", highlightthickness=2)
Label(frame2, text="Pizza Type:", fg="orange", font=("Arial", 10)).grid(row=0, column=0, sticky = W, padx=(5, 20))

#adding radiobuttons for pizza type
pizza_type = IntVar()
Radiobutton(frame2, text="Thin Crust", variable=pizza_type, value=1, height=2).grid(row=1, column=0, sticky = W, padx=10)
Radiobutton(frame2, text="Medium Crust",  variable=pizza_type, value=2, height=2).grid(row=2, column=0, sticky = W, padx=10)
Radiobutton(frame2, text="Pan", variable=pizza_type, value=3, height=2).grid(row=3, column=0, sticky = W, padx=10)

frame2.grid(row=1, column=2, sticky=N, padx=(20, 20))


# Process selection button
Button(root, text="Process Selection", command= lambda : order()).grid(row=2, column=1, ipadx=30, padx=20, columnspan=2, sticky=W)


# fourth frame for showing order
frame3 = Frame(root)
Label(frame3, text="Your Order:", font=("Arial", 8)).grid(row=0, column=0, sticky = W)

text_feild = Text(frame3, height = 5, width = 56)
text_feild.grid(row=1, column=0, sticky=W)

frame3.grid(row=3, column=0, pady=(10, 20), columnspan=3)


#run loop over main Window
root.mainloop()