#23 - Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados

#ex: Digite um número: 1834
#Unidade: 4
#Dezena: 3
#Centena:8
#Milhar: 1

# dessa maneira não se usa condição com IF, que seria o ideal.

numero = int(input('Digite um numero de 0 a 9999'))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10 # jogada matemática para se obter somente a unidade representada
print('O numero digitado {} tem como'.format(numero))
print('Unidade {}'.format(numero[u]))
print('Dezena {}'.format(numero[d]))
print('Centena {}'.format(numero[c]))
print('Milhar {}'.format(numero[m]))
