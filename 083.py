#crie um programa onde o usuario digite uma expressão qualquer que use parenteses.
#seu aplicativo deverá analisar a expressão passada está com os paranteses na ordem correta.
pares = str(input('Digite a expressão:'))
pilha = []
for simb in pares:
    if simb == '(':
        pilha.append(')')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('sua expressão está correta')
else:
    print('sua expressão está errada')
