#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
aluno = {}
aluno['nome'] = str(input('Qual o nome do aluno:'))
aluno['media'] = float(input('Qual a media do aluno:'))
print('=-'*35)
print(f'O nome do aluno é: {aluno["nome"]}')
print(f'A media do alun é: {aluno["media"]}')
print('=-'*35)
if aluno['media'] >= 7.0:
    print('Aluno Aprovado!')
else:
    print('Aluno reprovado!')
