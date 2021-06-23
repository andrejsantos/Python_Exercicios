#faça um programa que leia uma frase e conte quantas vezes aparece a letra 'A'
#em que posição ela aparece pela primeira vez
#em que posição ela aparece pela ultima vez
frase = str(input('digite uma frase:')).upper().strip()
a1 = frase.count('A')
a2 = frase.find('A')+1
a3 = frase.rfind('A')
print('quantas vezes aparece a letra a:{}\nem que posição ela aparece primeiro:{}\nem que posição ela aparece por ultimo:{}'.format(a1, a2, a3))
