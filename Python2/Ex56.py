'''56 - Faça um programa que leia nome, idd e sexo de 4 pessoas. no final o programa deve mostrar:
media de idd.
nome do homem mais velho 
qntas mulheres tem menos de 20 anos.
'''
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for p in range(1, 5):
    print('------------ {}ª PESSOA ---------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo M/F: '))
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        mediaidade = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é {} anos '.format(mediaidade))
print('O homem mais velho é {} e tem {} anos '.format(nomevelho, maioridadehomem))
print('Ao todo são {} mulheres com menos de 20 anos '.format(totmulher20))
