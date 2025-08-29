import random

for _ in range(100):
    nove_digitos = ''

    for _ in range(9):
        nove_digitos += str(random.randint(0,9))
    contagem_regresiva_1 = 10
    cpf_nove_digitos = nove_digitos[:9]
    resultado_1 = 0

    for digitos in cpf_nove_digitos:
        resultado_1 += int(digitos) * contagem_regresiva_1
        contagem_regresiva_1 -= 1

    multiplar_resultado = resultado_1 * 10
    digito_1 = multiplar_resultado % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0

    cpf_dez_digitos = cpf_nove_digitos + str(digito_1)
    contagem_regresiva_2 = 11
    resultado_2 = 0

    for digitos in cpf_dez_digitos:
        resultado_2 += int(digitos) * contagem_regresiva_2
        contagem_regresiva_2 -= 1


    multiplar_resultado_2 = resultado_2 * 10
    digito_2 = multiplar_resultado_2 % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    cpf_gerado_pelo_calculo = f"{cpf_nove_digitos}{digito_1}{digito_2}"

    print(cpf_gerado_pelo_calculo)