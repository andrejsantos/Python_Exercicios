#faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". caso contrario peça que digite de novo.
sexo = str(input('Informe seu sexo[M/F]:')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. Informe seu sexo:'))
print('Sexo {} registrado com sucesso'.format(sexo))
#Feito somente com ajuda.(fracassado)
