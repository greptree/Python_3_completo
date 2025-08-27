#criar funcoes que multiplica duplicam, triplicam e quadruplica.
#o numero recebido como paramentro.

def cria_multiplicando(multiplicando): # essa funcao recebe um multiplicando como argumento, recebe o argumento e retorna uma funcao interna.
    # clousure: funcao interna que lembra o valor da funcao externa passada.

    def cria_multilplicador(multiplicador): # cria um multiplicador.
        return multiplicando * multiplicador # recebe o valor da funcao externa vezes o valor da funcao interna atual.
    

    return cria_multilplicador # retorna a funcao interna.


multiplicar = cria_multiplicando(2) # variavel multiplicar recebe uma funcao cria_multiplicando com argumento (2) e retorna uma funcao interna.

dobro = multiplicar(2) # 2 * 2
triplo = multiplicar(3) # 2 * 3
quadruplica = multiplicar(4) # 2 * 4


print(dobro)
print(triplo)
print(quadruplica)
    
    