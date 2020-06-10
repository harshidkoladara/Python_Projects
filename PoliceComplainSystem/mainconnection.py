import sqlite3
 
from sqlite3 import Error
 
def sql_connection():
 
    try:
 
        con = sqlite3.connect('mydatabase.db')
 
        return con
 
    except Error:
 
        print(Error)
 
def sql_table(con):
 
    cursorObj = con.cursor()
    #cursorObj.execute('insert into data VALUES(1,0," "))')
    cursorObj.execute("CREATE TABLE IF NOT EXISTS data (id integer,num integer,address varchar(30))")
    try:
        cursorObj.execute("INSERT INTO data VALUES(1,0,'')")
    except:
        pass

    
    cursorObj.execute("select num from data where id=1")
    rows = cursorObj.fetchall()
 
    for row in rows:
 
        return row[0]
 
    con.commit()







