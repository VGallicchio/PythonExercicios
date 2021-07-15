''' 40 - Escreva um programa que leia duas notas de um aluno calcule a media e mostre:

- abaixo de 5.0 reprovado.
- O entre 5.0 e 6.9 recuperação
- Média 7.0 ou superiro aprovado '''
('-='18)
print('Aprovado/Reprovado')
('-='18)

n1 = int(input('Digite sua primeira nota '))
n2 = int(input('Digite sua segunda nota '))
media = (n1+n2)/2

if media < 5.0:
    print('Reprovado')
elif media == 5.0 and <= 6.9:
    print('Recuperação')
else:
    print('Aprovado')
