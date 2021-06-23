#faça um programa que indentifique se ele é par ou impar
num = int(input('digite um numero:'))
if num % 2 == 0:
    print('o numero:{} é par'.format(num))
else:
    print('o numero:{} é impar'.format(num))