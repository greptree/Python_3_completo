
numero_inteiro = input("Type an integer number: ")

try:
    numero_verificado = int(numero_inteiro)
    if numero_verificado == 0:
        print("zero")
    elif numero_verificado % 2 == 0:
        print("even number")
    else:
        print("odd number")
except:
    print("enter an integer")