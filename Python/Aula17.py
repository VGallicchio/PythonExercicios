#Aula 17 listas (1)

''' Diferentemente das tuplas as listas são mutáveis
vc pode adicionar ou remover itens da lista. Para remover
ele simplesmente remove o que estava na lista e re-organiza 
os indices, se tentar remover um indice que não está na lista
vai dar erro, com o um if da pra tratar isso.
Da para criar listas com range e eles assumem os indíces.

'''
#exemplo verificar para remover
if 'pizza' in lanche: #exemplo para verificiar e remover indice.
	lanche.remove('pizza')

#ex lista range
valores=list(range(4, 11))

valores:
4 5 6 7 8 9 10
indices
0 1 2 3 4 5 6
#O sort, organiza os valores. 
valores=[8, 2, 5, 9, 10]
valores:
8 2 5 9 10
indices
0 1 2 3 4 
valores.sort()
valores:
2 5 8 9 10
indices
0 1 2 3 4
valores.sort(reverse=True)#faz o sort reverso
#len(valores) vai dizer qual tamanho dos indices. 0 até o fim.

#Exemplos práticos:
num = [2, 5, 9, 1]	#Criando lista e mutando indice
num[2] = 3
num.append(7) #adicionando valor a lista
num.sort() #colocando em ordem
num.insert(2, 0) #adicionando na posição 2 o valor 0. 
num.pop() #deleta o ultimo valor
num.pop(2) #deleta o elemento no indice 2
num.remove(2) #remove o primeiro elemento que ele encontrar com o parametro que estiver na lista no caso o 2
print(num)
print(f'Essa lista tem {len(num)} elementos. ') #Mostrando tamanho de indices de tuplas

####
valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores: #para cada valor em valores
	print(f'{v}...', end='')

valores = list()	
for c, v in enumerate(valores): #enumerate pega tanto a chave quanto valor
	print(f'Na posição {c} encontrei o valor {v}! ', end='')
print('Cheguei ao final da lista')	

###

a = [2, 3, 4, 7]
b = a 
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}') #aparentemente ele vai mexer so na lista B,  porem quando se igual as listas elas se ligam.

#Para fazer uma copia da lista:

a = [2, 3, 4, 7]
b = a[:] 
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}') #copia da lista ai muda o valor

