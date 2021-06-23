#crie um programa que leia duas notas de um aluno e caulcule sua media final
nota1 = float(input('NOTA DO ALUNO:'))
nota2 = float(input('NOTA DO ALUNO:'))
media = (nota1 + nota2) / 2
print('sua nota foi:\033[4;32m{:.1f}\033[m'.format(media))
if media < 5.0:
    print('\033[1;31mvocê foi reprovado\033[m')
elif media > 7.0:
    print('\033[1;36mPARABENS VOCÊ FOI APROVADO\033[m')
else:
    print('\033[1;33mvocê está de recuperação\033[m')