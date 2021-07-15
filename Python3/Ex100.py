'''
Ex 100 - Faça um programa que tenha lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocálos dentro da lista e a segunda função vai mostrar
a soma entre todos os valores PARES sorteados pela função anterior.
'''
from random import randint
from time import sleep
def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}, ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


numeros = list()
sorteia(numeros)
somapar(numeros)