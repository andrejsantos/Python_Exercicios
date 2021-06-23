#faça um programa que leia 3 numeros e fala qual deles é o maior e qual é o menor
n1 = int(input("digite um numero:"))
n2 = int(input("digite outro número:"))
n3 = int(input("dihite mais um numero:"))
#maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
#menor
    menor = n1
if n2 < n1 and n2 < n3:
        menor = n2
if n3 < n1 and n3 < n2:
        menor = n3
print('esse é o menor numero:{}'.format(menor))
print('esse é o maior numero:{}'.format(maior))

