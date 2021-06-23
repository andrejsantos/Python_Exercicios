#escreva um programa que calcule o valor pago em um produto considerando o seu preço normal e condição de pagamento
#a vista ou cheque 10% de desconto
#a vista no cartão 5% de desconto
#em 2x no cartão preço normal
#3x ou mais 20% de juros
print('{:=^100}'.format('\033[4;33m LOJA DO MESTRE ANDRÉ \033[m'))
produto = int(input('qual o valor do produto?'))
print('''escolha a forma de pagamento...
(1)dinheiro ou cheque
(2)cartão a vista
(3)2x no cartão
(4)3x ou mais no cartão''')
pagamento = int(input('qual a forma de pagamento:'))
if pagamento == 1:
    ct1 = 10 / 100 * produto
    dinheiro1 = produto - ct1
    print('o valor do produto terá 10% de desconto:{}R$'.format(dinheiro1))
elif pagamento == 2:
    ct2 = 5 / 100 * produto
    cartão2 = produto - ct2
    print('sua compra a vista no cartão tem 5% de desconto:{}R$'.format(cartão2))
elif pagamento == 3:
    cartão3 = produto / 2
    print('o produto em duas vezes fica com o preço normal, parcelado fica{}'.format(cartão3))
elif pagamento == 4:
    xxxx = 20 / 100 * produto
    juros = produto + xxxx
    parcelas = int(input('vão ser em quantas parcelas?'))
    parcelamento = juros / parcelas
    print('sua compra de {:.1f}R$ será parcelada em {}x de {:.1f}R$ com JUROS.'.format(produto, parcelas, parcelamento))
    print('o valor completo com juros de 20% fica:{:.1f}R$'.format(juros))
else:
    print('não foi escolhido nenhuma das opções')