import sqlite3

conn=sqlite3.connect("test_bank_basic.db")

c=conn.cursor()

# check if table exists already before creating new one.
c.execute("""SELECT count(name) from sqlite_master WHERE type='table' AND name='account' """)
if c.fetchone()[0]==1:
    pass
    c.execute("DELETE FROM account;") # delete all records to start fresh test everytime the program runs.
else:
    c.execute("""CREATE TABLE account (name text, balance real)""")

test_name='Janak'
test_balance=100.0

#storing data in list and populating that into table.

accounts=[("David", 201.0),
          ('Ross', 301.5)]


#single data entry
c.execute("INSERT INTO account VALUES('Sita', 10001);") # Static data input
c.execute("INSERT INTO account VALUES(?, ?)", (test_name, test_balance))
c.execute("INSERT INTO account VALUES(:name, :balance)", {'balance': test_balance, 'name':test_name})

#multiple data entry via list created above
c.executemany("INSERT INTO account VALUES(?, ?);", accounts)


conn.commit()

c.execute("SELECT * FROM account;")

#print(c.fetchall())
lst=c.fetchall()

print(lst)
print(f" Account Name\t\t Account Balance")
print(f"---------------------------------")
for item in lst:
    print(f"{item[0]} \t\t\t\t {item[1]}")

#update one record and display updated record.

c.execute('''UPDATE account SET name=:newname WHERE name=:name''', {'name':'Sita', 'newname':'Sujata' })

c.execute("SELECT * FROM account;")
lst=c.fetchall()

print(lst)
print(f" Account Name\t\t Account Balance")
print(f"---------------------------------")
for item in lst:
    print(f"{item[0]} \t\t\t\t {item[1]}")

#update all record

interest_rate=1.05
c.execute("SELECT * FROM account;")
lst=c.fetchall()

for item in lst:
    newbalance=item[1]*interest_rate
    c.execute('''UPDATE account SET balance=:balance WHERE name=:name''', {'name': item[0], 'balance': newbalance })

c.execute("SELECT * FROM account;")
lst=c.fetchall()

print(f" Account Name\t\t Account Balance")
print(f"---------------------------------")
for item in lst:
    print(f"{item[0]} \t\t\t\t {item[1]}")

#delete record and display updated table records
#c.execute("DELETE FROM account WHERE name='Ross';")
c.execute("DELETE FROM account WHERE balance<110;")

c.execute("SELECT * FROM account;")
lst=c.fetchall()

print(f" Account Name\t\t Account Balance")
print(f"---------------------------------")
for item in lst:
    print(f"{item[0]} \t\t\t\t {item[1]}")

conn.close() # close the connection



