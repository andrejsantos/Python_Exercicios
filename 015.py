#faça um programa que calcule o aluguel do carro
a =float(input('dias alugados:'))
b =float(input('km rodados:'))
aluguel =(a * 60) + (b *0.15)
print('total a pagar:{}R$'.format(aluguel))