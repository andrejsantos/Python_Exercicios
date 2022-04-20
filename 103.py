# Faça um programa que tenha uma função chamada ficha(),
# que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
def ficha(j, g):
    if j == '':
        j = '<desconhecido>'
    print(f'O jogador {j} fez {g} gol(s) no campeonato')


jogador = str(input("Nome do jogador:")).title()
Gols = str(input("Numero de gols:"))
if Gols.isnumeric():
    Gols = int()
else:
    Gols = 0
ficha(jogador, Gols)
