#Aula 10 condições IF ; ELSE considações.

if carro.esquerda{}: #Estrutura if python
 bloco True
 Else:
 bloco False
 
 #Exemplo para dizer se o carro é novo ou velho, na condição de abaixo de 3 anos, é novo.
 tempo = int(input('Quantos anos de fabricação tem seu carro ?'))
 
 if tempo<3:
    print('Carro novo')
    else:
    print('Carro velho')
    print('---FIM---')
    
 #Abaixo temos ele como condição simplificada.
 tempo = int(input('Quantos anos de fabricação tem seu carro ?'))
    print('Carro novo' if tempo<3 else 'Carro velho')
    print('---FIM---')
    
#Exemplo bom dia.
nome = str(input('Qual é seu nome? '))
if nome == 'Vitor':
print('Que nome lindo você tem!')
else:
print('Seu nome é tão normal')
print('Bom dia, {}'.format(nome))

#Média
n1 = float(input('Nota 1'))
n2 = float(input('Nota 2'))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m=>6.0:
print('Aprovado')
else:
print('Reprovado')


