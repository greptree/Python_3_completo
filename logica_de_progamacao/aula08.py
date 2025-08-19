nome = ""
sobrenome = ""
idade = 17
maior_idade = (idade >= 18)
ano_nascimento = 2025 - idade
altura_em_metros = 1.65
print(maior_idade)

def check_idade(x):
    if(x):
        print("Maior de idade")

    if(not x):
        print("Menor de idade")


print(f"Nome: {nome}")
print(f"Sobrenome: {sobrenome}")
print(f"Idade: {idade}")
print(f"Ano de Nascimento: {ano_nascimento}")
check_idade(maior_idade)
print(f"Altura em metros; {altura_em_metros}")
