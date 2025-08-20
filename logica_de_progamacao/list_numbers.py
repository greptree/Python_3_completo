# Peça para o usuário digitar 5 números e guarde em uma lista

numeros = []
while True:
    numero_digitado = float(input("numero: "))
    numeros.append(numero_digitado)

    maior_numero = numeros[0]
    for numero_list in numeros:
        if numero_list > maior_numero:
            maior_numero = numero_list
    
    if len(numeros) > 4:
        soma = 0
        for numero_soma in numeros:
            soma += numero_soma

        print(numeros)
        print(f"maior numero {maior_numero}")
        print(f"Soma dos numeros: {soma}")
        break

 