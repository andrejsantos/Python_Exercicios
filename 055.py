#faça o programa que leia  o peso de cinco pessoas. no final, mostre qual foi o maior e o menor pesos lidos.
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('qual o peso da {}ª pessoa:'.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('esse é o manior peso:{}Kg'.format(maior))
print('esse é o menor peso:{}Kg'.format(menor))
#completo com 20% de ajuda(só a parte do else para baixo)