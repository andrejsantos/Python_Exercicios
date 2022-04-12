#crie um programa que tenha uma tupla unica com nomes de produtos e seus respectivos preços, na sequencia.
#no final, mostre uma listagem de preços, organizando os dados em forma tabular.
mercadoria = ('lápis', 1.75,
              'Borracha', 2.00,
              'Caderno', 15.90,
              'Estojo', 25.00,
              'Tranferidor', 4.20,
              'Compasso', 9.99,
              'Mochilas', 120.32,
              'Canetas', 22.30,
              'Livros', 34.90)
print('-'*50)
print(f'{"LISTA DE COMPRAS":^50}')
print('-'*50)
for lista in range(0, len(mercadoria)):
    if lista % 2 == 0:
        print(f'{mercadoria[lista]:.<30}', end=' ')
    else:
        print(f'R$:{mercadoria[lista]:>3.2f}')
print('-'*50)
