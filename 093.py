#Crie um programa que gerencie o aproveitamento de um jogador de futebol.
#O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
#No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
jogador = {}
part = list()
jogador['Nome'] = str(input('Nome do jogador:')).strip().title()
total = int(input(f'Quantas partidas {jogador["Nome"]} jogou:'))
for c in range(total):
    part.append(int(input(f'Quantos gols {jogador["Nome"]} fez na partida {c+1}:')))
jogador['gols'] = part[:]
jogador['total'] = sum(part)
print('-=' * 35)
print(jogador)
print('-=' * 35)
for v, k in jogador.items():
    print(f'O campo {v} tem o valor {k}')
print('-=' * 35)
print(f'O jogador {jogador["Nome"]} jogou no total:{total} partidas')
for v, k in enumerate(jogador['gols']):
    print(f'=> Na partida {v+1} fez {k} gols.')
print(f'total de {jogador["total"]} gols')
