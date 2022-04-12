#refaça o (desafio 051), lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros da progressão usando a estrutura while.
t = int(input('Primeiro termo:'))
r = int(input('Razão:'))
termo = t
c = 1
while c <= 10:
    print('{} - '.format(termo), end='')
    termo += r
    c +=1
print('FIM!')
