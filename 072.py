#crei um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte
#seu programa deverá ler um numero (entre 0 e 20) e mostralo por extense.
numeros = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze','treze', 'quatoze',
           'quinze', 'dezeseis', 'dezesete', 'dezoito',
           'dezenove', 'vinte')
while True:
    res = int(input('Digite um numero de 0 a 20:'))
    if 0 <= res <= 20:
        print(f'Você digitou: {numeros[res]}')
    elif res > 20:
        print('Numero invalido')
    cont = str(input('Deseja continuar?[S/N]:')).upper().strip()
    if cont == 'N':
        break
print('Tenha um otimo dia')
