#desenvolva um programa que leia quatro valores pelo teclado e gurde-os em uma tupla. no final,mostre:
#A) quantas vezes apareceu o valor 9.
#B) em que posição foi digitado o primeiro valor 3.
#C) quais foram os números pares.

num = (int(input(('Digite um número:'))),
       int(input(('Digite outro número:'))),
       int(input(('Digite outro número:'))),
       int(input(('Digite outro número:'))))
print(f'O valor 9 apareceu {num.count(9)} vez')
if 3 in num:
       print(f'O valor 3 apareceu na {num.index(3)+1}° posição')
else:
       print('O numero 3 não foi digitado em nenhuma posição')
print('Os valores pares são:', end='')
for n in num:
       if n % 2 == 0:
              print(n, end=' ')
