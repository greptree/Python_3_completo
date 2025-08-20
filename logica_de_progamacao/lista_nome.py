# Crie uma lista com os nomes de 4 amigos e:
# Imprima todos os nomes.
# Troque o segundo nome por outro.
# Remova o último nome.

def mostrar_nomes(x):
    contador = 0
    for indices in nomes:
        print(f"Nome: {contador} {indices}")
        contador += 1

nomes = ["Pomni","Caine","Zooble","Jax","Kinger"]
mostrar_nomes(nomes)
print(nomes)
nomes[1] = "Raghata"
nome_removido = nomes.pop()

print(nomes)
