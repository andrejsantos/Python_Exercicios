#Crie um programa onde o usuário possa digitar sete valores numéricos e
# cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final,
# mostre os valores pares e ímpares em ordem crescente.
num = [[], []]
for n in range(1, 8):
    numero = (int(input(f'Digite o {n}° numero:')))
    if numero % 2 == 0:
        num[0].append(numero)
    else:
        num[1].append(numero)
print('='*50)
num[0].sort()
num[1].sort()
print(f'Os numeros pares foram: {num[0]}')
print(f'Os numeros impares foram: {num[1]}')
