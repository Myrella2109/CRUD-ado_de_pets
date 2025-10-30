# ==========================
# ARQUIVO: funcoes.py
# ==========================
# Define as classes responsáveis por manipular o banco de dados:
# GerenciadorPets, GerenciadorClientes e GerenciadorONGs
# Cada uma realiza as operações CRUD da sua respectiva entidade.
# ==========================

import sqlite3
from modelo import Pet, Cliente, ONG


# ---------------- GERENCIADOR DE PETS ----------------
class GerenciadorPets:
    def __init__(self):
        self.conn = sqlite3.connect("pets.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS pets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                idade INTEGER,
                especie TEXT,
                raca TEXT,
                adotado INTEGER DEFAULT 0
            )
        """)
        self.conn.commit()

    def cadastrar_pet(self, pet):
        self.cursor.execute(
            "INSERT INTO pets (nome, idade, especie, raca, adotado) VALUES (?, ?, ?, ?, ?)",
            (pet.nome, pet.idade, pet.especie, pet.raca, pet.adotado)
        )
        self.conn.commit()
        pet.id = self.cursor.lastrowid
        return pet

    def listar_pets(self):
        self.cursor.execute("SELECT * FROM pets")
        pets = []
        for row in self.cursor.fetchall():
            id, nome, idade, especie, raca, adotado = row
            pets.append(Pet(nome, idade, especie, raca, id, adotado))
        return pets

    def buscar_pet_por_especie(self, especie):
        self.cursor.execute("SELECT * FROM pets WHERE especie = ?", (especie,))
        pets = []
        for row in self.cursor.fetchall():
            id, nome, idade, especie, raca, adotado = row
            pets.append(Pet(nome, idade, especie, raca, id, adotado))
        return pets

    def buscar_pet_por_id(self, id_pet):
        self.cursor.execute("SELECT * FROM pets WHERE id = ?", (id_pet,))
        row = self.cursor.fetchone()
        if row:
            id, nome, idade, especie, raca, adotado = row
            return Pet(nome, idade, especie, raca, id, adotado)
        return None

    def atualizar_pet(self, pet):
        self.cursor.execute("""
            UPDATE pets
            SET nome=?, idade=?, especie=?, raca=?, adotado=?
            WHERE id=?
        """, (pet.nome, pet.idade, pet.especie, pet.raca, pet.adotado, pet.id))
        self.conn.commit()

    def marcar_como_adotado(self, id_pet):
        self.cursor.execute("UPDATE pets SET adotado=1 WHERE id=?", (id_pet,))
        self.conn.commit()

    def remover_pet(self, id_pet):
        self.cursor.execute("DELETE FROM pets WHERE id=?", (id_pet,))
        self.conn.commit()

    def fechar_conexao(self):
        self.conn.close()


# ---------------- GERENCIADOR DE CLIENTES ----------------
class GerenciadorClientes:
    def __init__(self):
        self.conn = sqlite3.connect("pets.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                cpf TEXT UNIQUE,
                telefone TEXT,
                email TEXT
            )
        """)
        self.conn.commit()

    def cadastrar_cliente(self, cliente):
        self.cursor.execute(
            "INSERT INTO clientes (nome, cpf, telefone, email) VALUES (?, ?, ?, ?)",
            (cliente.nome, cliente.cpf, cliente.telefone, cliente.email)
        )
        self.conn.commit()
        cliente.id = self.cursor.lastrowid
        return cliente

    def listar_clientes(self):
        self.cursor.execute("SELECT * FROM clientes")
        clientes = []
        for row in self.cursor.fetchall():
            id, nome, cpf, telefone, email = row
            clientes.append(Cliente(nome, cpf, telefone, email, id))
        return clientes

    def buscar_cliente_por_cpf(self, cpf):
        self.cursor.execute("SELECT * FROM clientes WHERE cpf = ?", (cpf,))
        row = self.cursor.fetchone()
        if row:
            id, nome, cpf, telefone, email = row
            return Cliente(nome, cpf, telefone, email, id)
        return None

    def fechar_conexao(self):
        self.conn.close()


# ---------------- GERENCIADOR DE ONGs ----------------
class GerenciadorONGs:
    def __init__(self):
        self.conn = sqlite3.connect("pets.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS ongs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                cnpj TEXT UNIQUE,
                endereco TEXT,
                telefone TEXT,
                email TEXT
            )
        """)
        self.conn.commit()

    def cadastrar_ong(self, ong):
        self.cursor.execute(
            "INSERT INTO ongs (nome, cnpj, endereco, telefone, email) VALUES (?, ?, ?, ?, ?)",
            (ong.nome, ong.cnpj, ong.endereco, ong.telefone, ong.email)
        )
        self.conn.commit()
        ong.id = self.cursor.lastrowid
        return ong

    def listar_ongs(self):
        self.cursor.execute("SELECT * FROM ongs")
        ongs = []
        for row in self.cursor.fetchall():
            id, nome, cnpj, endereco, telefone, email = row
            ongs.append(ONG(nome, cnpj, endereco, telefone, email, id))
        return ongs

    def atualizar_ong(self, ong):
        self.cursor.execute("""
            UPDATE ongs
            SET nome=?, cnpj=?, endereco=?, telefone=?, email=?
            WHERE id=?
        """, (ong.nome, ong.cnpj, ong.endereco, ong.telefone, ong.email, ong.id))
        self.conn.commit()

    def remover_ong(self, id_ong):
        self.cursor.execute("DELETE FROM ongs WHERE id=?", (id_ong,))
        self.conn.commit()

    def buscar_ong_por_id(self, id_ong):
        self.cursor.execute("SELECT * FROM ongs WHERE id=?", (id_ong,))
        row = self.cursor.fetchone()
        if row:
            id, nome, cnpj, endereco, telefone, email = row
            return ONG(nome, cnpj, endereco, telefone, email, id)
        return None

    def fechar_conexao(self):
        self.conn.close()
