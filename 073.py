#crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato braisileiro de futebol,
#na ordem de colocação. depois mostre
#A) apenas os 5 primeiros colocados.
#B)os ultimos 4 colocados da tabela.
#C)uma lista com os times em ordem alfabetica.
#D)em que posição na tabela está o time chapecoense.
lista = ('Palmeiras', 'Santos', 'Vasco da Gama', 'Grêmio',
         'Flamengo', 'Corinthians', 'Internacional', 'Cruzeiro',
         'São Paulo', 'Atlecico Minero', 'Botafogo','Fluminense',
         'Coritiba', 'Bhaia', 'Goiás', 'Guarani', 'Sport', 'Portuguesa',
         'Atlético Paranaense', 'Vitória')
print(f'Os 5 primeiros são:{lista[:5]}')
print('=+'*40)
print(f'Os 4 últimos são: {lista[-4:]}')
print('=+'*40)
print(f'times em ordem alfabeticas: {sorted(lista)}')
print('=+'*40)
print(f'O Cruzeiro está na {lista.index("Cruzeiro")+1}° posição')
