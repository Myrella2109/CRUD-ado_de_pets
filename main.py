from modelo import Pet, Cliente, ONG
from funcoes import GerenciadorPets, GerenciadorClientes, GerenciadorONGs

# Instanciando os gerenciadores
gerenciador_pets = GerenciadorPets()
gerenciador_clientes = GerenciadorClientes()
gerenciador_ongs = GerenciadorONGs()

# ---------------- MENU PRINCIPAL ----------------
def menu_principal():
    print("\n=== SISTEMA DE ADOÇÃO DE PETS (POO) ===")
    print("1. Gerenciar Pets")
    print("2. Gerenciar ONGs")
    print("3. Clientes (Consulta e Adoção)")
    print("0. Sair")

# ---------------- MENU PETS ----------------
def menu_pets():
    print("\n--- MENU DE PETS ---")
    print("1. Cadastrar Pet")
    print("2. Listar Pets")
    print("3. Buscar Pet por Espécie")
    print("4. Atualizar Pet")
    print("5. Marcar como Adotado")
    print("6. Remover Pet")
    print("0. Voltar")

# ---------------- MENU ONGs ----------------
def menu_ongs():
    print("\n--- MENU DE ONGs ---")
    print("1. Cadastrar ONG")
    print("2. Listar ONGs")
    print("3. Atualizar ONG")
    print("4. Remover ONG")
    print("0. Voltar")

# ---------------- MENU CLIENTES ----------------
def menu_clientes():
    print("\n--- MENU DE CLIENTES ---")
    print("1. Cadastrar Cliente")
    print("2. Listar Clientes")
    print("3. Consultar Pets Disponíveis")
    print("4. Adotar um Pet")
    print("0. Voltar")

# ---------------- PROGRAMA PRINCIPAL ----------------
while True:
    menu_principal()
    opcao = input("Escolha uma opção: ")

    # --- GERENCIAR PETS ---
    if opcao == "1":
        while True:
            menu_pets()
            op_pet = input("Escolha uma opção: ")
            try:
                if op_pet == "1":
                    nome = input("Nome do pet: ")
                    idade = int(input("Idade do pet: "))
                    especie = input("Espécie: ")
                    raca = input("Raça: ")
                    pet = Pet(nome, idade, especie, raca)
                    gerenciador_pets.cadastrar_pet(pet)
                    print(f"✅ Pet '{nome}' cadastrado com sucesso!")

                elif op_pet == "2":
                    pets = gerenciador_pets.listar_pets()
                    if pets:
                        print("\n🐾 Lista de Pets:")
                        for pet in pets:
                            print(pet)
                    else:
                        print("Nenhum pet cadastrado.")

                elif op_pet == "3":
                    especie = input("Espécie para buscar: ")
                    pets = gerenciador_pets.buscar_pet_por_especie(especie)
                    for pet in pets:
                        print(pet)

                elif op_pet == "4":
                    id_pet = int(input("ID do pet: "))
                    pet = gerenciador_pets.buscar_pet_por_id(id_pet)
                    if pet:
                        nome = input(f"Novo nome ({pet.nome}): ") or pet.nome
                        idade_in = input(f"Nova idade ({pet.idade}): ")
                        idade = int(idade_in) if idade_in else pet.idade
                        especie = input(f"Nova espécie ({pet.especie}): ") or pet.especie
                        raca = input(f"Nova raça ({pet.raca}): ") or pet.raca
                        pet_atualizado = Pet(nome, idade, especie, raca, id_pet, pet.adotado)
                        gerenciador_pets.atualizar_pet(pet_atualizado)
                        print("✅ Pet atualizado com sucesso!")
                    else:
                        print("Pet não encontrado.")

                elif op_pet == "5":
                    id_pet = int(input("ID do pet: "))
                    gerenciador_pets.marcar_como_adotado(id_pet)
                    print("✅ Pet marcado como adotado!")

                elif op_pet == "6":
                    id_pet = int(input("ID do pet: "))
                    gerenciador_pets.remover_pet(id_pet)
                    print("✅ Pet removido com sucesso!")

                elif op_pet == "0":
                    break
                else:
                    print("Opção inválida.")

            except Exception as e:
                print(f"❌ Erro: {e}")

    # --- GERENCIAR ONGs ---
    elif opcao == "2":
        while True:
            menu_ongs()
            op_ong = input("Escolha uma opção: ")
            try:
                if op_ong == "1":
                    nome = input("Nome da ONG: ")
                    cnpj = input("CNPJ: ")
                    endereco = input("Endereço: ")
                    telefone = input("Telefone: ")
                    email = input("E-mail: ")
                    ong = ONG(nome, cnpj, endereco, telefone, email)
                    gerenciador_ongs.cadastrar_ong(ong)
                    print(f"✅ ONG '{nome}' cadastrada com sucesso!")

                elif op_ong == "2":
                    ongs = gerenciador_ongs.listar_ongs()
                    if ongs:
                        print("\n🏢 Lista de ONGs:")
                        for ong in ongs:
                            print(ong)
                    else:
                        print("Nenhuma ONG cadastrada.")

                elif op_ong == "3":
                    id_ong = int(input("ID da ONG: "))
                    ong = gerenciador_ongs.buscar_ong_por_id(id_ong)
                    if ong:
                        nome = input(f"Novo nome ({ong.nome}): ") or ong.nome
                        cnpj = input(f"Novo CNPJ ({ong.cnpj}): ") or ong.cnpj
                        endereco = input(f"Novo endereço ({ong.endereco}): ") or ong.endereco
                        telefone = input(f"Novo telefone ({ong.telefone}): ") or ong.telefone
                        email = input(f"Novo e-mail ({ong.email}): ") or ong.email
                        ong_atualizada = ONG(nome, cnpj, endereco, telefone, email, id_ong)
                        gerenciador_ongs.atualizar_ong(ong_atualizada)
                        print("✅ ONG atualizada com sucesso!")
                    else:
                        print("ONG não encontrada.")

                elif op_ong == "4":
                    id_ong = int(input("ID da ONG a remover: "))
                    gerenciador_ongs.remover_ong(id_ong)
                    print("✅ ONG removida com sucesso!")

                elif op_ong == "0":
                    break
                else:
                    print("Opção inválida.")

            except Exception as e:
                print(f"❌ Erro: {e}")

    # --- CLIENTES ---
    elif opcao == "3":
        while True:
            menu_clientes()
            op_cli = input("Escolha uma opção: ")
            try:
                if op_cli == "1":
                    nome = input("Nome do cliente: ")
                    cpf = input("CPF: ")
                    telefone = input("Telefone: ")
                    email = input("E-mail: ")
                    cliente = Cliente(nome, cpf, telefone, email)
                    gerenciador_clientes.cadastrar_cliente(cliente)
                    print(f"✅ Cliente '{nome}' cadastrado com sucesso!")

                elif op_cli == "2":
                    clientes = gerenciador_clientes.listar_clientes()
                    if clientes:
                        print("\n👤 Lista de Clientes:")
                        for cli in clientes:
                            print(cli)
                    else:
                        print("Nenhum cliente cadastrado.")

                elif op_cli == "3":
                    print("\n🐶 Pets disponíveis para adoção:")
                    pets = [p for p in gerenciador_pets.listar_pets() if not p.adotado]
                    if pets:
                        for pet in pets:
                            print(pet)
                    else:
                        print("Nenhum pet disponível no momento.")

                elif op_cli == "4":
                    cpf = input("Informe seu CPF: ")
                    cliente = gerenciador_clientes.buscar_cliente_por_cpf(cpf)
                    if not cliente:
                        print("⚠️ Cliente não encontrado. Cadastre-se primeiro.")
                        continue

                    pets = [p for p in gerenciador_pets.listar_pets() if not p.adotado]
                    if not pets:
                        print("Nenhum pet disponível para adoção.")
                        continue

                    for pet in pets:
                        print(pet)

                    id_pet = int(input("Digite o ID do pet que deseja adotar: "))
                    gerenciador_pets.marcar_como_adotado(id_pet)
                    print(f"🎉 Parabéns {cliente.nome}! Você adotou o pet com ID {id_pet}.")

                elif op_cli == "0":
                    break
                else:
                    print("Opção inválida.")

            except Exception as e:
                print(f"❌ Erro: {e}")

    # --- SAIR ---
    elif opcao == "0":
        print("\nEncerrando o sistema. Até logo! 🐾")
        gerenciador_pets.fechar_conexao()
        gerenciador_clientes.fechar_conexao()
        gerenciador_ongs.fechar_conexao()
        break

    else:
        print("Opção inválida, tente novamente.")
