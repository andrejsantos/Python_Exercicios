#escreva um programa que leia a idade de um jovem e diga se ele ainda tem que se alistar ou se já passou do tempo
from datetime import date
atual = date.today().year
nasc = int(input('ano de nascimento:'))
idade = atual - nasc
print('quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('você tem que se alistar esse ano')
elif idade < 18:
    saldo = 18 - idade
    print('ainda falta {} anos para você se alistar'.format(saldo))
elif idade >18:
    saldo = idade - 18
    print('você ja deveria ter se alistado a {} anos'.format(saldo))
