import sqlite3

# Conectando ao banco de dados (criará um novo se não existir)
conn = sqlite3.connect("pets.db")

# Criando um cursor
cursor = conn.cursor()

# Criando a tabela de pets
cursor.execute("""
CREATE TABLE IF NOT EXISTS pets (
    id INTEGER PRIMARY KEY, 
    nome TEXT, 
    idade INTEGER, 
    especie TEXT, 
    raca TEXT, 
    adotado INTEGER DEFAULT 0
)
""")

# Salvando as alterações
conn.commit() 

# Fechando a conexão 
cursor.close()  
conn.close() # Fechar a conexão