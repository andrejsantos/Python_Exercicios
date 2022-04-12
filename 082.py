#crie um programa que vai ler vários valores e colocar em uma lista.
#depois,crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados, respectivamente.
#ao final mostre o conteudo das tres listas geradas
lista = list()
impar = list()
par = list()
while True:
    lista.append(int(input('Digite um numero:')))
    resposta = str(input('Quer continuar? [S/N]')).strip().upper()
    if resposta == 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print('"'*50)
print(f'sua lista completa{lista}')
print(f'os numeros pares da sua lista são: {par}')
print(f'os numeros impares da sua lista são {impar}')
