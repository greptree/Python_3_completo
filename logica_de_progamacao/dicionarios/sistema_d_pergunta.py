import os
perguntas = [
    {
        "pergunta": "Quanto é 2 + 2?",
        "opcoes": ["1", "2", "3", "4"],
        "resposta": "4"
    },
    {
        "pergunta": "Qual é a capital da França?",
        "opcoes": ["Londres", "Paris", "Roma", "Berlim"],
        "resposta": "Paris"
    },
    {
        "pergunta": "Qual é o resultado de 5 * 3?",
        "opcoes": ["8", "15", "10", "20"],
        "resposta": "15"
    },
    {
        "pergunta": "Quem escreveu 'Dom Quixote'?",
        "opcoes": ["Shakespeare", "Miguel de Cervantes", "Tolstói", "Dante"],
        "resposta": "Miguel de Cervantes"
    },
    {
        "pergunta": "Qual é o maior planeta do Sistema Solar?",
        "opcoes": ["Terra", "Saturno", "Júpiter", "Marte"],
        "resposta": "Júpiter"
    }
]

contador = 0
acertos = 0

while contador < len(perguntas):

    pergunta = perguntas[contador]
    print(pergunta["pergunta"])
    print("")

    for indice,opcao in enumerate(pergunta["opcoes"]):
        print(f"{indice}) {opcao}")

    try:
        print("")
        escolher_opcao = int(input("Escolha uma opcao: "))

        if escolher_opcao > len(pergunta["opcoes"]) -1 :
            os.system("clear")
            print("⚠️ Opcao inexistente ⚠️")
            print("")
            continue

        if pergunta["opcoes"][escolher_opcao] == pergunta["resposta"]:
            os.system("clear")
            print("")
            print("Voce acertou ✅")
            print("")
            acertos += 1
        else:
            os.system("clear")
            print("Voce Errou ❌")
        
        contador += 1
        
    except ValueError:
         os.system("clear")
         print("⚠️ Digite um Opcao Valida!⚠️")
    

os.system("clear")
print(f"Acertos: {acertos}✅")
print(f"Erros: {contador - acertos}❌")