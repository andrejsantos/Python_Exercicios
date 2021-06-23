#escreva um programa que faça o computador pensar em um numero inteitoentre 0 e 5 para o usuario descobrir qual foi o numero escolhido.
#o programa deverá dizer se o usuario acertou ou errou
from random import randint
num = int(input('tente adivinhar o que eu estou pensando de 0 a 5,BOA SORTE!:'))
sorteio = randint(0, 5)
if sorteio == num:
    print('VOCÊ GANHOU!')
else:
    print('VOCÊ PERDEU!.o numero era:{},mais sorte na proxima'.format(sorteio))