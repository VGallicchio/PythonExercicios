''' 66 - Crie um programa que leia vários números interios pelo teclado. O programa só vai parar quando digitar o valor
999, que é a condição de parada. No final mostre quantos números foram digitados e qual foi a soma entre eles 
desconsiderando o flag '''

s = c = 0
while True:
    n = int(input('Digite um número inteiro [999 - para parar]: '))
    if n == 999:
        break
    else:
        c += 1
        s += n
print('A soma dos {} valores foi {} '.format(c, s))
print(f'A soma dos {c} números foi {s}')
