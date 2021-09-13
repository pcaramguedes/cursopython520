import sqlite3

conn = sqlite3.connect('cafe.db')

cursor = conn.cursor()
nome='água'
descricao='solvente universal'
tipo='líquido'
unidade_medida='ml'
sql = f"""
    insert into ingrediente (nome, descricao, tipo, unidade_medida)
    values ('{nome}','{descricao}','{tipo}','{unidade_medida}')
"""

cursor.execute(sql)
conn.commit()
conn.close()
