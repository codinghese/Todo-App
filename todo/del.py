import sqlite3
conn = sqlite3.connect('Todo.db')
data = conn.execute("delete from todolist where id>0 ");
conn.close();
