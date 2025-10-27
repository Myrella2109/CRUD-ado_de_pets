from funcoes import (
    cadastrar_pet_poo, listar_pets, buscar_pet, 
    atualizar_pet, marcar_como_adotado, remover_pet
)

# Função para exibir o menu
def menu():
    print("\n--- SISTEMA DE ADOÇÃO DE PETS ---")
    print("1. Cadastrar pet")
    print("2. Listar pets")
    print("3. Buscar pet por espécie")
    print("4. Atualizar pet")
    print("5. Marcar como adotado")
    print("6. Remover pet")
    print("0. Sair")


# Programa principal
while True:
    menu()
    opcao = input("Escolha uma opção: ")

    try:
        if opcao == "1":
            print("\n--- CADASTRO DE PET ---")
            nome = input("Nome do pet: ")
            # A idade deve ser um inteiro
            idade = int(input("Idade do pet: ")) 
            especie = input("Espécie (Ex: Cachorro, Gato): ")
            raca = input("Raça: ")
            
            cadastrar_pet_poo(nome, idade, especie, raca)
            print(f"✅ Pet '{nome}' cadastrado com sucesso!")
            
        elif opcao == "2":
            print("\n--- LISTA DE PETS DISPONÍVEIS ---")
            pets = listar_pets()
            if pets:
                for pet in pets:
                    # Formato: ID | NOME (IDADE) | ESPÉCIE/RAÇA | ADOTADO (0=Não, 1=Sim)
                    status_adotado = "Sim" if pet[5] == 1 else "Não"
                    print(f"ID: {pet[0]} | Nome: {pet[1]} ({pet[2]} anos) | Espécie: {pet[3]} / Raça: {pet[4]} | Adotado: {status_adotado}")
            else:
                print("Nenhum pet encontrado.")

        elif opcao == "3":
            print("\n--- BUSCAR PET POR ESPÉCIE ---")
            especie = input("Digite a espécie para buscar: ")
            pets = buscar_pet(especie)
            if pets:
                for pet in pets:
                    status_adotado = "Sim" if pet[5] == 1 else "Não"
                    print(f"ID: {pet[0]} | Nome: {pet[1]} ({pet[2]} anos) | Espécie: {pet[3]} / Raça: {pet[4]} | Adotado: {status_adotado}")
            else:
                print(f"Nenhum pet da espécie '{especie}' encontrado.")
                
        elif opcao == "4":
            print("\n--- ATUALIZAR DADOS DO PET ---")
            id_pet = int(input("Digite o ID do pet que deseja atualizar: "))
            nome = input("Novo nome do pet: ")
            idade = int(input("Nova idade do pet: "))
            especie = input("Nova espécie: ")
            raca = input("Nova raça: ")

            atualizar_pet(nome, idade, especie, raca, id_pet)
            print(f"✅ Pet com ID {id_pet} atualizado com sucesso!")
            
        elif opcao == "5":
            print("\n--- MARCAR PET COMO ADOTADO ---")
            id_pet = int(input("Digite o ID do pet para marcar como adotado: "))
            marcar_como_adotado(id_pet)
            print(f"✅ Pet com ID {id_pet} marcado como adotado!")
            
        elif opcao == "6":
            print("\n--- REMOVER PET ---")
            id_pet = int(input("Digite o ID do pet que deseja remover: "))
            remover_pet(id_pet)
            print(f"✅ Pet com ID {id_pet} removido com sucesso!")
            
        elif opcao == "0":
            print("Saindo do sistema. Até logo!")
            break
            
        else:
            print("Opção inválida.")
            
    except ValueError:
        print("⚠️ Erro: Por favor, digite um número inteiro para ID ou idade.")
    except Exception as e:
        print(f"❌ Ocorreu um erro: {e}")