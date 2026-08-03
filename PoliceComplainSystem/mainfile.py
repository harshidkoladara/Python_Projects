from mainconnection import *

con = sql_connection()
 
what = sql_table(con)

if(what==0):
    x=input("Enter Address of Police station :")
    cursorObj = con.cursor()
 
    cursorObj.execute('update data set address="'+x+'"where id=1')
    cursorObj.execute('update data set num=1 where id=1')
    con.commit()
else:
    con = sql_connection()
    
    cursorObj = con.cursor()
 
    cursorObj.execute('select address from data where id=1')
    rows = cursorObj.fetchall()
 
    for row in rows:
 
        print(row[0])
 
    con.commit()
