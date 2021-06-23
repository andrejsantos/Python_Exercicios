#faça um programa que resolva o teorema de pitagora
from math import hypot
Ca =float(input('cateto adjacente:'))
Co =float(input('cateto oposto:'))
hi = hypot(Co, Ca)
print('hipotenusa vai medir:{:.2f}'.format(hi))