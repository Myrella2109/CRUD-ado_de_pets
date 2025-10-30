# ==========================
# ARQUIVO: modelo.py
# ==========================
# Define as classes principais (entidades) do sistema:
# Pet, Cliente e ONG — aplicando conceitos de POO.
# ==========================


class Pet:
    def __init__(self, nome, idade, especie, raca, id=None, adotado=0):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.especie = especie
        self.raca = raca
        self.adotado = adotado  # 0 = não adotado, 1 = adotado

    def __str__(self):
        status = "✅ Adotado" if self.adotado else "🕓 Disponível"
        return f"[{self.id}] {self.nome} | {self.especie} - {self.raca} | Idade: {self.idade} | {status}"


class Cliente:
    def __init__(self, nome, cpf, telefone, email, id=None):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email

    def __str__(self):
        return f"[{self.id}] {self.nome} | CPF: {self.cpf} | Tel: {self.telefone} | Email: {self.email}"


class ONG:
    def __init__(self, nome, cnpj, endereco, telefone, email, id=None):
        self.id = id
        self.nome = nome
        self.cnpj = cnpj
        self.endereco = endereco
        self.telefone = telefone
        self.email = email

    def __str__(self):
        return f"[{self.id}] {self.nome} | CNPJ: {self.cnpj} | Endereço: {self.endereco} | Tel: {self.telefone} | Email: {self.email}"
