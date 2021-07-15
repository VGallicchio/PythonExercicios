'''Aula 14 - Estrutura de repetição While'''

Com while podemos fazer um laço for de outra maneira por exemplo:

numa expressão:

for c in range(1, 10):
    print(c)
print('FIM')

com while:

c = 1 #contador.
while c < 10: # enquanto o contador for menor que 10 vai repetir o laço.
    print(c)
    c += 1 # incrementando mais um ao contador. Até ele chegar na variável 10.
print('FIM') # Fim do laço.

Com o while diferemtente do for, podemos fazer flags e pontos de parada por exemplo:

n = 1 #ponto de partida para n.
while n != 0:
    n = int(input('Digite um valor: ')) #Enquanto o numero digitado não for diferente de zero o programa não vai parar.
print('Fim')

por exemplo:
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: ')) #Enquanto a resposta for S, de sim ele vai continuar rodando o programa e assumindo valores, para n.
    r = str(input('Quer continuar? [S/N] ')).upper() #para para o programa tem que digitar N.
print('FIM')

Exemplo com if.
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um numero: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Voce digitou {} numeros pares e {} numeros impares!'.format(par, impar))

'''Para  poder fazer uma decrementação de numeros basta o contador assumir o valor da variavel e fazer o contador
-1, ou -2 caso de dois em dois e assim por diante. O mesmo vale para incrmentar.
'''
n = int(input('Digite um número para decrementar até zero: '))
c = n

while c > 0:
    print(c)
    c -= 1
print('fim')

''' Incrementando.
'''
n = int(input('Digite um número para encrementar de 1 em 1 até chegar nele: '))
c = 1

while c <= n:
    print(c)
    c += 1
print('fim')
