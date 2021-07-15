#30-Crie um programa que leia um num int, mostrar se é par ou impar.


num = int(input('Digite um numero inteiro'))

if(num%2) == 0:
    print("O numero escolhido é par {}".format(num))
else:
    print("O numero escolhido é impar {}".format(num))
    