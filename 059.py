# escreva um codigo que leia dois valores diferentes e mostre um menu na tela:
# 1=somar. 2=multiplicar. 3=maior. 4=novos numeros. 5=fechar programa
from time import sleep
fechar = 0
num1 = int(input('primeiro valor:'))
num2 = int(input('segundo valor:'))
while fechar != 5:
    print('=-' * 10)
    print('[1] somar')
    print('[2] multiplicar')
    print('[3] maior')
    print('[4] novos numeros')
    print('[5] sair.')
    print('=-'*10)
    escolha = int(input('O que deseja fazer?'))
    if escolha == 1:
        soma = num1 + num2
        print('A soma entre {} + {} = {}'.format(num1, num2, soma))
    elif escolha == 2:
        multi = num1 * num2
        print('A multiplicação entre {} * {} = {}'.format(num1, num2, multi))
    elif escolha == 3:
        if num1 > num2:
            print('O maior numero escolido é: {}'.format(num1))
        elif num2 > num1:
            print('O maior numero escolido é: {}'.format(num2))
        else:
            print('Não tem numero maior.')
    elif escolha == 4:
        print('Informe novamente os numeros:')
        num1 = int(input('primeiro valor:'))
        num2 = int(input('segundo valor:'))
    elif escolha == 5:
        fechar = 5
        print('fechando programa.....')
    else:
        print('Opção invalida. Tente novamente.')
        sleep(1)
print('Fim do programa! volte sempre!')
#feito 100% sozinho !!!!!!!!!!!