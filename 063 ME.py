#escreva um programa que leia um numero "n" inteiro qualquer
#mostre na tela os "N" primeiros elementos de uma (sequencia fibbonacci).
n = int(input('Quantos termos você quer mostrar ?'))
t1 = 0
t2 = 1
print('{} - {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' - {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' - Fim!')
#RESOLUÇÃO FEITA 100% POR MIM DEPOIS DE TER ENTENDIDO. SEM OLHAR O RESULTADO.
