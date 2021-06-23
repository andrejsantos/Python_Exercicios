#escreva um programa que leia dois numeros e diga qual é o maior se não tiver ele fale que não tem numero maior
num1 = int(input('digite um numero:'))
num2 = int(input('digite outro numero:'))
if num1 > num2:
    print('o maior numero é\033[1:36m:{}\033[m'.format(num1))
elif num2 > num1:
    print('o maior numero é:\033[1;36m{}\033[m'.format(num2))
else:
    print('não existe numero maior')
