# manipulando dicionario chaves e valores.

pessoa = {} #criado dicionario pessoa

chave = "nome" # chave dinamica. 

pessoa[chave] = "David William" # criado "nome" : "David William"
pessoa["idade"] = 20

print(pessoa)
print(pessoa["idade"])
lista = []

pessoa[chave] = "Ichigo Kurosaki"
del pessoa["idade"]

print(pessoa[chave])

# print(lista[1]) #IndexError
# print(pessoa["nome1"]) #Keyerror

# CRUD CREATE READ UPDATE DELETE
# usar try cat para ver if retorna algum erro :D



