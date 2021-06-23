#escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual será a base de converção
numero = int(input('digite um numero:'))
print('1 BINÁRIO')
print('2 OCTAL')
print('3 HEXADECIMAL')
escolha = int(input('qual base de converção você quer?'))
if escolha == 1:
    print('o numero:{}, convertido em binário fica:{}'.format(numero, bin(numero)[2:]))
elif escolha == 2:
    print('o numero:{}, convertido em octal fica:{}'.format(numero, oct(numero)[2:]))
elif escolha == 3:
    print('o numero:{}, convertido em hexadecimal fica:{}'.format(numero, hex(numero)[2:]))
else:
    print('não foi escolhido nenhuma das opções!')

