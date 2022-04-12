#crie um programa que vai gerar cinco nuúmeros aleatorios e colocar em uma tupla.
#depois disso, mostre a listagem de numeros gerados e tambem indique o menor e o maio valor que estão na tupla.
from random import randint
num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os numeros sorteados foram:', end='')
for n in num:
    print(f'{n}', end=' ')
print(f'\nO maior numero sorteado foi: {max(num)}')
print(f'O menor número sorteado foi: {min(num)}')
