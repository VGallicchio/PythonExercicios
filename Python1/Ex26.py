#26-Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra 'A'
#Em que posição ela aparece pela primeira vez
#Em que posição ela aparece a ultima vez

frase = str(input('Digite uma frase')).upper().strip()

print('A palavra A aparece {} vezes na frases '.format(count('A')))
print('Ela aparece pela primeira vez na posição {}'.format(frase.find('A')+1))
print('Ela aparece a ultima vez na posição {}'.format(frase.rfind('A')+1))
