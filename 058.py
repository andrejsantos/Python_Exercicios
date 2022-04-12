# melhore o jogo (desafio 28) onde o CPU vai pensar em um numero e vc tem que adivinhar qual é entre 0 e 10.
#só que agora vc vai ter chances até acertar , mostrando no final quantos palpites foram nececarios para acertar.
from random import randint
print('ADIVINHE O NUMERO DE 0 A 10')
sorteio = randint(0, 10)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Em qual numero eu estou pensando:'))
    palpites += 1
    if jogador == sorteio:
        acertou = True
    else:
        if jogador < sorteio:
            print('MAIS!')
        elif jogador > sorteio:
            print('MENOS!')
print('Você acertou com {} tentativas'. format(palpites))
