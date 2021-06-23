#faça um programa que caucule a soma entre todos os numeros impares que são múltiplos de três entre 1 e 500
for c in range(0, 500):
    if c % 3 == 0:
        print('esse numero é multiplo de 3:\033[4;36m{}\033[m'.format(c))
    else:
        print('\033[1;33m=\033[m'*35)
