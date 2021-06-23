#faça um programa que leia um numero qualquer e mostre o seu fatorial.
num = int(input('digite um numero para calcular seu fatorial:'))
c = num
f = 1
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
