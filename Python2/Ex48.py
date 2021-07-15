'''48 - Faça um programa que Calcule a soma de todos os numeros impares que são multiplos
de três e que se encontram no intervalo de 1 até 500.'''

soma = 0
cont = 0
for n in range(1, 501, 2):
    if (n % 3) == 0:
        cont += 1
        s += n
    print ('A soma dos Numeros impares multiplos de 3 de 1 a 500 {} é {}'.format(cont, s))
print('FIM')