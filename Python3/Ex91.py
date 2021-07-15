'''
Ex  91 faça um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado.
'''
from random import randint
from time import sleep
from operator import itemgetter
jogo ={'Jogador 1': randint(1, 6), #0 = jogador 1 = dado
       'Jogador 2': randint(1, 6),
       'Jogador 3': randint(1, 6),
       'Jogador 4': randint(1, 6)}
ranking = list()
for k, v in jogo.items():
    print(f'O dado do {k} caiu com {v}')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) #intemgetter(1) em bibliotecas não pode usar o sorted, então tem que por em uma lista e usar o item getter para fazer isso._
print('---'*20)
print('    =-Ranking Jogaadores-=')
for i, v in enumerate(ranking):
    print(f'   {i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)
