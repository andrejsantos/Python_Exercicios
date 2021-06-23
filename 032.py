#fazer um programa que leia o ano que foi digitado e diga se é um ano BISSEXTO
ano = int(input('digite o ano:'))
if  ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
    print('o ano:{} é bissexto'.format(ano))
else:
    print('o ano:{} não é bissexto'.format(ano))

