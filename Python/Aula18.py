'''
Aula 18 - Listas (parte 2)
Em listas além de dar appends em outros valores, podemos dar append
em outras estruturas.
por exemplo dentro:

'pedro' 24 dentro da lista pessoas.
pessoas = list[['Pedro', 25], ['Maria' 19],['João' 32]]
				  0	     1       0     1      0    1
				  --------       -------      ------   
Indice				 0			    1		     2
print(pessoas[0][0]) - Ou seja dentro do indice zero vou pegar o 
que está no indice zero da outra lista. Print Pedro no caso.
print(pessoas[1][1]) - Vai pegar no que está no indice 1, dentro
do indice 1 da lista, ou seja 19.
print(pessoas[2][0] - Vai printar o 2 do indice dentro da lista 0
ou seja vai printar João.
print(pessoas[1]) - Vai printar tudo do indice 1, ou seja ['Maria', 19]
'''
Exemplos práticos:
#Ex1
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste) #até aqui foi criada uma lista, dentro de outra lista.
print(galera)
[['Gustavo', 40]]

#Ex2.
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera;append(teste) 
teste[0] = 'Maria' # Neste trecho estamos mudando gustavo para maria
teste[1] = 22 #e aqui mudando 40 para 22.
galera.append(teste) #pelo fato de ligarmos as duas estruturas vai alterar as duas listas
print(galera )
[['Maria', 22], ['Maria', 22]]

Para que adicione na sequencia tem que fazer uma uma copia como abaixo.
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera;append(teste[:]) 
teste[0] = 'Maria' 
teste[1] = 22 
galera.append(teste[:]) #[:] Copia 
print(galera )
[['Gustavo', 40], ['Maria', 22]]

#Ex3
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[2][1]) = 13

for p in galera:
	print(p)
#saida vai ser
['João', 19] 
['Ana', 33]
['Joaquim', 13] 
['Maria', 45]

for p in galera:
	print(p[0])
#saida vai ser
['João'] 
['Ana']
['Joaquim'] 
['Maria']

for p in galera:
	print(f'{p[0]} tem {p[1]} anos de idade.')
#saida vai ser
João tem 19 anos de idade.
e assim por diante.
Maria...

#Adicionando lista de nomes e idade, pedindo para inserir.
galera = list()
dado = list()
for c in range(0, 5):
	dado.append(str(input('Nome: ')))
	dado.append(int(input('Idade: ')))
	galera.append(dado[:])
	dado.clear()

print(galera)

#Imprimindo maior de idade com for, dentro da lista.
galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 5):
	dado.append(str(input('Nome: ')))
	dado.append(int(input('Idade: ')))
	galera.append(dado[:])
	dado.clear()

for p in galera:
	if p[1] >= 21:
		print(f'{p[0]} é maior de idade.')
		totmai +=1
	else:
		print(f'{p[0]} é menor de idade.')
		totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')

