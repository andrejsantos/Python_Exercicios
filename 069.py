#Crie um programa que leia a idade e o sexo de varias pessoas.
#A cada pessoa cadastrada, o programa devera perguntar se o usuario quer continuar. No final mostre
#1) quantas pessoas tem mais de 18 anos.
#2)quantos homens foram cadastrados.
#3)quantas mulheres tem menos de 20 anos.
total = homen = mulher = 0
sexo = 'MF'
cont = 'SN'
while True:
    print('='*50)
    print('CADASTRE UMA PESSOA')
    print('=' * 50)
    idade = int(input('Idade:'))
    sexo = str(input(('Sexo [M/F]:'))).strip().upper()[0]
    print('-'*50)
    cont = str(input('Quer continuar [S/N]')).strip().upper()[0]
    print('-' * 50)
    if sexo == 'F':
        if idade <= 20:
            sexo = mulher
            mulher += 1
    elif sexo == 'M':
        sexo = homen
        homen += 1
    if idade >= 18:
        idade = total
        total += 1
    if cont == 'N':
        break
print('~'*50)
print('FIM DO PROGRAM ....')
print('~'*50)
print(f'Total de pessoas com mais de 18 anos: {total}')
print(f'Ao todo temos {homen} homens cadastrados.')
print(f'E temos {mulher} mulheres com menos de 20 anos.')
print('~'*50)

