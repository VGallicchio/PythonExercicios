'''Ex 62 - Melhore o desafio 61, perguntando para o usuario se 
ele quer mostrar mais alguns termos. O programa encerra quando
ele disse que quer mostrar 0 termos'''

#ANTIGO
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

#MELHORADO
from time import sleep
n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = 1
t = 0
m = 10
while m != 0:
    t = t + m
    while c < t:
        print('{}º Termo = {}'.format(c, n))
        n = n + r
        c += 1
        sleep(0.5)
    m = int(input('Quer mostar mais termos? Quantos? '))
print('FIM DO PROGRAMA')

'''O CONTADOR M VALENDO 10 FAZ COM QUE CALCULE OS 10 TERMOS DA PA PEDIDOS, EXEMPLO
NUMERO 10 COM RAZÃO 10, VAI PULAR DE 10 EM 10, ATÉ NO M=10, NO CASO, 10, 20.... ATÉ 100,
QUANDO FIZER ISSO ELE ENTRA NO WHILE C < T, ONDE T COMEÇA VALENDO ZERO. SAINDO DO LAÇO
O T ESTARIA VALENDO 100, FAZENDO 100 MAIS O NUMERO DE TERMOS SELECIONADOS. E SE REPETINDO
ATÉ SELECIONAR O ZERO'''
