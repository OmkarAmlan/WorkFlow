import sqlite3
import init
import cipher

conn=sqlite3.connect("users.db")
cur=conn.cursor()

def check(password):
    l, u, p, d = 0, 0, 0, 0
    n=len(password)
    if (n >= 8):
        for i in password: 
            if (i.islower()):
                l+=1           
            if (i.isupper()):
                u+=1           
            if (i.isdigit()):
                d+=1           
            if(i=='@'or i=='$' or i=='_'):
                p+=1          
    if(l>0 and u>0 and d>0 and p>0 and (l+u+d+p)==n):
        return 1
    return 0

def create_account(username,password):
    cur.execute("""
                CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY,
                username VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL
                );
                 """)
    conn.commit()
    cur.execute("SELECT * FROM users where username = ?",(username,))
    if cur.fetchall():
        return 2
    else:
        if check(cipher.decipher(password)):
            cur.execute("INSERT INTO users (username,password) VALUES(?,?)",(username,password))
            conn.commit()
            return 1
        else:
            return 0

def master_password_check(username,password):
    cur.execute("""
                CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY,
                username VARCHAR(255) NOT NULL,
                password TEXT NOT NULL
                );
                 """)
    conn.commit()
    cur.execute("SELECT * FROM users WHERE username = ? AND password = ?",(username,password))
    if cur.fetchall():
        return 1
    else:
        return 0
