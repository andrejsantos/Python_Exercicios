#que caucule o o peso e a altura e caulcule o IMC e diga a faixetaria dela
altura = float(input('qual a sua altura?'))
peso = float(input('qual o seu peso?'))
conta1 = altura * altura
conta2 = peso / conta1
resultado = conta2
print('o IMC é:\033[4;34m{:.1f}\033[m'.format(resultado))
if resultado < 18.5:
    print('\033[4;36mvocê está abaixo do peso\033[m')
elif resultado < 25:
    print('\033[4;32mvocê tem o peso ideal\033[m')
elif resultado < 30:
    print('\033[1;35mvocê está acima do peso\033{m')
elif resultado < 40:
    print('\033[1;33mobesidade\033[m')
else:
    print('\033[1;31mocbesidade morbida\033[m')
