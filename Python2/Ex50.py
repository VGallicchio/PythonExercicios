'''50 - Faça um programa que leia seis numeros int e mostre a soma apenas daqueles que forem pares.
se o valor digitado for impar desconsidere-o'''

for n in range(0, 6):
    num(input('Digite um {} valor: '.format(n)))
    if (num % 2) == 0:
        s += num
        cont += 1
        else:
        print('Voce nao digitou nenhum numero par')
print('Voce informou {} numeros PARES e a soma foi {} '.format(cont, s))
