nome = "David William"
nome_alterado = "*"
contador = 0
while contador < len(nome):

    nome_alterado += f"{nome[contador]}*"
    contador += 1

print(nome_alterado)