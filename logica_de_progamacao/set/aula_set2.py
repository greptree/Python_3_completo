# metodos uteis com set() ler a documentacao para conhecer outros.

s1 = set()
s1.add("luiz") # adiciona valor no dicionario vazio

s1.add(1) # adiciona valor no dicionario
s1.update(("Hello World",1,2,3,4)) # usado para varios valores tomar cuidado com valores interaveis
s1.clear()# ira eliminar o set
s1.discard()# ira ilimnar algum valor do set passado como argumento.
print(s1)