import sqlite3
#1: conectar com o arquivo de banco de dados
conn = sqlite3.connect('cafe.db')
#2: criar um cursor para executar instruções no banco de dados
cursor = conn.cursor()

#3: criar instrução SQL

sql = """
    create table ingrediente(
        id integer primary key autoincrement,
        nome text,
        descricao text,
        tipo text,
        unidade_medida text

    );
"""
cursor.execute(sql)

