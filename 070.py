#Crie um programa que leia o nome e preço de varios produtos. perguntando se quer continuar
#mostre no final
#1)qual é o total gasto na compra.
#2)quantos produtos custam mais de 1000$.
#3)qual é o nome do produto mais barato.
total = barato = cont = caro = 0
nomeb = ''
print('LOJA')
while True:
    nome = str(input('Nome do produro:'))
    valor = float(input('preço do produto:'))
    cont += 1
    con = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    total = valor + total
    if valor > 1000:
        caro += 1
    if cont == 1 or valor < barato:
        barato = valor
        nomeb = nome
    if con == 'N':
        break
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {caro} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomeb} que custa R${barato}')
#concluido com 20% de ajuda.
