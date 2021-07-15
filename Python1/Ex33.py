#33-Faça um programa que leia três números e diga qual é o maior e o menor.

n1 = int(input('Digite o numero inteiro 1'))
n2 = int(input('Digite o numero inteiro 2'))
n3 = int(input('Digite o numero inteiro 3'))
#verificando o menor
menor = n1
if n2 < n1 and n2 < n3:
menor = n2
if n3 < n1 and n3 < n2:
menor = n3
#verificando o maior
maior = a
if n2 > n1 and n2 > n3:
maior = n2
if n3 > n1 and n3 > n2:
maior = n3
print('O menor valor é {} '.format(menor))
print('O maior valor é {} '.format(maior))
