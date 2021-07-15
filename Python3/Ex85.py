'''
Ex 85 Crie um programa onde o usuário possa digitar sete valores números e cadastre-os em uma lista
unica que mantenha separados os valores pares e impares. No final, mostre os valores
pares e impares em ordem crescente.
'''

num = [[], []]
n = 0

for n in range(1, 8):
    n = int(input(f'Digite {n}º um número: '))
    if n % 2 == 0:
        if n in num[0]:
            print('-='*30)
            n = int(input('Número repetido digite outro número: '))
            num[0].append(n)
        else:
            num[0].append(n)
    else:
        if n in num[1]:
            print('-='*30)
            n = int(input('Número repetido digite outro número: '))
            num[1].append(n)
        else:
            num[1].append(n)
num[0].sort()
num[1].sort()
print('-='*30)
print(f'Números pares digitados {num[0]}')
print(f'Números impares digitados {num[1]}')