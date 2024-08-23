produtos = []
while True:
    nome = input("Nome do eletrônico: ")
    produtos.append(nome)
    resp = input("Deseja adicionar outro? (s|n): ").upper()
    if resp == "N":
        break

print(produtos)
