#Crie um programa que simule um caixa etronico, perguntando o valor de saque
#e o programa vai informar quantas cédulas serão entregues de cada valor
#considere notas 50$ / 20$ / 10$ / 1$ no caixa.
print('='* 50)
print('CAIXA 24H')
print('='* 50)
valor = int(input('Que valor você quer sacar?'))
total = valor
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
print('SAQUE CONCLUIDO, VOLTE SEMPRE.')
#NÃO CONSEGUI FAZER. MAS ENTENDI O CONCEITO.