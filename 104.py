def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO. digite um numero!')
        if ok:
            break
    return valor


#programa principal
n = leiaint('Digite um numero:')
print(f'Você acabou de digitar o número: {n}')
