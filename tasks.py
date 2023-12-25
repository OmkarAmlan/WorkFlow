import login
import init
import sqlite3
from datetime import datetime

conn=sqlite3.connect("users.db")
cur=conn.cursor()

def add_task(username,task,description,rating):
    #Task database creation
    cur.execute("""
            CREATE TABLE IF NOT EXISTS tasks(
                task TEXT NOT NULL,
                description TEXT NOT NULL,
                rating VARCHAR(255) NOT NULL,
                done BOOLEAN NOT NULL,
                date date NOT NULL,
                id INTEGER PRIMARY KEY,
                username VARCHAR(255) NOT NULL
                );
                 """)
    conn.commit()
    now=datetime.now()
    cur.execute("INSERT INTO tasks (username,task,description,rating,done,date) VALUES(?,?,?,?,?,?)",(username,task,description,rating,False,now.date()))
    conn.commit()
    
    
def view_task(username):
    cur.execute("""
            CREATE TABLE IF NOT EXISTS tasks(
                task TEXT NOT NULL,
                description TEXT NOT NULL,
                rating VARCHAR(255) NOT NULL,
                done BOOLEAN NOT NULL,
                date date NOT NULL,
                id INTEGER PRIMARY KEY,
                username VARCHAR(255) NOT NULL
                );
                 """)
    conn.commit()
    cur.execute("SELECT * FROM tasks where username = ? AND done = ?",(username,False))
    return cur.fetchall()

def view_task_complete(username):
    cur.execute("""
            CREATE TABLE IF NOT EXISTS tasks(
                task TEXT NOT NULL,
                description TEXT NOT NULL,
                rating VARCHAR(255) NOT NULL,
                done BOOLEAN NOT NULL,
                date date NOT NULL,
                id INTEGER PRIMARY KEY,
                username VARCHAR(255) NOT NULL
                );
                 """)
    conn.commit()
    cur.execute("SELECT * FROM tasks where username = ? AND done = ?",(username,True))
    return cur.fetchall()

def update_table(username,task):
    cur.execute("""
            CREATE TABLE IF NOT EXISTS tasks(
                task TEXT NOT NULL,
                description TEXT NOT NULL,
                rating VARCHAR(255) NOT NULL,
                done BOOLEAN NOT NULL,
                date date NOT NULL,
                id INTEGER PRIMARY KEY,
                username VARCHAR(255) NOT NULL
                );
                 """)
    conn.commit()
    cur.execute("UPDATE tasks SET done=True WHERE username=? AND task=?",(username,task))
    conn.commit()
    