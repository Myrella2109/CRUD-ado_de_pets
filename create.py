from models import Pet
from dicionario import pets

# Calcula o próximo ID disponível
proximo_id = max(int(k) for k in pets.keys()) + 1 if pets else 1
# Função para cadastrar um novo pet


def cadastrar_pet_poo():
    global proximo_id
    print("\n--- Cadastro de Novo Pet (POO) ---")
    nome = input("Nome do pet: ")

    while True:
        try:
            idade = int(input("Idade do pet: "))
            break
        except ValueError:
            print("Idade inválida. Por favor, digite um número inteiro.")
    raca = input("Raça do pet: ")
    especie = input("Espécie do pet: ")

    novo_pet_obj = Pet(
        id_pet=proximo_id, nome=nome, idade=idade, especie=especie, raca=raca
    )

    pets[str(proximo_id)] = novo_pet_obj.to_dict()
    print(f"\nPet '{nome}' cadastrado com sucesso! ID: {proximo_id}")
    proximo_id += 1  # Incrementa o próximo ID para o próximo cadastro
