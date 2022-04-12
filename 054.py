#crie um programa que leia o ano de nacimento de 7 pessoas e diaga quem atingiram a maior idade(21 anos) e quantos já são de maiores
import datetime
atual = datetime.date.today().year
totmaior = 0
totmenor = 0
for c in range(1, 8):
    data = int(input('olá,informe o ano de nacimento da {}ª pessoa:'.format(c)))
    idade = atual - data
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('total de pessoas maiores de idade foram:{}'.format(totmaior))
print('total de pessoas menores de idade foram:{}'.format(totmenor))
