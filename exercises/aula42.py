frase = "Só uma mente livre de obstáculos é capaz de captar a beleza caótica do mundo.".lower() #assasins screed

i = 0
qtd_apareceu_mais = 0
letra_apareceu_mais_vezes = " "

while i < len(frase):

    letra_atual = frase[i]
    qnt_de_x_letra_apareceu = frase.count(letra_atual)
    

    if letra_atual != " ":
        
        if qnt_de_x_letra_apareceu > qtd_apareceu_mais:
            qtd_apareceu_mais = qnt_de_x_letra_apareceu
            letra_apareceu_mais_vezes = letra_atual
    i += 1

print(qtd_apareceu_mais,letra_apareceu_mais_vezes)