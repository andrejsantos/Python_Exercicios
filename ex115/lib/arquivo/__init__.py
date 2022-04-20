from Exercicios.ex115.lib.interface import *


def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('DEU RUIM! na criação do arquivo')
    else:
        print(f'Aquivo {nome} Criado')


def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO! na leitura do arquivo')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='<Desconhecido>', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('ERRO na abertura do arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('ERRO no salvamento de dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()

