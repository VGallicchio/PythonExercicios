#16-Programa que leia um numero real e mostre na tela a sua porção inteira / Ex: 6.127 parte inteira 6

#Neste importamos a biblioteca math para utilizar o comando trunc.

import math
num = float(input('digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, math.trunc(num)))

#Podemos tambem importar apenas a funcionalidade necessária para o códico da biblioteca, como por exemplo:

from math import trunc
num = float(input('digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))

#Abaixo temos um exemplo da resolução sem importar a biblioteca math. o int(num) faz com que o numero seja
#ajustado para a sua porção inteira.

num = float(input('digite um valor: '))
print('o valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))