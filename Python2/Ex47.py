'''47 - Faça um programa que mostre na tela Todos os números pares que estão entre 1 e 50'''

'''for f in range(1, 50, 2)
    print('Números pares ente 1 e 50')
print('FIM')'''
    
for n in range(1, 51):
    if (n % 2) == 0:
    print('Números pares ente 1 e 50')
    print(n)
print('FIM')

#Com laço 2:
for n in range(2, 51, 2):
    print(n, end=' ')
print('Numeros pares de 1 a 50')
