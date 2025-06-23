#Inserting into database
import sqlite3
conn = sqlite3.connect("Practice.db")
conn.execute('''
INSERT INTO students (sid,name,age,course) VALUES
(1, 'Riya Aggarwal', 20, 'Python'),
(2, 'Parveen Kumar', 21, 'Data Science'),
(3, 'Nehal Bakliwal', 19, 'Python')
''')

conn.execute('''
INSERT INTO courses (cid, name, duration_months) VALUES
(101, 'Python', 3),
(102, 'Data Science', 6),
(103, 'Web Development', 4)
''')
conn.commit()
conn.close()