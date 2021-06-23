#faça um programa que leia um numero real qualquer e mostre seu valor inteiro
from math import trunc
num =float((input('digite um numero:')))
R =trunc(num)
print('o numero:{} tem parte inteira de:{}'.format(num, R))
