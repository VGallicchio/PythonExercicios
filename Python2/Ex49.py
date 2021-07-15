'''49 - Refaça o Desafio 09, mostrando a tabuada de um numero que o usuário escolher,
só que agora faça com laço for.'''

#programa que leia um valor int e moestre sua taboada

n = int(input('Digite um numero para saber sua tabuada'))
for tab in range(1, 11):
    res = n*tab 
    print(' {} x {} = {} '.format(n, tab, res))
print('Fim'.exit())

n = int(input('Digite um numero para saber sua tabuada'))
for tab in range(1, 11):
    print('{} x {:2} = {} '.format(n, tab, n*tab))
print('Fim'.exit())
