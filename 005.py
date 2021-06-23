#faça m rograma que leia um numero que vem antes de depois do numero digitado
a =int(input('\033[0;32;44mdigte um numero aqui:\033[m'))
n1 = a - 1
n2 = a + 1
print('\033[7mo numero antes desse é:{},o numero depois desse é:{}\033[m'.format(n1, n2))

#tambem pode-se usar o .format() de outra forma ex:
a =int(input('\033[33mdigte um numero aqui:\033[m'))
print('\033[1;36mo numero antes desse é:{},o numero depois desse é:\033[m{}'.format(a-1, a+1))
