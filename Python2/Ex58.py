'''Ex 58 - Melhore o jogo do desafio 28 onde o computador
vai pensar em numero entre 0 e 10. Só que agora o jogador
vai tentar adivinhar até ele acertar, mostrando no final
quantos palpites foram necessários para vencer'''

#meu
from random import randint
jogador = int(input('Tente adivinhar o número de 0, 10 que a CPU pensou: '))
cpu = randint(0, 10)
tentativas = 1
print(cpu)

while jogador != cpu:
    print('Você errou Ternte novamente')
    jogador = int(input('Tente adivinhar novamente o numero: '))
    tentativas += 1
print('PARABÉNS você acertou com {} tentativas!!! '.format(tentativas))

#Meu com dicas
from random import randint
jogador = int(input('Tente adivinhar o número de 0, 10 que a CPU pensou: '))
cpu = randint(0, 10)
tentativas = 1
#print(cpu) teste vitoria.

while jogador != cpu:
    #print('Você errou Tente novamente')
    jogador = int(input('Tente adivinhar novamente o numero: '))
    tentativas += 1
    if jogador > 10:
        print('Chutou número maior que 10, tente entre 0 e 10: ')
    elif jogador < cpu:
        print('Errou tente um valor maior: ')
    else:
        print('Errou tente um valor menor: ') 
print('PARABÉNS você acertou com {} tentativas!!! '.format(tentativas))

#Curso em vídeo.

from random import randint
print('='*20)
print('TENTE ADIVINHAR QUE NUMERO A CPU PENSOU!!!')
print('='*20)
cpu = randint(0, 10)
tries = 0
a = False
print(cpu)#teste vitória.
while not a:
    jogador = int(input('Qual seu palpite de 0 a 10: '))
    tries += 1
    if jogador == cpu:
        a = True
    else:
        if jogador > 10:
            print('Chutou número maior que 10, tente entre 0 e 10: ') #linha que eu add para caso digitar valor que não seja entre 0 e 10.
        elif jogador < cpu:
            print('Errou tente um valor maior: ')
        else:
            print('Errou tente um valor menor: ') 
print('Acertou com {} tentativas'.format(tries))
