'''Ex 61 - Refaça o desafio 51, lendo o primeiro termo e a razao
de uma PA, mostrando os 10 primeiros termos da progressao usando
While'''

from time import sleep
n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = 1
while c <= 10:
    print('{}º Termo = {}'.format(c, n))
    n = n + r
    c += 1
    sleep(1)
print('FIM')
