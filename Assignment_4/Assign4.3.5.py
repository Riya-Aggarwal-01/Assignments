import sqlite3
conn = sqlite3.connect("Practice.db")

id = input("Enter ID you want to delete")
conn.execute(f"DELETE from students where sid = {id}")
conn.commit()
conn.close()