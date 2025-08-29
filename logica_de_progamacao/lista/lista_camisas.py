# Crie uma lista com 5 números e:
# Mostre o primeiro e o último elemento.
# Mostre o tamanho da lista (quantos elementos).
# Inverta a ordem dos elementos.

camisas_numeros = [1,7,10,11,23]
camisas_ultimo_numero = camisas_numeros[-1]
camisas_primeira_numero = camisas_numeros[0]

print(f"Primeira camisa: {camisas_primeira_numero}")
print(f"Ultima camisa:{camisas_ultimo_numero}")
print(f"Total de camisas: {len(camisas_numeros)}")
print(f"Camisas ordem invertida: {camisas_numeros[::-1]}")