#crie um programa onde o usuario possa digitar varios valores númericos e cadastre-os em uma lista.
#caso o número já exista lá desntro, ele não será adicionado.
# no final serão exibidos todos os valores únicos digitados, em ordem crescente.
lista = list()
resp = 'S'
while resp in 'Ss':
    num = (int(input('digite um valor:')))
    if num not in lista:
        lista.append(num)
    else:
        print('esse numero já está na lista')
    resp = str(input('deseja continuar? [S/N]:')).strip().upper()
lista.sort(), #esse tem que ser depois do comendo de repetição se não ele não reconhece.
print(f'Os numeros adicionados a lista foram: {lista}')
