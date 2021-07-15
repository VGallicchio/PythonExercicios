''' 41 - Escreva um programa que leia o ano de nascimento de um atleta e mostre sua categoria

- Até 9 anos: Mirim
- Até 14 ano: Infantil
- Até 19 anos: Junior
- Até 25 anos: Sênior
- Acima: Master '''
'''
('-='18)
print('Categoria do Atleta')
('-='18)

idd = int(input('Qual a idade do atleta '))

if idd <= 9:
    print('Atleta Mirim')
elif idd <= 14:
    print('Atleta Infantil')
elif idd <=19:
    print('Atleta Junior')
elif idd <=20:
    print('Atleta Sênior')
else:
    print('Atleta Master')
'''
from datetime import date
atual = date.today().year
nasc = int(input('Qual seu ano de nascimento: '))
idade = atual - nasc
print('O Atleta tem {} anos. '.format(idade))

if idd <= 9:
    print('Atleta Mirim')
elif idd <= 14:
    print('Atleta Infantil')
elif idd <=19:
    print('Atleta Junior')
elif idd <=25:
    print('Atleta Sênior')
else:
    print('Atleta Master')
