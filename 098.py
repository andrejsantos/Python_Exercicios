#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
from time import sleep
def contador(i, f, p):
    if p < 0:
        p += -1
    if p == 0:
        p = 1
    print('=-' * 35)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        cont = 1
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            cont -= p
            sleep(0.5)
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('Sua vez de personalizar')
ini = int(input('Inicio:'))
fim = int(input('Fim:'))
pas = int(input('Passo:'))
contador(ini, fim, pas)
