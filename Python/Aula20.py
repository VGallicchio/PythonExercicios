'''
Aula 20 - Funções. O python pode usar funções personalizadas, chamaadas de DEF.
Supomos que queremos criar uma rotina de mostrar linhas. Seria
como def:
def mostraLinha():
	print('--------------------------------')

Para chamar a função agora é só chamar pelo nome dela ou seja mostraLinha()
ai vai chamar o que tem dentro da def mostraLinha().
Com as def - funções podemos personalizar de várias formas.
e colocar algo que poderia se repetir várias vezes.
'''

a = 4
b = 5
s = a + b
print(s)

a = 8
b = 9
s = a + b
print(s)

a = 2
b = 1
s = a + b
print(s)

'''
Aqui são três trechos iguais. Então vamos exemplificar uma função.
'''
def soma(a, b):
    s = a + b
    print(s)

#programa principal
soma(4, 5)
soma(8, 9)
soma(2, 1)


'''
Podemos também definiar quais são as variáveis:
'''
def soma(a, b):
    print(f' A = {a} e B = {b}')
    s = a + b
    print(f' A soma A + B = {s}')


#programa principal
soma(b=4, a=5)

'''
Empacotando variáveis:
o * dentro do () faz com que a variavel possa receber quantas coisas necessarias
pelo programador.
'''
def contador(*num):

contador(5, 7, 3, 1, 4)
contador(8, 4, 7)

'''
Podemos também empacotar :
'''
def contador(*num):
    print(num)


contador(5, 7, 3, 1, 4)
contador(8, 4, 7)
#Criar como um for
def contador(*num):
    for valor in num:
        print(f'{valor} fim', end='')


contador(5, 7, 3, 1, 4)
contador(8, 4, 7)

#definir len...
def contador(*num):
    tam = len(num):
		print(f' Recebi os valores {num} e são ao todo {tam} números', end='')


contador(5, 7, 3, 1, 4)
contador(8, 4, 7)

#podemos também tranbalhar com listas.
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)

#aqui por exemplo criamos uma função que dobre os valores dentro da lista.

#desempacotamento
def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)
