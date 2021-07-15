'''73 - Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato, na ordem de colocação,
depois mostre:
a) apenas os 5 primeiros colocados.
b) os ultimos 4 colocados da tabela.
c) uma lista com os times em ordem alfabetica
d) em que posição na tabela está o time da chapecoense.
'''
#Meu código.
from time import sleep
import os
times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 
'Atlético MG', 'Botafogo', 'Athetlico PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport', 'Vitória', 'Coritiba', 'Avai', 
'Ponte Preta', 'Atlético GO')

while True:
    op = int(input('''
    [1] - Mostrar 5 primeiros colocados:
    [2] - Mostrar Rebaixados:
    [3] - Mostrar Times em ordem alfabética.
    [4] - Mostrar Colocação Chapecoense:
    [5] - Mostrar tabela de classificação:
    [6] - Sair
    Insira a opção: '''))
    #os.system('clear')
    sleep(1)
    if op == 1:
        print('Cinco primeiros colocados:')
        for time in range (0, 5):
            print('{}º {}'.format(time + 1, times[time]))
    elif op == 2:
        print('Rebaixados:')
        for time in range (16, 20):
            print('{}º {}'.format(time +1, times[time]))
    elif op == 3:
        print('Times em ordem alfabética:')
        for time in sorted(times):
            print({time})
    elif op == 4:
        print('Chapecoense está na {}ª Colocação'.format(times.index('Chapecoense')))
    elif op == 5:
        print('Posição      Clube')
        for time in range (0, 20):
            print('{}º     {}'.format(time +1, times[time]))
    elif op == 6:
        break
    else:
        print('Opção inválida digite novamente: ')
print('FIM')

#Curso em vídeo
times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 
'Atlético MG', 'Botafogo', 'Athetlico PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport', 'Vitória', 'Coritiba', 'Avai', 
'Ponte Preta', 'Atlético GO')
print('-=' *15)
print(f'Lista de times do Brasileirão: {times}')
print('-=' *15)
print(f'Os 5 primeiros times são {times[0:5]}')
print('-=' *15)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' *15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' *15)
print(f'O time da Chapecoense está na {times.index("Chapecoense")+1}ª posição')