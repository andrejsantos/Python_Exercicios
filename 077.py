#crie um programa que tenha uma tupla com varias palavras (não usar acentos).
#depois mostrar, para cada palavra, quais são as suas vogais.
palavras = ('andre', 'leonardo', 'python',
            'pokemon', 'codigo', 'palavras', 'game')
for c in palavras:
    print(f'\nNa palavra \033[36m{c.upper().strip()}\033[m temos as vogais:', end=' ')
    for letra in c:
        if letra.upper() in 'AEIOU':
            print(letra, end=', ')
