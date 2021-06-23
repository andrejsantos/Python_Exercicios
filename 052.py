# faça um programa que leia um numero inteiro e diga se ele é um numero primo ou não
num = int(input('digite um numero:'))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[36m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mo numero {} foi divisivel {} vezes'.format(num, total))
if total == 2:
    print('ESSE É UM NUMERO PRIMO')
else:
    print('ESSE NÃO É UM NUMERO PRIMO')

# completo  com 70% de ajuda
