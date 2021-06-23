#refazer o disafio 35 com mais detalhes
r1 = int(input('digite a primeira reta:'))
r2 = int(input('digite a segunda reta:'))
r3 = int(input('digite a terceira reta:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
     print('as retas {}, {}, {} conseguem formar um triangulo'.format(r1, r2 ,r3), end=' ')
     if r1 == r2 == r3:
          print('EQUILÁTERO')
     elif r1 != r2 != r3 != r1:
      print('ESCALENO')
     else:
          print('ISOCELES')
else:
     print('não podem formar um triangolo')