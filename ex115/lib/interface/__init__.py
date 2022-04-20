
def leiaint(msg1):
    while True:
        try:
            n = int(input(msg1))
        except (TypeError, ValueError):
            print('ERRO! o valor inteiro que você digitou é invalido')
            continue
        except KeyboardInterrupt:
            print('Usuario preferiu não digitar esse número.')
        else:
            return n


def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaint('Sua opção:')
    return opc
