#fazer um programa que leia um angulo qualquer e mostre o seno, cosseno e tanjente
import math
ângulo = int(input('digite o ângulo:'))
sen = math .sin(math.radians(ângulo))
cos = math .cos(math .radians(ângulo))
tg = math .tan(math .radians(ângulo))
print('o ângulo de{} temseno:{:.2f}, cosseno{:.2f} e a tanjente:{:.2f}'.format(ângulo, sen, cos, tg ))