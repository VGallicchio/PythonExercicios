''' 68 - Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador Perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''
#Meu código
from random import randint
from time import sleep
print('==='*20)
print('VAMOS JOGAR PAR OU IMPAR QUERO VER VENCER O COMPUTADOR')
print('==='*20)
r = 0
v = 0

while True:
    jogador = int(input('Escolha um valor: '))
    escolha = str(input('PAR ou IMPAR ? ')).upper().strip()[0:5]
    CPU = randint(1, 10)
    print('O compútador jogou {} '.format(CPU))
    if escolha == 'IMPAR':
        escolhacpu = 'PAR'
    else:
        escolhacpu = 'IMPAR'
    print('O compútador escolheu {} '.format(escolhacpu))
    print('==='*20)
    r = jogador + CPU
    print('Você jogou {} o computador jogou {}, o total foi {} '.format(jogador, CPU, r), end = '')
    if r % 2 == 0:
        r = 'PAR'
    else:
        r = 'IMPAR'
    print('DEU {} o jogador escolheu {} e a CPU escolheu {} '.format(r, escolha, escolhacpu))
    sleep(1)
    if escolha == r:
        print('O jogador venceu')
        v += 1
    else:
        print('A CPU venceu')
        break
        sleep(3)
sleep(2)
print('GAME OVER você venceu {} vezes'.format(v))    

#Curso em video
from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end= ' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
            else:
                print('Você PERDEU!')
                break
        elif tipo == 'I':
            if total % 2 == 1:
                print('Você VENCEU!')
                v += 1
            else:
                print('Você PERDEU')
                break
        print('VAMOS jogar novamente...')
 print(f'GAME OVER! você venceu {v} vezes. ')
 