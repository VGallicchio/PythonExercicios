#Aula 13 Estrutura de repetição For.

for c in range (1,10): #estrutura de laço de repetição for, python.

for c in range(0,3): #Exemplo.
passo
pula
passo
pega

for c in range(0,3):
 if moeda:
  pega
 passo
 pula
 passo
 pega
 
 #exemplo
for c in range(0,6):
    print(c) #vai repetir o c seis vezes
    print(fim) #Caso coloque dentro o python se comporta como ele está dentro do laço, não precisa especificar end for.. etc..
print('Fim') # aqui ele está fora do laço.

for c in range(6,0, -1): # Desta forma ele se comporta desincremantando -1 até 0. 
#Ou +1 para incrementar, ou 2 para pular de 2 em 2, assomo como outras linguagens.
    print(c) #vai repetir o c seis vezes
print('Fim') 

#Exemplo
n = int(input('Digite um número: ')) #Obviamente podemos denominar como variável o numero de 'passos';
for c in range (0, n+1):
    print(c)
print('FIM')

#Exemplo
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: ')) #Aqui denominamos todo o laço como variáveis.
for c in range (i, f+1, p):
    print(c)
print('FIM')

#Exemplo
s = 0
for c in range (0, 4):
  n = int(input('Escolha um numero: '))#Da para dizer que ele vai pedir o numero N vezes de acordo com o laço.
  s + = n #Para o laço ele vai fazer o somatório de todos os valores.
print('O somatório de todos os valores foi {}: ')
