import sqlite3
from modelo import Pet # Importa a classe Pet

class GerenciadorPets:
    def __init__(self, nome_banco="pets.db"):
        self.nome_banco = nome_banco
        self._conectar_e_criar_tabela()

    def _conectar_e_criar_tabela(self):
        """Conecta ao banco e cria a tabela se não existir."""
        conn = sqlite3.connect(self.nome_banco)
        cursor = conn.cursor()
        
        # Criação da tabela (seu código banco.py migrado para o __init__)
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
        
        conn.commit() 
        conn.close() 

    def _executar_query(self, query, parametros=()):
        """Função auxiliar para conectar, executar e fechar a conexão."""
        conn = sqlite3.connect(self.nome_banco)
        cursor = conn.cursor()
        cursor.execute(query, parametros)
        
        # Se for um SELECT, retorna os resultados
        if query.strip().upper().startswith("SELECT"):
            resultado = cursor.fetchall()
            conn.close()
            return resultado
        else:
            conn.commit()
            conn.close()
            # Para INSERT, retorna o ID da última linha inserida
            if query.strip().upper().startswith("INSERT"):
                 return cursor.lastrowid
            return None
    
    # --- MÉTODOS CRUD ---

    def cadastrar_pet(self, pet: Pet):
        """Cadastra um novo pet no banco de dados."""
        query = "INSERT INTO pets (nome, idade, especie, raca) VALUES (?, ?, ?, ?)"
        pet_id = self._executar_query(query, pet.to_tuple_insert())
        pet.id = pet_id # Atualiza o ID no objeto Pet
        return pet

    def listar_pets(self):
        """Lista todos os pets e retorna uma lista de objetos Pet."""
        query = "SELECT * FROM pets"
        dados = self._executar_query(query)
        # Transforma cada tupla de dados em um objeto Pet
        pets = [Pet(dado[1], dado[2], dado[3], dado[4], dado[0], dado[5]) for dado in dados]
        return pets

    def buscar_pet_por_especie(self, especie):
        """Busca pets por espécie e retorna uma lista de objetos Pet."""
        query = "SELECT * FROM pets WHERE especie LIKE ?"
        dados = self._executar_query(query, (f'%{especie}%',))
        # Transforma cada tupla de dados em um objeto Pet
        pets = [Pet(dado[1], dado[2], dado[3], dado[4], dado[0], dado[5]) for dado in dados]
        return pets
    
    def buscar_pet_por_id(self, id_pet):
        """Busca um pet por ID e retorna um objeto Pet ou None."""
        query = "SELECT * FROM pets WHERE id = ?"
        dados = self._executar_query(query, (id_pet,))
        if dados:
             # Retorna o primeiro e único resultado como objeto Pet
            dado = dados[0]
            return Pet(dado[1], dado[2], dado[3], dado[4], dado[0], dado[5])
        return None

    def atualizar_pet(self, pet: Pet):
        """Atualiza todos os dados (exceto 'adotado') de um pet existente."""
        query = "UPDATE pets SET nome = ?, idade = ?, especie = ?, raca = ? WHERE id = ?"
        self._executar_query(query, pet.to_tuple_update())

    def marcar_como_adotado(self, id_pet):
        """Muda o status 'adotado' do pet para 1 (Sim)."""
        query = "UPDATE pets SET adotado = 1 WHERE id = ?"
        self._executar_query(query, (id_pet,))

    def remover_pet(self, id_pet):
        """Remove um pet do banco de dados pelo ID."""
        query = "DELETE FROM pets WHERE id = ?"
        self._executar_query(query, (id_pet,))