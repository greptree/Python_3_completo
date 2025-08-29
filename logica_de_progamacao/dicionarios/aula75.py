# pessoas em python

pessoa = {
    "nome" : "David",
    "nome_do_meio" : "William",
    "idade" : 19,
    "endereco": [
        {"Rua": "Rua99", "casa": "l23",},
        {"Rua": "23sad", "casa232": "l2sa3",}
]
}


# variavel recebe {} dicionario 
# "chave" = "valor"
# valor aceita valores tipos primitivos, listas,tuplas etc.
for chave in pessoa:
    print(chave, pessoa[chave])
    