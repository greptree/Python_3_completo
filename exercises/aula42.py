frase = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. "\
"Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a".lower()

contador_letra = 0
maior_letra = ""

for contador in frase:
    if contador == " ":
        continue
    if frase.count(contador) > contador_letra:
        contador_letra = frase.count(contador)
        maior_letra = contador
    
print(f"{maior_letra},{contador_letra}")