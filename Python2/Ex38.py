''' 38 - Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:

- O primeiro valor é maior
- O segundo valor pe maior
- Não existe valor maior, os dois são iguais '''
('-='*15)
print('Comparação de igualidade numérica')
('='*15)

n1 = int(input('Digite um numero inteiro : '))
n2 = int(input('Digite outro numero inteiro : '))

if n1 > n2:
    print('O valor {} é maior que o valor {} '.format(n1, n2))
elif n1 < n2:
    print('O valor {} é maior que o valor {} '.format(n2, n1))
else:
    print('Não existe valor maior os dois são iguais')
