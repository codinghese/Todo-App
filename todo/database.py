import sqlite3  
  
con = sqlite3.connect("Todo.db")  
print("Database opened successfully")  
  
con.execute("create table todolist (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL UNIQUE)")  
  
print("Table created successfully")  
  
con.close()  