# Aula sobre Estruturas de dados (colecacoes)
# escolhido hoje foi set

# Ate o momento ja estudei sobre.
# 

# Set e parecido com conjuntos numericos, Diagrama de Venn.

# criando set

# set so aceita valores imutaveis.

numeros = set() # cria um dicionario vazio
nomes = {"maria","ana","debora"} # consegue setar valores por padrao. porem nao garente a ordem.

print(nomes)


# Peculariedades de set

# ilimina valores 

super_lista = [1,2,3,4,4,4,4,5,5,5,5,5,6,7,7,8,6,5,3,2,1,3,4,5,7,9,5,4,3]

# type coversion

list_set= set(super_lista) # Ira retornar apenas items nao repetidos. e tambem em formato de dicionario sem chave

new_list = list(list_set) # retorna uma lista

print(list_set)

# set nao tem indexes 
# set sao interaveis