#Exercicio de progamacao - Calculo do IMC

import os


print("Calculadora de IMC")
print("------------------")
print()

nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura"))
peso = float(input("Digite seu peso"))
imc = peso / (altura * altura)

print(f"seu imc e : {imc:.2f}")