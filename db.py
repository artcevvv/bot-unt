import sqlite3
from main import data

#очистка бд перед запуском / timecreated

conn= sqlite3.connect('dates.sqlite')
c= conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS RecordONE (Date TEXT)')

def data_entry():
    for i in data:
        c.execute(f"INSERT INTO RecordONE VALUES ('{i}')")
    
    conn.commit()

create_table()  
data_entry()
 
c.close()
conn.close()