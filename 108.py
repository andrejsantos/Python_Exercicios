#Exercício Python 108: Adapte o código do desafio #107,
#criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.
from modulos1 import moeda
n = float(input("Digite um valor:"))
print(f'A metade de {moeda.moeda(n)} é:{moeda.moeda(moeda.metade(n))} ')
print(f'O dobro de {moeda.moeda(n)} é: {moeda.moeda(moeda.dobro(n))} ')
print(f'Aumentando 10% temos: {moeda.moeda(moeda.aumentar(n, 10))}')
