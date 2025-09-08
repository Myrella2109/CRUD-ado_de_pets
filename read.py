
# Função para listar todos os pets
def listar_pets(pets):
    if not pets:
        print("Nenhum pet cadastrado.")
        return
    for id_pet, dados in pets.items():
        status = "Adotado" if dados['adotado'] else "Disponível"
        print(f"\nID: {id_pet} | Nome: {dados['nome']} | Idade: {dados['idade']} | Raça: {dados['raca']} | Especie: {dados['especie']}| Status: {status}")

# Função para buscar pet por nespecie
def buscar_pet(pets):
    especie_busca = input("Digite a espécie do pet para buscar: ").lower()
    encontrados = []
    for id_pet, dados in pets.items():
        if dados['especie'].lower() == especie_busca:
            encontrados.append((id_pet, dados))
    if encontrados:
        for id_pet, dados in encontrados:
            status = "Adotado" if dados['adotado'] else "Disponível"
            print(f"\nID: {id_pet} | Nome: {dados['nome']} | Idade: {dados['idade']} | Raça: {dados['raca']} | Especie: {dados['especie']}| Status: {status}")
    else:
        print("Nenhum pet dessa espécie foi encontrado.")

