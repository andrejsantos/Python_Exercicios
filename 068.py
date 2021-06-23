#faça um programa que jogue par ou impar com o computador. o jogo só será interrompido quando o jogador perder.
#mostrando o total de vitorias no final do jogo.
cpu = jogador = cpu = soma = v = 0
from random import randint
print('JOGO DE PAR OU IMPAR')
while True:
    jogador = int(input('Digite um numero:'))
    cpu = randint(0, 10)
    soma = jogador + cpu
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I]:')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {cpu}. O total é {soma}', end=' ')
    print('deu PAR'if soma % 2 == 0 else 'deu ÍMPAR')
    if escolha == 'P':
        if soma % 2 == 0:
            print('VOCÊ GANHOU!')
            v += 1
        else:
            print('VOCÊ PERDEU!')
            break
    elif escolha == 'I':
        if soma % 2 == 1:
            print('VOCÊ GANHOU!')
            v += 1
        else:
            print('VOCÊ PERDEU')
            break
    print('Vamos de novo!...')
print(f'FIM  DO JOGO... você venceu {v} vezes.')
#FEITO 80% SOZINHO