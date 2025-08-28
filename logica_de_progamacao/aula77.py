#metodos para dicionario 
pessoa = { 
    "nome": "Edward", 
    "sobrenome": "Wong Hau Pepelu Tivruski IV", 
    "haircolor": "red", 
    "nascimento": {"dia": 1, "mes": "janeiro","ano" : 1958}
      } 

print(len(pessoa)) # Retornar quantas chaves tem. 
print(pessoa.__len__()) # Retorna quantas chaves tem. dunder method in python 
print(list(pessoa.keys()))# metodo keys retornar as chaves > tratar o valor por que recebe dict_keys 
print(list(pessoa.values()))# metodo values retornar os valores das chaves. 
print(list(pessoa.items()))# metodo item retorna a chave o o valor correspondente. 
#print(pessoa["idade"]) retornaria um keyerror. 
pessoa.setdefault("idade",0) #chave e valor setado por padrao. obs: pouco usado metodo pouco usado.
print(pessoa["idade"]) #acessando chave do dicionario pessoa. 

# len 
# # keys 
# # values 
# # items 
# # setdefault