#Crie um programa que leia varios numeros inteiros. Oprograma só vai parar com "999" e mostre quantos numeros foram digitados.
#e mostre a soma entre eles (desconsiderando o flag)
num = soma = cont = 0
while True:
    num = int(input('Digite um Número[999 para parar]:'))
    cont += 1
    if num == 999:
        break
    soma += num
print(f'A soma dos {cont} Valores foi {soma}!')
#FEITO 100% SOZINHO
