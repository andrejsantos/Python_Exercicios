#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.
temp = []
pessoas = list()
maior = menor = 0
while True:
    temp.append(str(input('Nome:')))
    temp.append(float(input('peso:')))
    if len(pessoas) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    pessoas.append(temp[:])
    temp.clear()
    resp = str(input('quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print(f'Osdados foram {pessoas}')
print(f'Ao todo, Você cadastrou {len(pessoas)} pessoas')
print(f'Omaior peso foi de {maior}Kg. Peso de', end=' ')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')
print()
print(f'O menor peso foi {menor}Kg. Peso de', end=' ')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]}', end=' ')
