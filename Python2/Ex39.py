''' 39 - Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade

- Se ele ainda vai se alistar exercito.
- Se é a hora de se alistar
- Se já passou do tempo do alistamento 

Seu programa também deverá mosrar o tempo que faltou ou que passou do prazo 
desafio ler sexo m/f dizer se for mulher n pode.
'''

'''
('-='*15)
print('Alistamento')
('-='*15)
idd = int(input('Qual sua idade recruta ? '))

if idd < 18:
    print('Parabéns você ainda vai se alistar bem vindo recruta')
elif idd = 18:
    print('Parabés você deve se alistar imediatamente recruta')
else:
    print('Parabéns você já cumpriu está etapa, está livre recruta')

'''

from datetime import date
('-='*15)
print('Alistamento')
('-='*15)
atual = date.today().year
nasc = int(input('Qual seu ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos de idade em {}.'.format(nasc, idade, atual))
if idade < 18:
    saldo = 18 - idade
    print('Parabéns você ainda vai se alistar ainda faltam {} anos para ser um recruta'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será no ano {}. '.format(ano))
elif idade == 18:
    print('Parabés você deve se alistar imediatamente recruta')
else:
    saldo = idade - 18
    print('Parabéns você já cumpriu está etapa, está livre de ser um recruta há {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi no ano {}. '.format(ano))
