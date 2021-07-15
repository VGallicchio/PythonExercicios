''' 77- Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você devera
mostrar para cada palavra quais são as suas vogais.
'''

print('='*65)
print(f'{"DIGITE PALAVRAS SEM ACENTOS PARA SABER QUANTAS VOGAIS TEM NELA":^40}')
print('='*65)
palavras = (str(input('Digite uma Palavra: ')),
            str(input('Digite outra palavra: ')),
            str(input('Digite mais uma Palavra: ')),
            str(input('Digite a última Palavra: ')))
print('='*30)
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou': #se for colocar acentuação só colocar na onde vai encontrar ex: 'aáâãeéêiíóôoõúu'
            print(letra.upper(), end='')
