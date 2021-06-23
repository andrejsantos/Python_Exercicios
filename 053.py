# faça um programa que leia uma frase e diga se ela é palindromo
frase = str(input('digite uma frase:')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso =''
for c in range(len(junto) -1, - 1, -1):
    inverso += junto [c]
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('A frase não é um palíndromo')
#não soube fazer nada