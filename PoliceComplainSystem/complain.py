from tkinter import *
from mainconnection import *
def complen():
    root=Tk()
    root.geometry("650x500")
    root.title("Complain")

    f1=Frame(root)
    f1.grid(row=0,column=0)

    f2=Frame(root)
    f2.grid(row=1,column=0)

    Label(f1,text=" COMPLAIN REGISTRATION FORM",anchor="c").pack()




    l1=Label(f2,text="Department Address",width=30,pady=10)
    l1.grid(row=0,column=0)


    e1=Entry(f2,width=40)
    e1.grid(row=0,column=1)


    con = sql_connection()
    what = sql_table(con)
    if(what==1):
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute('select address from data where id=1')
        rows = cursorObj.fetchall()
        for row in rows:
            e1.insert(0,row[0])
            
        con.commit()


    l2=Label(f2,text="Enter Your Complain Statement",width=30,pady=10)
    l2.grid(row=1,column=0)

    ta1=Text(f2,height=6,width=30)
    ta1.grid(row=1,column=1)
    root.mainloop()
