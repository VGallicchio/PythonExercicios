''' 70 - Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário
vai continuar no final.
No final mostre:
A - Total gasto na compra.
B - Quantos produtos custa mais de 1000 reais.
C - Qual é o nome do produto mais barato.
'''
#MEU
total = mmil = maior = menor = 0
while True:
    produto = str(input('Insira o produto: '))
    preco = float(input('Insira o preço: '))
    total += preco
    if preco > 1000:
        mmil += 1
    '''if preco > maior:
        preco = maior
    else:
        preco = menor''' #neste caso meu código ficou errado, pois tem de associar a string para o produto.
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja inserir outro produto ? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print('Total gasto na compra {} R$ '.format(total))
print('{} produtos custam mais de 1000 R$ '.format(mmil))
print('{} foi o produto mais barato  que custa {} R$'.format(produto, menor))


#CURSO EM VIDEO
total = mmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Insira o produto: ')).upper()
    preco = float(input('Insira o preço: '))
    cont += 1
    total += preco
    if preco > 1000:
        mmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja inserir outro produto ? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print('Total gasto na compra {:.2f} R$ '.format(total))
print('{} produtos custam mais de 1000 R$ '.format(mmil))
print('{} foi o produto mais barato que custa {:.2f} R$'.format(barato, menor))
