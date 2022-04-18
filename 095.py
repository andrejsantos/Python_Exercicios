#Aprimore o desafio 93 para que ele funcione com vários jogadores,
#incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
time = list()
jogador = {}
part = list()
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do jogador:')).strip().title()
    total = int(input(f'Quantas partidas {jogador["Nome"]} jogou:'))
    part.clear()
    for c in range(total):
        part.append(int(input(f'Quantos gols {jogador["Nome"]} fez na partida {c+1}:')))
    jogador['gols'] = part[:]
    jogador['total'] = sum(part)
    time.append(jogador.copy())
    while True:
        res = str(input('Quer continualr? [S/N].')).upper()[0]
        if res in 'SN':
            break
        print('ERRO! responda apenas S ou N.')
    if res == 'N':
        break
print('-' * 45)
print('COD. ', end='')
for i in jogador.keys():
    print(f'{i:<14}', end='')
print('')
print('_' * 45)
for k, v in enumerate(time):
    print(f'({k}) ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print('')
print('-=' * 45)
while True:
    busca = int(input('Mostrar dados de qual jogador? (COD. de parada 999):'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO 404')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}:')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'No jogo {i+1} Fez {g} gols.')
    print('-=' * 45)
'''print(f'O jogador {jogador["Nome"]} jogou no total:{total} partidas')
for v, k in enumerate(jogador['gols']):
    print(f'=> Na partida {v+1} fez {k} gols.')
print(f'total de {jogador["total"]} gols')'''
