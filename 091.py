#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from operator import itemgetter
from random import randint
from time import sleep
jogo = {'jogador 1': randint(1, 6),
        'jogador 2': randint(1, 6),
        'jogador 3': randint(1, 6),
        'jogador 4': randint(1, 6)}
ranking = ()
print(f'{"==O JOGO==":>25}')
for J, D in jogo.items():
    print(f'O {J} Tirou:{D}')
    sleep(1)
print('=-' * 40)
print(f'{"==RANKING==":>25}')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}.')
    sleep(1)
