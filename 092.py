#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
#Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
#Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime
cadastro = {}
cadastro['Nome'] = str(input('Nome:')).strip().title()
nas = int(input('Ano de Nascimento:'))
idade = datetime.now().year - nas
cadastro['Idade'] = idade
cadastro['Ctps'] = int(input('Carteira de trabalho (0 Não tem):'))
if cadastro['Ctps'] != 0:
    cadastro['Ano de Contratação'] = int(input('Ano de contratação:'))
    cadastro['Salario'] = float(input('Salário R$:'))
    cadastro['Aposentadoria'] = cadastro['Idade'] + (cadastro['Ano de Contratação'] + 35) - datetime.now().year
print('-=' * 35)
for k, v in cadastro.items():
    print(f'- {k} igual: {v}')
