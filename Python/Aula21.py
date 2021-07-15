'''
Aula 21 - Função (Parte2)

Ativando no console a função help() podemos ter o manual de todas as funçoes do python basta
digita-las. Também podemos dar um print em doctstring ex:
print(input.__doc__), para saber o conteudo de input as informações.

Docstrings: é basicamente uma string de documentação. Todas funcionalidades tem sua funcionalidades.
ex:
def contador(i, f, p):
 Em uma função como essa. E alguem está usando a funcionalidades.
 Podemos criar um help() para o usuário saber como usar.
 
 para fazer uma docstring
 so abrir aspas duplas e colocar os parametros.
 """
 -> Faz a contagem e ....
 .......
 """
O que tiver ai dentro vai ser o help() docstring.

Parmetros Opcionais:
por exemplo temos uma funcionalidade de somar somar(3, 2, 5)
função seria def somar(a, b, c):
	s=a+b+colocar
	print(s)
se colocar somar(8, 4)
vai faltar parametro.. ou seja podemos usar o parametro opcional.
somar(a, b, c=0):
como não foi informado o terceiro valor o c vai receber zero.
podemos colocar todos como parametros adcionais.
ai qualquer coisa q vc colocar ele vai pegar os parametros opcionais.

Escopo de variáveis: Seria o local onde a variável vai existir e onde ela não vai mais 
existir...

ex:
def teste()
	print(f'Na função teste, n vale {n}')
	

#Programa principal.
n = 2
print(f'No programa principal, n vale {2}')
teste()


Mesmo N tendo sido definido no programa principal ele vai funcionar dentro de toda a área
da função. Escopo global.
Se adcionarmos:
def teste()
	x = 8
	print(f'Na função teste, n vale {n}')
	print(f'Na função teste, x vale {x}')
	

#Programa principal.
n = 2
print(f'No programa principal, n vale {2}')
teste()
print(f'No programa principal, x vale {x}') # Aqui teremos o erro, pois como na variavel x ela está so dentro de teste ela só funciona na função ou seja o X é uma variavel local.

Ex:

def funcao()
	n1 = 4
	print(f'N1 dentro vale {n1}')

n1 = 2
funca()
print(f'N1 Fora vale {n1}')


Porém podemos definir que podemos usar a variável global ou seja.
Ex:

def funcao()
	global n1
	n1 = 4
	print(f'N1 dentro vale {n1}')

n1 = 2
funca()
print(f'N1 Fora vale {n1}')

Aqui dizemos para o python não use n1, assim a variavel n1 dentro da função
vai passar a ter o valor da global ou seja n1 em global vai valer 4.

Retorno de valores:
return()

def somar(a=0, b=0, c=0)
	s = a+b+coisa
	return s
	
resp = somar(3, 2 ,5)
somar(2, 2)
somar(6)
nesse caso ele faz um pra cada linha, se eu quiser fazer que elas apareça juntas ou seja
As somas valem 10, 4 e 6 podemos usar o return.
a variável vai para dentro de s.
ou podemos usar até um print.
r1 = somar(3, 2 ,5)
r2 = somar(2, 2)
r3 = somar(6)
print(f'meus calculos deram {r1}, {r2} e {r3}.')

O return não é só para numeros, podemos retornar valores logicos, boleanos etc...
def par(n=0)
	if n % 2 = 0:
		return True
	else:
		return False

num = int(input('Digite um número: '))
if par(num):
	print('É par!')
else:
	print('Não é par!')


'''

#pratico.
def fatorial(num=1):
	f = 1
	for c in range(num, 0, -1):
		f *= cada
	return f
	
n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual {fatorial{n}'}


#pratico.
def fatorial(num=1):
	f = 1
	for c in range(num, 0, -1):
		f *= cada
	return f
	
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}'}
