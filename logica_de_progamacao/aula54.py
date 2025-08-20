import os
lista_completa = ["Maca"]


while True:
    print("Selecione uma opcao")
    opcao_selecionada = input("[i]nserir [a]pagar [l]istar: ").lower()

    if opcao_selecionada == "i":
        os.system("clear")
        item_lista = input("Digite o item: ")
        lista_completa.append((item_lista))

    elif opcao_selecionada == "a":
        try:
            indice_apagar = int(input("digite o indice: "))
            lista_completa.pop(indice_apagar)
        except ValueError:
            print("Digite um número válido.")
        except IndexError:
            print("Impossível apagar, não existe esse índice.")
    
    elif opcao_selecionada == "l":
        os.system("clear")
        lista_enumerada = enumerate(lista_completa)
        if len(lista_completa) == 0:
            print("Lista vazia.")
        for indice,nome in lista_enumerada:
            print(f"{indice} - {nome}")
        