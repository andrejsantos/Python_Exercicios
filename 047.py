#crie um programa que mostre todos os numeros pares de 1 ao 50
for c in range(1, 51):
    if c % 2 == 0:
        print('esse numero é PAR:{}'.format(c))
    else:
        print('esse numero é IMPAR:{}'.format(c))
