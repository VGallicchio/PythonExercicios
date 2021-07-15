'''
Aula 19
Os dicionários podem ser declarados de duas formas assim como tuplas e listas.
dados = dict() onde dict constrou a variavel dados como um dicionario.
dados = {} ou por colchetes.
dados = {'nome': 'Pedro', 'idade': 25} - ou seja pedro é o valor e nome 'endereço', indice.
print(dados['nome']) - Pedro
print(dados['idade']) - 25
Em dicionários podemos inserir dados de forma em que por exemplo:
dados['sexo']='M' - Ou seja estamos dizendo que sexo dentro do dicionário receberemos M, de masculino.
Também podemos remover elementos usando o comando del.
del dados['idade'], ele perde o elemento e a estrutura.

print(filme.values())
.values() dentro de dicionários retorna todos os valores dentro dele.
Ou seja o que está dentro dos valores.


print(filme.keys()) vai pegar tudo que estiver como chaves. Por exemplo titulo ano etc...

Se quiser pegar ambos tanto valor como chave, tem que usar items.
print(filme.items())
Com isso podemos usar o For como já sabemos.

for k, v in filme.items():
para cada K - chave e V - Valor.
	print(f'O (k) é (v)')
O titulo é Star Wars.
O Ano é 1977
O Diretor é George Lukas

Lembrando que é sempre possivel ajuntar listas, tuplas e dicionarios.
Ou seja pode se criar uma lista onde se tem um diciionário dentro.

Por exemplo os filmes podem estar dentro de uma lista locadora:
print(locadora[0]['ano'])
Vai printar a referencia zero da lista e o ano dentro do diciionário.

'''
#Exemplos:
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas)
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]}')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
for k in pessoas.values():
    print(k)
for k, v in pessoas.items(): #meio que é no lugar do enumerate para dicionários.
    print(f'{k} = {v}')

################################
#Deletando
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
del pessoas['sexo']
for k, v in pessoas.items(): #meio que é no lugar do enumerate para dicionários.
    print(f'{k} = {v}')

################################
#Alterando
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
pessoas['nome'] = 'Leandro'
for k, v in pessoas.items(): #meio que é no lugar do enumerate para dicionários.
    print(f'{k} = {v}')

################################
#Adicionando
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
pessoas['peso'] = 98.5
for k, v in pessoas.items(): #meio que é no lugar do enumerate para dicionários.
    print(f'{k} = {v}')

################################
#Criando diciionário dentro de uma listas

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])

################################
#Adicionando dicio a uma lista com append.
brasil = list()
estado = dict()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) #dicionários ñ aceitam fatiamento. Deve-se usar o copy comando inetrno para dicionários.
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}. ')
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print() #pode usar laços dentro de laõs há várias opções.
