import sqlite3
conn = sqlite3.connect("Practice.db")

conn.execute("UPDATE Students SET course = 'Web Development' WHERE sid = 2")
conn.commit()
conn.close()