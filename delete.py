# Função para remover um pet do sistema
def remover_pet(pets):
    try:
        id_pet = int(input("Digite o ID do pet para remover: "))
        if id_pet in pets:
            nome = pets[id_pet]['nome']
            del pets[id_pet]
            print(f"Pet '{nome}' removido com sucesso.")
        else:
            print("ID inválido.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
