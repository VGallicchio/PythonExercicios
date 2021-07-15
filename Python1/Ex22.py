#22- Crie um programa que leia o nome completo de uma pessoa e mostre:+/

#O nome com todas as letras maisculas.
#O nome com todas minusculas.
#Quantas letras ao todo (sem considerar os espaços)
#Quantas Letras tem o primeiro nome.

nome = str(input('Insira seu nome completo')).strip() #O strip elimina os espaços que forem usados de forma incorreta ao se digitar um nome por exemplo por um usário tanto antes como depois

print('Analisando seu nome')
print('Seu nome em maisculas {}'.format(nome.upper()))
print('Seu nome em minusculas {}'.format(nome.lower()))
print('Seu nome tem aotodo {} letras'.format(len(nome)-nome.count(' '))) #(' ') count, faz com que ele conte com len, excluindo o espaço
#print('Seu primeiro nome tem {} letras'.format(count(' '))) #Aqui ele conta até o primeiro ' ' espaço, vazio.
#pode colocar tambem os nomes como listas e pedir para ler so o numero de letras da primeira lista
separa = nome.split() # aqui com o split ele divide o nome em listas
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))

