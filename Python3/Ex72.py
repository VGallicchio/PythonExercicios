'''72 - Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

#MEU
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte',)
while True:
    pos = -1
    while pos < 0 or pos > 20:
        pos = int(input('Digite um número entre 0 e 20: '))
        if pos not in [0, 20]:
            print('Número fora do escopo')
    print(f'Você digitou o número {numeros[pos]}')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja inserir outro número ? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print('FIM DO PROGRAMA')

#Curso em vídeo
cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte',)
while True:
	num = int(input('Digite um número entre 0 e 20: '))
	if 0 <= num <= 20:
		break
	print('Tente Novamente. ', end='')
print(f'Você digitou o número {cont[num]}')
