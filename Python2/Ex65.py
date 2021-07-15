'''Ex 65 - Crie um programa que leia vários numeros inteiros pelo
teclado. No final da execução, mostre a média entre todos os valores
e qual foi o maior e o menor valor lido. O programa deve perguntar ao
usuário se ele quer ou não continuar digitando valores.'''

#Meu
r = 'S'
n = 0
m = c = s = 0
maior = menor = n

while r in 'Ss':
    n = int(input('Digite um valor: '))
    r = str(input('Deseja inserir outro valor [S/N]: ')).strip()[0]
    c += 1
    s += n
    m = s/c
    if n > maior:
        maior = n
    else:
        menor = n
print('Você digitou {} números e a média entre eles é {} '.format(c, m))
print('Maior valor digitado {}: '.format(maior))
print('Menor valor digitado {}: '.format(menor))

#Curso em vídeo

resp = 'Ss'
media = soma = quant = maior = menor = 0

while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Deseja digitar outro número [S/N]: ')).upper().strip()[0]
media = soma / quant
print('A média dos números é {:.2f}: '.format(media))
print('O maior número digitado foi {} e o menor foi {}. '.format(maior, menor))
