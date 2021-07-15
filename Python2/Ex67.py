''' 67 - Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário
o programa será interrompindo, quando o número solicitado for negativo'''

c = 0 
while True:
    n = int(input('Digite um número para calcular sua tabuada: '))
    print('-----'*20)
    if n < 0:
        break
    for c in range (1, 11):
        print('{} x {} = {} '.format(n, c, n*c))
    print('-----'*20)
print('FIM')
