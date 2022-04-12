#crie um programa que leia varios numeros inteiros. no final mostre a media entre eles e qual foi o maior e o menor valores lidos
#o programa deve perguntar se quer ou não continuar.
soma = quant = média = menor = maior = 0
r = 'S'
while r in 'Ss':
    num = int(input('Digite um numero:'))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    r = str(input('Quer continuar? [S/N] ')).upper() .strip()
média = soma / quant
print('Você digitou {} números e a média foi {} o maior valor foi {} e o menor valor {}'.format(quant, média, maior, menor))
