#caulcule a nota media do aluno
p1 =int(input('prova 1:'))
p2 =int(input('prova 2:'))
p3 =int(input('prova 3:'))
p4 =int(input('prova 4:'))
p5 =int(input('prova 5:'))

nt = (p1+p2+p3+p4+p5)/5

print('\033[34mmedia do aluno:{}\033[m'.format(nt))