from dicionario import pets

# Calcula o próximo ID disponível
proximo_id = max(pets.keys()) + 1 if pets else 1
# Função para cadastrar um novo pet
def cadastrar_pet():
    global proximo_id
    nome = input("Nome do pet: ")
    idade = int(input("Idade do pet: "))
    raca = input("Raça do pet: ")
    especie = input("Espécie do pet: ")

    novo_pet = {
        'nome': nome,
        'idade': idade,
        'especie': especie,
        'raca': raca,
        'adotado': False
    }
    pets[proximo_id] = novo_pet
    print(f"\nPet '{nome}' cadastrado com sucesso! ID: {proximo_id}")
    proximo_id += 1 # Incrementa o próximo ID para o próximo cadastro