'''
Ex 88 Crie um programa que ajude o jogador da mega sena a criar palpites
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 numeros
Entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
'''
from random import randint
from time import sleep
lista = list()
jogos = list()
print('-='*30)
print('    Jogo da MEGA SENA'   )
print('-='*30)
quant = int(input('Quantos jogos vai sortear? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-='*3, f'<SORTEANDO {quant} JOGOS 1>', '-='*3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=' * 5, '<Boa Sorte!>', '-=' * 5)
z