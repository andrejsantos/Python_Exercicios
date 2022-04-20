#Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
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


def leiar(msg2):
    while True:
        try:
            n = float(input(msg2))
        except (TypeError, ValueError):
            print('ERRO! o valor Real está invalido')
            continue
        except KeyboardInterrupt:
            print('Usuario preferiu não digitar esse número.')
        else:
            return n


ni = leiaint('Digite um número inteiro:')
nr = leiar('Digite um numero real:')
print(f'O numero inteiro digitado é: {ni} o real é {nr}')
