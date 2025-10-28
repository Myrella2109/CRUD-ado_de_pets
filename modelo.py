class Pet:
    def __init__(self, nome, idade, especie,raca, id_pet=None, adotado=0):
        self.id=id_pet
        self.nome=nome
        self.idade=idade
        self.especie=especie
        self.raca=raca
        self.adotado=adotado

    def __str__(self):
        status="Adotado" if self.adotado==1 else "Disponível"
        return f"ID: {self.id} | Nome: {self.nome} ({self.idade} anos)| Espécie:{self.especie}| Raça: {self.raca}| Status: {status}"    

    def to_tuple_insert(self):
        """Retorna os dados do Pet como uma tupla para INSERT."""
        # Sem o ID e 'adotado' (que usa DEFAULT)
        return (self.nome, self.idade, self.especie, self.raca)

    def to_tuple_update(self):
        """Retorna os dados do Pet como uma tupla para UPDATE."""
        # Nome, Idade, Especie, Raca, ID
        return (self.nome, self.idade, self.especie, self.raca, self.id)  