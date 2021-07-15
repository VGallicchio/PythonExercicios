'''Ex 59 - Crie um programa que leia dois valores e mostre
um menu na tela:

1 - somar
2 - multiplicar
3 - maior
4 - novos numeros
5 - sair do programa

seu programa deverá realizar a op solicitada em cada caso'''

from time import sleep
n1 = float(input('Digite um número: '))
n2 = float(input('Digite um número: '))
c = 0
while c !=5:
    print('''
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair''')
    c = int(input('Digite a Operação: '))
    if c == 1:
        soma = n1+n2
        print('Resultado de {} + {} = {} '.format(n1, n2, soma))
    elif c == 2:
        mult = n1*n2
        print('Resultado de {} * {} = {}: '.format(n1, n2, mult))
    elif c == 3:
        if n1 < n2:
            maior = n2
        elif n1 > n2:
            maior = n1
            print('Entre {} e {} o maior numero é {}: '.format(n1, n2, maior))
        else:
            print('Os valores {} e {} são iguais'.format(n1, n2))
    elif c == 4:
        print('Informe os números novamente')
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite um número: '))
    elif c == 5:
        print('Finalizando ....')
    else:
        print('Opção inválida')
    print('=-='*10)
    sleep(2)
print('FIM DO PROGRAMA')
