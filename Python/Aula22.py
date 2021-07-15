'''
Aula 22

Modularização serve para facilitar o código, manutenção etc etc..
No exemplo vamo pegar o programa que ta muito grande e modular.
Colocar as funções em uteis.py
para chamar o que está lá em uteis.py devemos usar o comando import.
Em python todo arquivo.py pode ser um modulo, desde que tenha função.
pode importar so uma função de dentro do modulo ex:
from uteis import fatorial, dobro
E importante ressaltar que esse método não e mais recomendado, pois
pode ter conflito se dois modulos tiverem o mesmo nome. No caso ele importa
sempre o ultimo.

Além da criação de modulos, se for necessário utilizar vários módulos podemos organizalos
em py isso é chamado de pacote.
Por exemplo se tiver várias funcoes dentro de uteis, criamos vários modulos como pacotes
pacote uteis no caso.
podemos separar por assuntos tipo tratamento de string etc...
por exemplo:
import uteis
from uteis import datas
Dentro de um projeto python toda pasta é considerada um pacote.

__init__.py vai ser criado sempre junto com o pacote.

para criar um pacote, dentro do seu projeto crie new python package.
dentro de uteis podem ser criados outros pacotes, modulos etc.

'''
import uteis

num = int(input('Digite um valor: '))
fat = uteis.fatorial(num)
print(f'O fatorial {num} é {fat}.'
print(f'O dobro de {num} é {uteis.dobro{num}}')


### exemplo com pacote
from uteis import numeros

num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O fatorial {num} é {fat}.'
print(f'O dobro de {num} é {numeros.dobro{num}}')

#No caso o pacote numeros está dentro do pacote uteis. 

