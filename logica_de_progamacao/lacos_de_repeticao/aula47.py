import os

palavra_secreta = "Limao".lower()
letras_acertadas = ''
contador_de_tentativas = 0

while True:
    letra_digita = input("Digite uma letra: ")
    ontador_de_chances += 1
    if len(letra_digita) > 1:
        print("Digite apenas uma letra")
        continue

    if letra_digita in palavra_secreta:
        letras_acertadas += letra_digita

    palavra_formada = ""

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += "*"

    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system("clear")
        print("!! Voce Descobriu a Palavra secreta !!")
        print(f"Palvra secreta: {palavra_secreta}")
        print(f"Tentativas: {contador_de_tentativas}")
