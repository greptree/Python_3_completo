# get
# pop
# popitem
# update


p1 = {
    "nome" : "Max Verstappen",
    "time" : "Red Bull"
}

print(p1.get("nome")) # retorna o nome do mito
#print(p1.get("nome")) # se nao tivesse a chave o mito nao teria nome e retornaria None
#print(p1["nome"]) # retorna o nome do mito, mas se nao tivesse dava keyerror
print(p1.get("sobrenome", "nao existe")) # pode imprimir um valor se nao existir mas o mais comum e usar o None

retira_nome = p1.pop("nome") # aqui retira a chave e retora o valor

print(p1.keys())
print(retira_nome) 

p1["nome"] = "naruto"
print(p1.keys()) # agora o naruto pilota pra formula 1
print(p1.get("nome"))
ultimo_item = p1.popitem() # retorna uma tupla com chave e valor
print(ultimo_item)
print(p1)

# update

p1.update({
    "nome" : "Lando Norris",
    "time" : "Mc Larren"
})

print(p1, f"lista atualizada")