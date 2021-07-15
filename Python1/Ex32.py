#32-Faça um programa que leia um ano qualquer e diga se ele é bissexto.

'''Anos bissextos são aqueles que são múltiplos de 4, como 1996, 2000, 2004 etc 
(que podem ser divididos por 4 deixando resto 0).
Porém, há uma exceção: múltiplos de 100 que não sejam múltiplos de 400.

Uma das duas condições a seguir deve ser verdadeira:
Condição 1: Ser múltiplo de 4 e não ser múltiplo de 100
Condição 2: Ser múltiplo de 400 (se for múltiplo de 400 automaticamente é de 4)'''

Logo, temos o código:
ano = int(input('Ano: '))

if (ano%4==0 and ano%100!=0) or (ano%400==0): #!= diferente de zero.
    print('Bissexto')
else:
    print('Não é bissexto')

'''
Comando pegar a data atual.
from datetime import date
biblioteca datetime
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual'))
if ano == 0:
ano = date.today().year
'''
