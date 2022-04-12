#faça um programa que leia 5 valores numericos e guarde-os em uma lista.
#no final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posiçoes na lista.
lista = list()
mai = 0
men = 0
for c in range(0, 5):
    lista.append(int(input('digite um numero:')))
    if c == 0:
        mai = men = lista[c]
    else:
        if lista[c] > mai:
            mai = lista[c]
        if lista[c] < men:
            men = lista[c]
print('-'*50)
print(f'você digitou a lista {lista}')
print(f'O maior numero foi: {mai} nas posições: ', end='')
for i, v in enumerate(lista):
    if v == mai:
        print(f'{i+1}...', end='')
print()#aqui serviu para aparecer certinho sem ser um na linha do outro
print(f'O menor numero foi: {men} nas posições: ', end='')
for i, v in enumerate(lista):
    if v == men:
        print(f'{i+1}...', end='')
print()#aqui serviu para aparecer certinho sem ser um na linha do outro
