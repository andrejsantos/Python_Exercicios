# crie um programa que leia o nome de uma pessoa completo e mostre
# 1/2:o nome com todas as letras maiusculas , o nome com todas as letras minusculas
# 3:quantas lestras ao todo sem considerar os espaços
# 4:quantas letras tem o primeiro nome
nome = str(input('digite um nome:')).strip()
print('tudo em maiusculo',nome.upper())
print('tudo em minusculo:',nome.lower())
print('qunatas letras tem:{}'.format(len(nome) - nome.count(' ')))
dividido =nome.split()
print('o primeiro nome é:{}, e ele tem:{} letras'.format(dividido[0], len(dividido[0])))
