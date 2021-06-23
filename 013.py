#fazer o programa que caucula a porcentagem adicional no salario
A =float(input('salario atual?'))
B =float(input('porcentagem:'))
C =(B/100)
D =C*A
E =float(D+A)
print('salario com a porcentagem adicional:{}'.format(E))