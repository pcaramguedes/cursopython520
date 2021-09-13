import sqlite3

conn = sqlite3.connect('cafe.db')
cursor = conn.cursor()

sql = """
    delete from ingrediente
    where id = 1
"""

cursor.execute(sql)
conn.commit()
conn.close()
