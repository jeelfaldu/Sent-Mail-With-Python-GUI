import sqlite3
conn = sqlite3.connect('data.db')

def sqlconecton():
    conn = sqlite3.connect('data.db')
    print ("Opened database successfully");
    conn.execute('''CREATE TABLE IF NOT EXISTS maildata
         (Email TEXT PRIMARY KEY);''')
    conn.close()


def insert(data):
    qurey = "INSERT OR REPLACE into maildata(Email) values('"+data+"')"
    conn.execute(qurey)   
    conn.commit()

def showdata():
    conn = sqlite3.connect('data.db')
    fqurey = "select Email from maildata"
    c = conn.execute(fqurey)
    for row in c:
       print(row[0],end="\n")
    conn.close()
    

