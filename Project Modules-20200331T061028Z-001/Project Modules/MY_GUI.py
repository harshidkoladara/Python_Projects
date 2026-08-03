import tkinter as tk
import tkinter.ttk as ttk
from ttkthemes import ThemedStyle
from PIL import ImageTk, Image


root = tk.Tk()
root.geometry('500x300')
root.title("EVA")

style = ThemedStyle(root)
style.set_theme("equilux")

frame_cont = tk.Frame(root, width=500, height=250,)
frame_cont.configure(bg='black')
frame_cont.pack()


frame_bottom = tk.Frame(root, width=500, height=50,)
frame_bottom.configure(bg="white")
frame_bottom.pack(side=tk.BOTTOM)

you_x, you_y, you_x_img, you_y_img = 2, 3, 2, 4
eva_x, eva_y, eva_x_img, eva_y_img = 1, 2, 1, 1

# img_you = ImageTk.PhotoImage(Image.open('C:/Users/Harshid/Downloads/Project Modules-20200331T061028Z-001/Project Modules/YOU.png'))
# img_eva = ImageTk.PhotoImage(Image.open('C:/Users/Harshid/Downloads/Project Modules-20200331T061028Z-001/Project Modules/EVA.png'))

you_img = ttk.Label(frame_cont, text="you",
                    background="black", font=('Verdana', 16, 'bold'))
you_img.grid(row=you_x_img, column=you_y_img, padx=10, pady=10)
eva_img = ttk.Label(frame_cont, text="eva",
                    background="black", font=('Verdana', 16, 'bold'))
eva_img.grid(row=eva_x_img, column=eva_y_img, padx=10, pady=10)


you_txt = ttk.Label(frame_cont, text="s",  background="black",
                    foreground="white", font=('Verdana', 12))
you_txt.grid(row=you_x, column=you_y, pady=10)
eva_txt = ttk.Label(frame_cont, text="fsfs",  background="black",
                    foreground="white", font=('Verdana', 12))
eva_txt.grid(row=eva_x, column=eva_y, pady=10)


def call_method(*args):
    print(1)

# img_giffy = ImageTk.PhotoImage(Image.open('C:/Users/Harshid/Downloads/Project Modules-20200331T061028Z-001/Project Modules/giphy.gif'))
giffy_img = ttk.Button(frame_bottom, text="Speak", command = call_method)
giffy_img.pack()
root.configure(bg='black')
root.mainloop()
