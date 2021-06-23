#faça im programa que pergunte o salario do funcionario e calcule o valor do seu almento
#para salario superiores a 1.250.00R$ calcile um aumento de 10%
#para os inferiores ou iguais o aumento é de 15%
salario = float(input('digite seu salario! R$:'))
if salario > 1250 :
    ct1 = (10 / 100) * salario + salario
    print('seu salario é de :{:.2f}R$ com o aumento de 10% ficou:{:.2f}R$'.format(salario, ct1))
else:
    ct2 = (15 / 100) * salario + salario
    print('seu salario é de :{:.2f}R$ com o aumento de 15% ficou:{:.2f}R$'.format(salario, ct2))