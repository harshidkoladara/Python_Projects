import sqlite3
import tkinter as tk


conn = sqlite3.connect('name.db')
my_cursor = conn.cursor()


sql = "CREATE TABLE IF NOT EXISTS name (dname varchar(50))"
my_cursor.execute(sql)

data_obj = my_cursor.execute("SELECT dname FROM name")
name_of_user = data_obj.fetchone()

root = tk.Tk()
root.title("Jarvis")
root.geometry('400x200')

if (name_of_user is None):
    def sub_btn(*args):
        sql = f'INSERT INTO `name` (`dname`) VALUES (\"{entry_name.get()}\")'
        my_cursor.execute(sql)
        conn.commit()
        root.destroy()
        import voice1

    name = tk.Label(root, text="Enter Name", width=20, font=("bold", 10))
    name.grid(row=0, column=0)
    entry_name = tk.Entry(root, width=20)
    entry_name.grid(row=0, column=1)

    btn = tk.Button(root, text="submit", width=20,
                    bg='brown', fg='white', command=sub_btn)
    btn.grid(row=1, column=1)

else:
    root.destroy()
    import voice1

root.mainloop()
