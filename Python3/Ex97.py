'''
Ex 97 - Faça um programa que tenha uma função de chamada escreva(), que receba
um texto qualquer como parametro e mostre uma mensagem com tamanho adaptável.

ex:
escreva('Olá, Mundo!').

Saida:
~~~~~~~~~~
Olá Mundo!
~~~~~~~~~~
'''

def escreva(texto):
    tam = len(texto) + 4
    print('~' * tam)
    print(f' {texto} ')
    print('~' * tam)


texto = str(input('Digite um Texto: '))
escreva(texto)
