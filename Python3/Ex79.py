'''Ex 79 Crie um programa onde o usuário possa digitar vários valoers
números e cadastre-os em uma lista. Caso o número já exista lá dentro, ele 
não será adicionado. No final, serão exibidos todos os valores únicos
digitados, em ordem crescente.
'''
print('\33c')
print('\33[1;34m-\33[1;33m'*40)
print(f'\33[1;32m{":":<0}\33[m\33[1;32m{"CADRASTROS NUMÈRICOS":^38}\33[m\33[1;32m{":":>0}\33[m')
print('\33[1;34m-\33[m'*40)
valor = []
while True:
    n = int(input('Digite O valor: '))
    valor.sort()
    if n not in valor:
        valor.append(n)
    else:
        print('Valor duplicado! não adicionado...')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja inserir outro número? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print('-'*40)
print(f' Valores da lista em ordem crescente: ')
print('-'*40)
print(valor)

#Curso em vídeo:
numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('-=' * 30)
numeros.sort()
print(f'Você digitou os valores {numeros}')
