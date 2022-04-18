# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def terreno(larg, comp):
    t = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {t:.1f}m²')


print('controle do terreno')
print('=-' * 35)
l = float(input('LARGURA:'))
c = float(input('COMPRIMENTO:'))
terreno(l, c)
