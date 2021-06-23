#faça um programa que calcule o preço da passagem cobrando R$0,50 por Km até 200Km e R$5,45 para viagens mais longas
viagem = float(input('qual a distancia da sua viagem?'))
ct1 = viagem * 0.50
if viagem<200:
    print('Você vai gastar:{}R$ na passagem'.format(ct1))
else:
    ct2 = viagem * 0.45
    print('Você vai gasta:{}R$ na passagem'.format(ct2))