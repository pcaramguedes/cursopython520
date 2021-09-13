import sqlite3

try:
    conn = sqlite3.connect('cafe.db')
    cursor = conn.cursor()
    sql = "SELECT * FROM ingrediente;"
    for registro in cursor.execute(sql):
        print('ID: ', registro[0])
        print('Nome: ', registro[1])
        print('Descricao: ', registro[2])
        print('Tipo: ', registro[3])
        print('Und Medida: ', registro[4])
except Exception as err:
    print('Erro inesperado')

except OperationalError:
    print('Erro operacional')
finally:
    conn.close()
