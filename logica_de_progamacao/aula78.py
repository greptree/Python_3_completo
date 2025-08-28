import copy

pessoa = { 
    "nome": "Edward", 
    "sobrenome": "Wong Hau Pepelu Tivruski IV", 
    "haircolor": "red", 
    "nascimento": {"dia": 1, "mes": "janeiro","ano" : 1958}
      } 

# copy -> retorna uma copia rasa "Shallow copy"

# pessoa2 = pessoa -> so estaria apontando para o dicionario na memoria

pessoa2 = pessoa.copy() # copia rasa do dicinario pessoa , agora tem dois dicinarios 

pessoa2["nome"] = "david"

print(pessoa["nome"])
print(pessoa2["nome"])

# GIANT OBS : se tiver algum dado mutavel ou seja algo como lista. ele vai copiar e refenrenciar para lista copiada.
# oque acontece e se eu mudar algo na lista copiada ele vai mudar na lista principal.

# por um lado e bom se tiver valores que forem mutaveis 

# usar copy se  for usar apenas os imutaveis.


# podemops usar o import copy , para deepcopy que seria um copy mais duro caso queira alterar o a lista e os mutaveis.

pessoa3 = copy.deepcopy(pessoa)
print(pessoa["nome"] + f" deepcopy")