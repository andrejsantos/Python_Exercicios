#Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep
def maior(* num):
    print('=*=' * 35)
    cont = maior = 0
    print('Analizando os valores')
    sleep(0.3)
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    sleep(0.5)
    print(f'foram informados {cont} valores ao todo.')
    print(f'O maior valor indformado foi {maior}.')


maior(2, 9, 4, 5, 6, 1)
maior(4, 7, 8)
maior(1, 2)
maior()
