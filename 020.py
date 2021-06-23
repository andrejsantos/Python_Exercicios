#faça um programa que faça um sorteio e mostre a ordem dos sorteados
from random import shuffle
n1 = str(input('digite o nome do aluno:'))
n2 = str(input('digite o nome do aluno:'))
n3 = str(input('digite o nome do aluno:'))
n4 = str(input('digite o nome do aluno:'))
lista = [n1, n2, n3, n4,]
shuffle(lista)
print('ordem do sorteio é{}'.format(lista))