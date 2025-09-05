# Dicionário para armazenar os pets
# Convertendo a lista inicial em um dicionário para facilitar o acesso por ID
pets = {
    1: {
        "nome": "Rex",
        "especie": "Cachorro",
        "idade": 3,
        "raca": "Labrador",
        "adotado": False
    },
    2: {
        "nome": "Mimi",
        "especie": "Gato",
        "idade": 2,
        "raca": "Persa",
        "adotado": False
    },
    3: {
        "nome": "Bidu",
        "especie": "Cachorro",
        "idade": 5,
        "raca": "Poodle",
        "adotado": False
    },
    4: {
        "nome": "Nina",
        "especie": "Gato",
        "idade": 1,
        "raca": "Siamês",
        "adotado": False
    },
    5: {
        "nome": "Thor",
        "especie": "Cachorro",
        "idade": 4,
        "raca": "Pitbull",
        "adotado": False
    }
}
# A chave "id" dentro do dicionário não é mais necessária, já que o ID agora é a chave principal.
# Além disso, o status de adoção "Disponível" foi substituído por False, que é mais fácil de ser gerenciado pelo código.

# Calcula o próximo ID disponível
proximo_id = max(pets.keys()) + 1 if pets else 1

# Função para cadastrar um novo pet
def cadastrar_pet(pets):
    global proximo_id
    nome = input("Nome do pet: ")
    idade = int(input("Idade do pet: "))
    raca = input("Raça do pet: ")
    especie = input("Especie do pet: ")

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

# Função para listar todos os pets
def listar_pets(pets):
    if not pets:
        print("Nenhum pet cadastrado.")
        return
    for id_pet, dados in pets.items():
        status = "Adotado" if dados['adotado'] else "Disponível"
        print(f"\nID: {id_pet} | Nome: {dados['nome']} | Idade: {dados['idade']} | Raça: {dados['raca']} | Status: {status}")

# Função para buscar pet por nome
def buscar_pet(pets):
    nome_busca = input("Digite o nome do pet para buscar: ").lower()
    encontrados = []
    for id_pet, dados in pets.items():
        if dados['nome'].lower() == nome_busca:
            encontrados.append((id_pet, dados))

    if encontrados:
        for id_pet, dados in encontrados:
            status = "Adotado" if dados['adotado'] else "Disponível"
            print(f"\nID: {id_pet} | Nome: {dados['nome']} | Idade: {dados['idade']} | Raça: {dados['raca']} | Status: {status}")
    else:
        print("Nenhum pet com esse nome foi encontrado.")

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

# Função para exibir o menu
def menu():
    print("\n--- SISTEMA DE ADOÇÃO DE PETS ---")
    print("1. Cadastrar pet")
    print("2. Listar pets")
    print("3. Buscar pet por nome")
    print("4. Atualizar pet")
    print("5. Marcar como adotado")
    print("6. Remover pet")
    print("0. Sair")

# Programa principal
while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        cadastrar_pet(pets)
    elif opcao == '2':
        listar_pets(pets)
    elif opcao == '3':
        buscar_pet(pets)
    elif opcao == '4':
        atualizar_pet(pets)
    elif opcao == '5':
        marcar_como_adotado(pets)
    elif opcao == '6':
        remover_pet(pets)
    elif opcao == '0':
        print("Saindo do sistema. Até logo!")
        break
    else:
        print("Opção inválida.")