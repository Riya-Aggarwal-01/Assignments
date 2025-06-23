# Selecting data from databse

import sqlite3
conn = sqlite3.connect("Practice.db")

data = conn.execute("select * from students")
for x in data:
    print(x)

data = conn.execute("SELECT * FROM Students WHERE course = 'Python' ")
for x in data:
    print(x)