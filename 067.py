#Faça um programa que mostre a tabuada de varios numeros, um de cada vez, para cada valor digitado pelo usuario.
#o programa será interrompido quando o numero solicitado for negativo.
num = 0
while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num < 0:
        break
    print('='*50)
    for cont in range(1, 11):#PODEMOS COLOCAR "FOR" DENTRO DE WHILE
        print(f'{cont} x {num} = {num*cont}')
    print('=' * 50)
print('Fim do programa. volte sempre!')
