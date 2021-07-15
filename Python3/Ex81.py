'''Ex 81 Crie um programa que vai ler vários números e colocar em uma lista
depois, mostre:
a) Quantos números foram digitados.
b) A lista de valores ordenada de forma decrescente.
c) se o valor 5 foi digitado e está ou não na lista.
'''
print('='*30)
num = []
n = 0
while True:
    num.insert(n, int(input(f'Digite o {n+1}º número: ')))
    n += 1
    num.sort(reverse=True)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja inserir outro número? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print('-'*30)
if 5 in num:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista')
print(f'Ao todo foram digitados {n} números.')
print(f'Números digitados em ordem drescente{num}')

# Curso em vídeo
valores = []
while True:
	valores.append(int(input('Digite um valor: ')))
	resp = str(input('Quer continuar? [S/N] '))
	if resp in 'Nn':
		break
print('-=' * 30)
print(f'Você digitou {len(valores)} elementos. ')
valores.sort(revere=True)
print(f'Os valores em ordem drescente são {valores}')
if 5 in valores:
	print('O valor 5 faz parte da lista!')
else:
	print('O valor 5 não foi encontrado na lista!')

