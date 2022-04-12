# JOGO DA MEGA SENA
from random import randint
L1 = list()
jogos = list()
print('*'*50)
print("JOGO DA MEGA SENA")
print('*'*50)
qnt = int(input("Quantos jogos deseja sortear?"))
T = 1
while T <= qnt:
    C = 0
    while True:
        num = randint(1, 60)
        if num not in L1:
            L1.append(num)
            C += 1
        if C >= 6:
            break
    L1.sort()
    jogos.append(L1[:])
    L1.clear()
    T += 1
print('=-' * 50)
print(f"{qnt}:JOGOS SORTEADOS")
print('-='*50)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
print('BOA SORTE!')
