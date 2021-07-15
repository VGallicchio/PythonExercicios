'''52 - Faça um programa que um num int e diga se ele é ou não número primo.'''

num = int(input('Digitei um numero para verificar se é numero primo: '))
mult = 0

for c in range (1, num + 1):
    if (n % c == 0):
    print('Multiplo de {}'.format(c))
    mult += 1
    if mult == 0):
        print('Numero Primo')
    else:
        print('Tem {} multiplos acima de 2 de {} '.format(mult, num))

###

num = int(input('Digite um numero: '))
tot = 0
for c in range(1, num +1)
    if num % c == 0:
        print('\33[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end='')
print('Numero {} foi divisivel {} veze '.format(num, tot)) #Fim do laço.
if tot == 2:
    print('E por isso ele é PRIMO')
else:
    print('E por isso ele não é primo')
