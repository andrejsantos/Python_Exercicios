#melhore o (desafio 61, perguntando para o usuario se ele quer mostra mais alguns termos.
#o programa encerra quando ele disser 0 termos
primero = int(input('Primero termo:'))
razao = int(input('Razão da PA'))
termo = primero
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print('{} - '.format(termo), end='')
        termo += razao
        c += 1
    print('PAUSA')
    mais = int(input('Qunatos termos você quer mostrar a mais ?'))
print('FIM')
#CONCULIDO 20% SOZINHO
