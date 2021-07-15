'''
Ex 87 Aprimore o desafio 86 mostrando no final:
A) Soma de todos os valores pares digitados.
B) Soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''

print('-='*30)
print('Construtor de Matriz Linhas e Colunas')
print('-='*30)
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))

print('-='*30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            spar += matriz[linha][coluna]
    print()
print('-='*30)
print(f'A soma de todos os valores pares digitados foi {spar}')
for linha in range(0, 3): #pega todas as linhas.
    scol += matriz[linha][2] #como a coluna declara é fixa é so declarar ela 0 coluna 1, 1 coluna 2, 2 coluna 3.
print(f'A soma dos valores da 3ª Coluna é {scol}')
for coluna in range(0, 3):
    if coluna == 0:
        mai = matriz[1][coluna]
    elif matriz[1][coluna] > mai:
        mai = matriz[1][coluna]
print(f'O maior valor da 2ª linha é {mai}')
