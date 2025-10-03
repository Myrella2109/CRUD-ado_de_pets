from create import cadastrar_pet_poo
from read import listar_pets, buscar_pet
from update import atualizar_pet, marcar_como_adotado
from delete import remover_pet
from dicionario import pets
from models import Pet


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

    if opcao == "1":
        cadastrar_pet_poo()
    elif opcao == "2":
        listar_pets()
    elif opcao == "3":
        buscar_pet()
    elif opcao == "4":
        atualizar_pet()
    elif opcao == "5":
        marcar_como_adotado()
    elif opcao == "6":
        remover_pet()
    elif opcao == "0":
        print("Saindo do sistema. Até logo!")
        break
    else:
        print("Opção inválida.")
