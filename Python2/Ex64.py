'''Ex 64 - Crie um programa que leia vários numeros inteiros pelo
teclado. O programa só vai parar quando o usuário digitar o valor
999, que é a condição de parada. No final mostre quantos números 
foram digitados e qual foi a soma entre eles (desconsiderando o flag)'''

#Meu

n = 0
c = 0
soma = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))  
    if n != 999:
        c += 1
        soma += n
print('No total foram digitados {} Números e a soma entre eles foi {}: '.format(c, soma))

#Colega
n = 0
s = 0
c = -1
while n != 999:
    c += 1
    s += n
    n = int(input('Digite um número [999 para parar]: '))
print('A soma é de {} e a quantidade é de {}'.format(s, c))

#Curso em vídeo
n = s = c = 0
n = int(input('Digite um número [999 para parar]: ')) # colocando o flag fora, ele não conta no final. pedindo o n por ultimo.
while n != 999:
    c += 1
    s += n
    n = int(input('Digite um número [999 para parar]: '))
print('A soma é de {} e a quantidade é de {}'.format(s, c))

