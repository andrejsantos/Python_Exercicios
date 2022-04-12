#crie um programa que leia varios numeros inteiros. O programa só vai parar digitando "999", que é a condição de parada.
#no final mostre quantos numeros foram digitados e  qual a soma entre eles.
num = cont = soma = 0
num = int(input('Digite um numero [999 para parar]:'))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um numero [999 para parar]'))
print('você digitou {} e a soma entre eles são {}'.format(cont, soma))
