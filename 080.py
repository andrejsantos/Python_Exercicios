#crie um programa onde usuarios possa digitar cinco valores numericos e cadastre-os em uma lista,
# já na posição correta de inserção correta(sem usar o sort()).
#nofinal, mostre a lista ordenada na tela.
lista = list()
for c in range(0, 5):
    numero = int(input('digite um numero:'))
    if c == 0:
        lista.append(numero)
        print(f'adicionado na posição {c}')
    elif numero > lista[len(lista)-1]:
        lista.append(numero)
        print(f'adicionado na ultima posição.')
    else:
        posi = 0
        while posi < len(lista):
            if numero <= lista[posi]:
                lista.insert(posi, numero)
                print(f'adicionado na posição {posi}')
                break
            posi += 1
print(f'numeros adicionados a lista{lista}')
