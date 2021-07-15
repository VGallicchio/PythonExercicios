'''
76 - Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos valores na sequência
No final, mostre uma listagem de preços organizando os dados em forma tubular.
'''
#Curso em vídeo
produtos = ('Arroz', 15.90, 'Extrato de Tomate', 0.89, 'Óleo de Soja', 1.25)
print(produtos)
print('-'*40)
print(f'{"Listagem de Produtos e Preços":^40}')
print('-'*40)
for pos in range (len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R${produtos[pos]:>7.2f}')
print('-'*40)
