'''46 - Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de
artificio, indo de 10 até 0, com uma pausa de 1 segundo entre eles'''

from time import sleep

for f in range(11, -1, -1):
    print('Contagem regressiva para o ano novo')
    print(f)
    sleep(1)
print('Feliz ano NOVO !!')
 