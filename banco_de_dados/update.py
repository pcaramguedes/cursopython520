import sqlite3

conn = sqlite3.connect('cafe.db')

cursor = conn.cursor()

sql = """
    update ingrediente
    set unidade_medida='l'
    where id = 1
"""

cursor.execute(sql)
conn.commit()

