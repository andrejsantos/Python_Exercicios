#fazer um programa que faça a soma somente de numeros PAR se for IMPAR ele vai descartar
soma = 0
for c in range(1, 7):
    num = int(input('digite um valor:'))
    if num % 2 == 0:
        soma += num
print('a soma dos numeros pares é:{}'.format(soma))
#completo mas com ajuda
