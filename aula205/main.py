import sqlite3 
from pathlib import Path

ROOT_DIR = Path(__file__).parent 
DB_NAME = 'db.sqlite3' 
DB_FILE = ROOT_DIR / DB_NAME 
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE) 
cursor = connection.cursor() 

# Apaga dados anteriores
cursor.execute(f'DELETE FROM {TABLE_NAME}') 
cursor.execute(f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"')
connection.commit()

# Cria a tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
    'id INTEGER PRIMARY KEY AUTOINCREMENT, '
    'name TEXT, '
    'weight REAL'
    ')'
)
connection.commit()

# SQL com placeholders nomeados
sql = f'INSERT INTO {TABLE_NAME} (name, weight) VALUES (:nome, :peso)'

# Executa inserções
cursor.execute(sql, {'nome': 'Sem nome', 'peso': 3})
cursor.executemany(sql, [
    {'nome': 'Joãozinho', 'peso': 3},
    {'nome': 'Maria', 'peso': 2},
    {'nome': 'Helena', 'peso': 4},
    {'nome': 'Joana', 'peso': 5},
])
connection.commit()

print("Inserções feitas com sucesso.")

cursor.close()
connection.close()

if __name__ == '__main__':
    print(sql)