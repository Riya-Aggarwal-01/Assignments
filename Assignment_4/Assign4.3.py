#creating a database
import sqlite3
conn = sqlite3.connect("Practice.db")
conn.execute('''
create table students(
sid INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR(50),
age INT,
course VARCHAR(30)
)
''')
conn.execute('''
create table courses(
cid INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR(100),
duration_months INT
)
''')
print("Tables created successfully")
conn.close()