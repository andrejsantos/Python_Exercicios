#escreva um codigo que leia nome, idade e sexo de 4 pessoas. no final do programa, mostre:
#a idade media do grupo
#qual o nome do homem mais velho
#quantas mulheres tem menos de 20
soma = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for c in range(1, 5):
    print('-'*10, '{}ª Pessoa'.format(c), '-'*10)
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]:')).strip()
    soma += idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade > 20:
        totmulher20 += 1
media = soma / 4
print('A média de idade do grupo  é de de {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo são tanta mulheres com menos de 20 anos'.format(totmulher20))
#NÃO CONSEGUI RESOLVER NADA, 100% COM AJUDA