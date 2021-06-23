#refazer o desafil 009 com mais detalhes, mostrando a tabuada de um numero que o usuario escolher com o laço FOR
num = int(input('escolha o numero da tabuada:'))
print('\033[1;36m=-\033[m' *10)
for c in range(1, 11):
    resultado = c * num
    print('\033[1;33m{}\033[m X \033[1;33m{}\033[m = \033[1;34m{}\033[m'.format(c, num, resultado))
print('\033[1;36m=-\033[m' *10)