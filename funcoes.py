import sqlite3

def conectarbanco():
    conn = sqlite3.connect("pets.db")
    cursor = conn.cursor()
    return conn, cursor

# Função para cadastrar um pet
def cadastrar_pet_poo(nome, idade, especie, raca):
    conn, cursor = conectarbanco()
    cursor.execute("INSERT INTO pets (nome, idade, especie, raca) VALUES (?, ?, ?, ?)", (nome, idade, especie, raca))
    conn.commit()
    cursor.close()
    conn.close()

# Função para listar todos os pets
def listar_pets():
    conn, cursor = conectarbanco()
    cursor.execute("SELECT * FROM pets")
    pets= cursor.fetchall()
    cursor.close()
    conn.close()
    return pets


# Função para buscar pet por nespecie
def buscar_pet(especie):
    conn, cursor = conectarbanco() 
    cursor.execute("SELECT * FROM pets WHERE especie = ?", (especie,))
    pets= cursor.fetchall()
    cursor.close()
    conn.close()
    return pets

# Função para atualizar dados de um pet
def atualizar_pet(nome,idade,especie,raca,id_pet):
    conn, cursor = conectarbanco()
    cursor.execute("UPDATE pets SET nome = ?, idade = ?, especie = ?, raca = ? WHERE id = ?", (nome, idade, especie, raca, id_pet))    
    conn.commit()
    cursor.close()
    conn.close()
    
# Função para marcar um pet como adotado
def marcar_como_adotado(id_pet):
    conn , cursor= conectarbanco() 
    cursor.execute("UPDATE pets SET adotado = 1 WHERE id = ?", (id_pet,))
    conn.commit()
    cursor.close()
    conn.close()
    
def remover_pet(id_pet):
    conn, cursor = conectarbanco()
    cursor.execute("DELETE FROM pets WHERE id = ?", (id_pet,))
    conn.commit()
    cursor.close()
    conn.close() 