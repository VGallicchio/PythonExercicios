#28-Escreva um programa que faça o computador "Pensar" em um número int, entre 0 e 5 e peça para o 
#Usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na
#tela se o usuário venceu ou perdeu.

import random
numero = random.choice(0, 1 , 2 ,3 ,4 ,5)
num = int(input('Tente descobrir o numero inteiro escolhido pelo computador de 0 a 5'))
if num == numero:
print ('parabéns você ganhou')
else:
print('que pena você perdeu')

# rand int
from random import randint
numero = randint(0, 5)
num = int(input('Tente descobrir o numero inteiro escolhido pelo computador de 0 a 5'))
if num == numero:
    print ('parabéns você ganhou')
    else:
    print('que pena você perdeu')
    
