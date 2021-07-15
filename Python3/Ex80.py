'''Ex 80 Crie um programa onde o usuário possa digitar cinco valores e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()). No final mostre na lista ordenada na tela.
'''
print('\33 lista').upper()
lista = list()
for c in range(0, 5):
    num = int(input(f'Digite o {c+1}ª valor: '))
    if c == 0 or num > lista[-1]:
        lista.append(num)
		print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
				print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores diogitados em ordem foram {lista}')
