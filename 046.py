#fazer um programa que faça uma contagem regrasiva de 10 até 0 com uma pausa de 1 segundo entre eles
from time import sleep
print('\033[1;36mFALTAM 10 SEGUNDOS PARA O ANO NOVO!\033[m')
for c in range(10, 0, -1):
    sleep(1)
    print(c)
sleep(1)
print('\033[1;33mFOGOS ESTOURANDO!\033[m')
