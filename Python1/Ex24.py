#24 - Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra Santo

cidade = str(input('Em que cidade você nasceu ? ')).strip()
print(cidade[:5].upper() == 'SANTO')


#cidade = str(input('Em que cidade você nasceu ? ')).strip()
#print('A cidade que você nasceu começa com Santo ? {}'.format(cidade[:5].upper == 'SANTO'()))

