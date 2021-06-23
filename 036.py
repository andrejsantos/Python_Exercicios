#escreva um programa para aprovar o emprestimo bancario para uma compra de uma casa
#perguntando o VALOR DA CASA, SALARIO, e QUANTOS ANOS VAI PAGAR
#calcule o valor da prestação mensal sabendo que ela não pode exeder 30% do salario ou o emprestimo sera negado
casa = float(input('qual o valor da casa?'))
salario = float(input('qual o seu salario?'))
anos = int(input('em quntos anos pretende pagar?'))
mensalidade = casa / (anos * 12)
gasto = salario * 30 / 100
print('uma casa de:\033[1;32m{:.2f}, que sera paga em {} anos\033[m'.format(casa, anos))
print('fica com a prestação de:\033[1;36m{:.2f} por mês\033[m'.format(mensalidade))
if mensalidade <= gasto:
    print('\033[1;35mparabéns!,você foi aprovado\033[m')
else:
    print('\033[4;31minfelizmente você não foi aprovado\033[m')
