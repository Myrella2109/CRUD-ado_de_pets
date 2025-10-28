from modelo import Pet
from funcoes import GerenciadorPets

# Instanciamos o Gerenciador de Pets para usar em todo o programa
# Ele já cuidará da conexão e da criação da tabela ao ser instanciado
gerenciador = GerenciadorPets() 

# Função para exibir o menu
def menu():
    print("\n--- SISTEMA DE ADOÇÃO DE PETS (POO) ---")
    print("1. Cadastrar pet")
    print("2. Listar todos os pets")
    print("3. Buscar pet por espécie")
    print("4. Atualizar dados do pet")
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
            idade = int(input("Idade do pet: ")) 
            especie = input("Espécie (Ex: Cachorro, Gato): ")
            raca = input("Raça: ")
            
            # 1. Cria o Objeto Pet
            novo_pet = Pet(nome, idade, especie, raca) 
            # 2. Passa o Objeto para o Gerenciador salvar no banco
            pet_salvo = gerenciador.cadastrar_pet(novo_pet)
            
            print(f"✅ Pet '{pet_salvo.nome}' (ID: {pet_salvo.id}) cadastrado com sucesso!")
            
        elif opcao == "2":
            print("\n--- LISTA DE PETS ---")
            pets = gerenciador.listar_pets()
            if pets:
                for pet in pets:
                    # O método __str__ da classe Pet faz a formatação
                    print(pet) 
            else:
                print("Nenhum pet encontrado.")

        elif opcao == "3":
            print("\n--- BUSCAR PET POR ESPÉCIE ---")
            especie = input("Digite a espécie para buscar: ")
            pets = gerenciador.buscar_pet_por_especie(especie)
            if pets:
                for pet in pets:
                    print(pet)
            else:
                print(f"Nenhum pet da espécie '{especie}' encontrado.")
                
        elif opcao == "4":
            print("\n--- ATUALIZAR DADOS DO PET ---")
            id_pet = int(input("Digite o ID do pet que deseja atualizar: "))
            
            pet_existente = gerenciador.buscar_pet_por_id(id_pet)
            if not pet_existente:
                 print(f"⚠️ Erro: Pet com ID {id_pet} não encontrado.")
                 continue

            nome = input(f"Novo nome (Atual: {pet_existente.nome}): ") or pet_existente.nome
            # Garante que a idade seja um número, mas mantém a atual se vazio
            idade_input = input(f"Nova idade (Atual: {pet_existente.idade}): ")
            idade = int(idade_input) if idade_input else pet_existente.idade
            especie = input(f"Nova espécie (Atual: {pet_existente.especie}): ") or pet_existente.especie
            raca = input(f"Nova raça (Atual: {pet_existente.raca}): ") or pet_existente.raca

            # 1. Cria um novo objeto Pet (ou reutiliza) com os novos dados
            pet_para_atualizar = Pet(nome, idade, especie, raca, id_pet, pet_existente.adotado)
            
            # 2. Passa o Objeto para o Gerenciador atualizar no banco
            gerenciador.atualizar_pet(pet_para_atualizar)
            print(f"✅ Pet com ID {id_pet} atualizado com sucesso!")
            
        elif opcao == "5":
            print("\n--- MARCAR PET COMO ADOTADO ---")
            id_pet = int(input("Digite o ID do pet para marcar como adotado: "))
            pet_existente = gerenciador.buscar_pet_por_id(id_pet)
            if not pet_existente:
                 print(f"⚠️ Erro: Pet com ID {id_pet} não encontrado.")
                 continue
                 
            gerenciador.marcar_como_adotado(id_pet)
            print(f"✅ Pet com ID {id_pet} marcado como adotado!")
            
        elif opcao == "6":
            print("\n--- REMOVER PET ---")
            id_pet = int(input("Digite o ID do pet que deseja remover: "))
            pet_existente = gerenciador.buscar_pet_por_id(id_pet)
            if not pet_existente:
                 print(f"⚠️ Erro: Pet com ID {id_pet} não encontrado.")
                 continue
                 
            gerenciador.remover_pet(id_pet)
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