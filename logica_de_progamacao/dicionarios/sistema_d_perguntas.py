# Exercico - de perguntas


def pergunta(lista,contador):
    return lista[contador].get("pergunta")

def resposta(lista,contador):
    return lista[contador].get("opcoes")

def resposta_correta(lista,contador):
    return lista[contador].get("resposta")


contador = 0
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

while contador < len(perguntas):

    print(pergunta(perguntas,contador))
    resposta_digitada = input(f"{resposta(perguntas,contador)}: ")
    resposta_certa = resposta_correta(perguntas,contador)

    if resposta_digitada == resposta_certa:
        print("voce acertou!!")
    else:
        print("voce errou!!")
        continue
        
    continuar = input("quer continuar? [y]es or [n]o: ")

    if continuar.lower() in "y":
        contador += 1
        continue

    break