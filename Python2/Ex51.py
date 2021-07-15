'''51 - Faça um programa que leia o primeiro termo e a razão de uma PA. No final mostre os 10 primeiros
 termos dessa progressão'''
 
 primeiro = int(input('Primeiro termo: '))
 razao = int(input('Raaão: '))
 decimo = primeiro + (10 - 1) * razao #formula para calcular termos, o 10 num de termos, se fosse 20 seria 20 asim por diante.
 for c in range (primeiro, decimo + razao, razao):
    print('{} '.format(c), end=' - ')
 print('FIM')
 