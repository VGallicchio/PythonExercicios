'''54 - Faça um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas pessoas
ainda não atingiram a maioridade e quantas já são maiores'''

from datetime import date
('-='*15)
print('Maioridade')
('-='*15)
atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1, 8):
    nome = str(input('Digite o nome da {} pessoa: '.format(c)))
    nasc = int(input('Qual seu ano de nascimento da pessoa {}: '.format(c)))
    idade = atual - nasc
#print('{} tem {} anos de idade em {}.'.format(nome, idade, atual)) verificador idade.
    if idade < 18:
    totmenor += 1
    else:
    totmaior += 1
print('O numero de pessoas menores de 18 são {} '.format(totmenor))
print('O numero de pessoas maiores de 18 são {} '.format(totmenor))
print('As  pessoas menores de 18 são {} '.format(nome))
print('AS pessoas maiores de 18 são {} '.format(nome))
