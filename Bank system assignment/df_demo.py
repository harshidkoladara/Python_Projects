import sqlite3
import pandas as pd
from pandas import DataFrame

conn=sqlite3.connect("bank.db")

c=conn.cursor()

c.execute("SELECT count(name) from sqlite_master WHERE type='table' AND name='account'")
if c.fetchone()[0]==1:
    c.execute("DELETE FROM account")
else:
    c.execute("CREATE TABLE account(acc_number text, name text, balance real)")

c.execute("SELECT count(name) from sqlite_master WHERE type='table' AND name='tsn'")
if c.fetchone()[0]==1:
    c.execute("DELETE FROM tsn")
else:
    c.execute("CREATE TABLE tsn(acc_number text, date text, amount real)")

c.execute("SELECT count(name) from sqlite_master WHERE type='table' AND name='tsn_rec'")
if c.fetchone()[0]==1:
    c.execute("DELETE from tsn_rec")
else:
    c.execute("CREATE TABLE tsn_rec(acc_number text, name text, date text, amount real)")


conn.commit()

#read data from csv

read_accounts=pd.read_csv('Bank_Accounts.csv')
read_accounts.to_sql("account", conn, if_exists='append', index=False)

read_transaction=pd.read_csv('Bank_Transactions.csv')
read_transaction.to_sql("tsn", conn, if_exists='append', index=False)

c.execute("""
INSERT INTO tsn_rec (acc_number, name, date, amount)
SELECT account.acc_number, account.name, tsn.date, tsn.amount
FROM account
LEFT JOIN tsn ON account.acc_number=tsn.acc_number
""")

conn.commit()

c.execute("SELECT * FROM tsn_rec;")
tsn_rec_df=DataFrame(c.fetchall(), columns=['acc_number', 'name', 'date', 'amount'])

tsn_rec_df.to_sql('tsn_rec', conn, if_exists='append', index=False)

tsn_rec_df.to_csv('Transaction_Record.csv')


















