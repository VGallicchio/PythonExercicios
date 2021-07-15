'''Ex 60 - Faça um programa que leia um numero e mostre o seu
fatorial exemplo: 5! = 5x4x3x2x1 = 120'''

'''O calculo está certo, porém eu fiz incrementando até o valor para calcular o fatorial, neste caso os prints
ficam fora de ordem, é mais fácil decrementar como no curso em vídeo (até deve ter como tratar isso para poder
imprimir más daria um codigo com muito mais linhas, desnecessário.'''
n = int(input('digite um valor para saber seu fatorial: '))
c = 1
f = 1
while c <= n:
    f *= c
    c += 1
print('{} '.format(f))


#CURSO EM VÍDEO.

n = int(input('Digite um número: '))
c = n #Contador Assume o valor de n, para ser decrementado dentro do while. 
f = 1
print('{}! = '.format(n), end='') #Print o numero digitado. end da fim na linha
while c > 0:#enquanto o c for maior que zero ele cai no laço.
    print('{}'.format(c), end='')#printa o c decrementando -1 do contador.
    print(' x ' if c > 1 else ' = ', end ='')#printa a mensagem IF o c for maior que 1, caso não da fim e finaliza o calculo.
    f *= c #calcula o fatorial decrementando do contador.
    c -= 1 #decrementa o contador.
print('{}'.format(f))

#BIBLIOTECA FACTORIAL

from math import factorial

n = int(input('Digite um numero inteiro: '))
f = factorial(n)
print('Fatorial de {} é {} '.format(n, f))
