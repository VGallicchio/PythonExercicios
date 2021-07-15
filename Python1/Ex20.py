#20-O mesmo prof quer sortear a ordem de apresentação. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
n1 = str(input('Primeiro Aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4] #Array com os valores para serem randomizados.

ordem = random.shuffle(lista) #Randomiza e embaralha a lista de valores armanezados nas arrays.
print('A ordem de apresentação será {}'.format(ordem))

# from random import suffle - utilizar somente choice. suffle(lista).
