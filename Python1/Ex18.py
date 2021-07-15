#18-Programa que leia um angulo e mostre na tela o valor do sen, cons e tang.

import math
angulo = float(input('Digite o ângulo desejado: '))
seno = math.sin(math.radians(angulo)) #Para funcionar bibli, do calculo de sen, é preciso pegar o radiano (radians)
print('O angulo de {} tem Seno de {:.2f} '.format(angulo, seno))
coseno = math.cos(math.radians(angulo))
print('O angulo de {} tem Coseno de {:.2f} '.format(angulo, coseno))
tangente = math.tan(math.radians(angulo))
print('O angulo de {} tem Tangente de {:.2f} '.format(angulo, tangente))

# from math import radiance, cos, sin, tan