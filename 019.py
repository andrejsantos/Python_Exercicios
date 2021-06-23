#fazer um programa que sorteie um aluno
from random import choice
n1 = str(input('digite o nome do aluno:'))
n2 = str(input('digite o nome do aluno:'))
n3 = str(input('digite o nome do aluno:'))
n4 = str(input('digite o nome do aluno:'))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('o aluno escolhido foi:{}'.format(escolhido))
