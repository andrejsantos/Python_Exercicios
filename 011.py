#informe a autura e largura da parede que eu falo quantos litros de tinta precisa para pintar
A =float(input('qual a altura da parede?'))
B =float(input('qual a largura da parede?'))
C = A*B
D = C/2
print('diametro da parede\033[36m{:.2f}x{:.2f}\033[m\n em metros é{}m²\n quantidade de tinta para pintar a parede{}L'.format(A, B, C, D ))