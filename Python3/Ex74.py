'''74 - Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor, que estão na tupla
'''
#rever

from random import randint
t = tuple(randint(0, 10) for i in range(0, 5))
print(f'Os números gerados foram {t}', end='')
print(f'\nO maior valor sorteado foi {max(t)}')
print(f'O menor valor sorteado foi {min(t)}')


#Curso em video
from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end='')
for n in numeros:
	print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')

''' O max e o min servem para tuplas, listas entre outros
pra pegar valor maximo e minimo dentro da array.

Na minha solução utilizei o comando de usar uma tupla e dentro dela randomizar
e o for colocou de 0 a 5
'''