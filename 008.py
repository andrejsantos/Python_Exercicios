#fazer um programa que converta metros em centimetros
m =int(input('digte a metragem aqui:'))
km = m /100000
hm = m /10000
dam = m /1000
dm = m /10
cm = m *10
mm = m *1000
print('metros digitados:\033[1;36m{}\033[m.m\nconvertido em:{}.km\nconvertido em hectometro:{}.hm\n'.format(m, km, hm,))
print('convertidos decametro:{}.dam\n convertido em decimetro:\033[33;4m{}\033[m.dm\nconvertidos em:{}.cm\nconvertidos em:{}.mm'.format(dam, dm, cm, mm))