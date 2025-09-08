# Função para atualizar dados de um pet
def atualizar_pet(pets):
    try:
        id_pet = int(input("Digite o ID do pet para atualizar: "))
        if id_pet in pets:
            print(f"Atualizando informações para o pet ID: {id_pet}")
            nome = input(f"Novo nome (atual: {pets[id_pet]['nome']}): ")
            idade = input(f"Nova idade (atual: {pets[id_pet]['idade']}): ")
            raca = input(f"Nova raça (atual: {pets[id_pet]['raca']}): ")
            especie = input(f"Nova espécie (atual: {pets[id_pet]['especie']}): ")
            
            if nome:
                pets[id_pet]['nome'] = nome
            if idade:
                pets[id_pet]['idade'] = int(idade)
            if raca:
                pets[id_pet]['raca'] = raca
            if especie:
                pets[id_pet]['especie'] = especie

            print("Informações atualizadas com sucesso!")
        else:
            print("ID inválido.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número para o ID e a idade.")

# Função para marcar um pet como adotado
def marcar_como_adotado(pets):
    try:
        id_pet = int(input("Digite o ID do pet para marcar como adotado: "))
        if id_pet in pets:
            if pets[id_pet]['adotado']:
                print("Este pet já foi adotado.")
            else:
                pets[id_pet]['adotado'] = True
                print(f"Pet '{pets[id_pet]['nome']}' marcado como adotado!")
        else:
            print("ID inválido.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")