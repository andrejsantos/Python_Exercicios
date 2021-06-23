#faça um programa que leia o nome de uma pessoa mostrando seu primeiro  e ultimo
nome = str(input('digite um nome:')).strip()
separação = nome.split()
a1 = separação[0]
a2 = separação[len(separação)-1]
print('nome completo:{}\nprimeiro nome:{}\nultimo nome:{}\n'.format(nome, a1, a2))
