#faça um programa que leia 3 medidas de retas e diga se elas podem formar um triangulo
r1 = int(input('digite a primeira reta:'))
r2 = int(input('digite a segunda reta:'))
r3 = int(input('digite a terceira reta:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
     print('as retas {}, {}, {} conseguem formar um triangulo'.format(r1, r2 ,r3))
else:
     print('essas retas não conseguem formar um triangulo')