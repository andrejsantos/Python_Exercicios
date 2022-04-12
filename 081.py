#crie um programa que vai ler vários números e colocar em uma lista.,
#depois disso mostre:
#A)quantos números foram digitados.
#B)A lista de valores de forma ordenada(decrescente).
#C)se o valor 5 foi digitado e está ou não na lista.
lista = list()
while True:
    lista.append(int(input('digite um numero:')))
    res = str(input('que continuar? [S/N]:')).strip().upper()
    if res == 'N':
        break
print('=-'*50)
print(f'você fez uma lista de {len(lista)} numeros')
if 5 in lista:
    print(f'O numero 5 foi adicionado na {lista.index(5)+1}° posição')
else:
    print('o numero 5 não foi adicionado a essa lista')
lista.sort(reverse=True)
print(f'A lista em forma decrecente fica', end=' ')
print(lista)
