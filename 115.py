#criar um menu em Python, usando modularização
from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'curso.txt'

if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar Pessoa', 'Fechar programa'])
    if resp == 1:
        lerarquivo(arq)
    elif resp == 2:
        cabeçalho('Novo Cadastro')
        nome = str(input('Nome:'))
        idade = leiaint('Idade:')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        cabeçalho('Encerrando o programa...')
        break
    else:
        cabeçalho('\033[31mERRO! opção invalida\033[m')
    sleep(2)
