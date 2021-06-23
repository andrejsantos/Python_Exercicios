#faça um programa que leia o nome de uma cidade e diga se ela começa com santos ou não
cidade = str(input('digite o nome de uma cidade:')).strip()
print(cidade[:5].upper().lower() =='Santo')