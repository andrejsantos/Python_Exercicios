#desenvolva um programa que leia o primeiro termo e a razâo de uma PA no final mostre os 10 primeiros termos dessa progressâo
termo = int(input('Primeiro termo:'))
razao = int(input('Razão:'))
decimo = termo + (10 - 1) * razao
for c in range(termo, decimo + razao, razao):
    print(end='{}-'.format(c))
print(end='ACABOU')
#completado 90% sozinho 10% com ajuda
