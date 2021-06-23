# faça um programa que calcule o ano de nascimento e diga quantos anos ele tem e que nivel ele tá
import datetime
ano = int(input('que ano voê nasceu?:'))
atual = datetime.date.today().year
idade = atual - ano
print('idade todal:\033[4;34m{}\033[m'.format(idade))
if idade <= 9:
    print('você é um \033[1;31mMIRIM\033[m')
elif idade <= 14:
    print('você ainda é \033[1;32mINFANTIL\033[m')
elif idade <= 19:
    print('parabens você já é \033[1;33mJUNIOR\033[m')
elif idade <= 25:
    print('parabens você chegou no nivel:\033[1;36mSENIOR\033[m')
elif idade > 25:
    print('parabens você chegou ao nivel maximo:\033[1;30mMASTER\033[m')
