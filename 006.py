#mostre o dobro, o triplo e a raiz do numero digitado
a =int(input('\033[4;31mdigte um numero aqui:\033[m'))
n1 = a * 2
n2 = a * 3
n3 = a ** (1/2)
print('\033[1;36mo dobro desse numero é:{}\n o triplo desse numero é numero é:{}\n a raiz quadrada desse numero é{:.2f}\033[m'.format(n1, n2, n3))