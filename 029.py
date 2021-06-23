#faça um programa que leia a velocidade do carro e se ele ultrapassar a velocidade maxima de 80Km/h ele recebe uma multa
#de 7,00R$ por cada Km ultrapassado
km = float(input('qual a velocidade do carro?'))
multa = (km - 80) * 7
if km>80:
    print('Você recebeu uma multa de:{:.2f}R$,por excesso de velocidade'.format(multa))
else:
    print('esta dentro da velocidade maxima')

