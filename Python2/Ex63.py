'''Ex 63 - Escreva um programa que leia um numero n inteiro e
mostre na tela os n primeiros elementos de uma sequencia Fibonacci

Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8'''

#Curso em vídeo.
print('=-='*20)
print('Sequência de Fibonacci')
print('-'*30)

n = int(input('Quantos termos da sequeência? '))
t1 = 0 
t2 = 1

print('~'*30)
print('{} - {} - '.format(t1, t2), end= '')
c = 3
while c <= n:
    t3 = t1 + t2
    print('{} - '.format(t3), end= '')
    t1 = t2
    t2 = t3
    c += 1
print('FIM')

#outra
print('=='*11)
print('SEQUÊNCIA DE FIBONACCI')
print('=='*11)
n = int(input('Quantos elementos você quer ver? '))
c = 0
d = 1
a = 0
if n % 2 == 0:
    while a != n:
        print(c, d, end=' ')
        c = c + d
        d = d + c
        a += 2
if n % 2 != 0:
    while a != (n+1):
        print(c, '' if a == (n -1) else d, end=' ')
        c = c + d
        d = d + c
        a += 2
print('Fim')