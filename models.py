# models.py ou dentro do seu arquivo principal

class Pet:
    # Este é o construtor, que será chamado quando você criar um novo Pet.
    def __init__(self, id_pet, nome, idade, especie, raca):
        # O 'self' representa a instância (o objeto) que está sendo criado.
        self.id = id_pet
        self.nome = nome
        self.idade = idade
        self.especie = especie
        self.raca = raca
        self.adotado = False # Atributo padrão para todo novo Pet
        
    # Opcional: Adicionar um método especial para facilitar a visualização do objeto
    def __str__(self):
        return f"ID: {self.id} | Nome: {self.nome} | Espécie: {self.especie} | Adotado: {'Sim' if self.adotado else 'Não'}"

    # Opcional: Adicionar um método para converter o objeto em um dicionário (útil para salvar)
    def to_dict(self):
        return {
            'nome': self.nome,
            'idade': self.idade,
            'especie': self.especie,
            'raca': self.raca,
            'adotado': self.adotado
        }