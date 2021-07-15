#27-Faça um programa que leia o nome completo de uma pessoa e mostre em seguida o primeiro e 
#o ultimo nome separadamente.
#Ex: Ana Maria de Souza
#primeiro = Ana
#Ultimo = Souza

n = str(input('Digite o seu nome').strip()
nome = n.split()
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {} '.format(nome[len(nome)-1]))
