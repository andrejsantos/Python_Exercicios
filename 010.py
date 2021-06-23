# digite o valor que esta na sua carteita que eu te falo quantos dolar você pode comprar,ps valor do dolar nesse momento 5,24
a = float(input('\033[36mquanto que você tem na carteira? R$\033[m'))
n1 = a / 5.24
print('quanto você tem:{:.2f}R$\nquantos dolar da para comprar:\033[1;31m{:.2f}U$\033[m'.format(a, n1))
