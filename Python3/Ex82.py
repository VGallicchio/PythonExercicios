'''Ex 82 Crie um programa para ler vários numéros e colocar em uma lista
Depois crie duas listas extras que vão conter apenas os valores impares e
os pares digitados, ao final mostre o conteudo das três listas geradas.
'''
print('='*30)
num = []
par = []
impar = []
n = 0
while True:
    num.insert(n, int(input(f'Digite o {n+1}º número: ')))
    n += 1
    num.sort()
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja inserir outro número? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print('-'*30)
print(f'Todos os números digitados {num}')
print(f'Numeros pares {par}')
print(f'Numeros impares {impar}')

#Curso em vídeo
num = list()
pares = list()
impares = list()
while True:
	num.append(int(input('Digite um número: ')))
	resp = str(input('Quer continuar? [S/N] '))
	if resp in 'Nn':
		break
for i, v in enumerate(num):
	if v % 2 == 0:
		pares.append(v)
	elif v % 2 != 0:
		impares.append(v)
print('-=' * 30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')
