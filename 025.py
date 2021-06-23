#fazer um programa que diga se tem silva no nome
nome = str(input('digite um nome:')).strip()
busca = 'silva' in nome.lower()
print(busca)
