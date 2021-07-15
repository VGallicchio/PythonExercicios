'''
Aula 16
Tuplas

Com duplas podemos colocar mais de um elementro dentro da variável.
Ele funciona muito parecido com fatiamento de strings por exemplo.

lanche = 
hambunguer posição 0
suco posição 1
pizza posição 2
da pra fatiar como strings 

print(lanche [2]), vai printar o que estiver na posição 2
print(lanche [:4]), vai printar tudo até posição 4
print(lanche [-4]), vai printar o hambunguer que está na posição 0 ou -4 da direita pra esquerda.

len(lanche) da pra ver quantas posições estão na variavel

Da pra usar elas nos laços exemplo:

for c in lanche: para comida em lanche dentro da variavel vai estrar dentro do laço
    print(c) - vai imprimir o hambunguer e fazer o looping, vai perder a posição 0 e receber 1.

LEMBRANDO QUE AS TUPLAS SÃO IMUTÁVEIS DENTRO DO PYTHON.

() - equivalem para tuplas
[] - equivalem para listas
{} - dicionários
'''
#posição       0        1        2       3                  
lanche = ('Hambúger', 'Suco', 'Pizza', 'Pudim')
print(lanche) # printa a tupla toda.

print(lanche[1]) # vai printar suco, posição 1.
print(lanche[-2]) # vai printar a pizza, como ultima posição é 4 volta o 3 e para no 2 então por isso a pizza.
print(lanche[1:3]) # vai printar suco e pizza.
print(lanche[1]) # vai printar suco, posição 1.
print(lanche[2:]) # vai printar pizza até o final, pudim.
print(lanche[:2]) # vai printar hambúrguer e suco.
print(lanche[-2:]) # vai começar na pizza e vai até o final pudim.
print(lanche[-3:]) # vai printar suco, pizza e pudim.

for comida in lanche: 
    print(f'Eu vou comer alguma coisa {comida}') #Vai fazer o laço dizendo que vai comer tudo que estã em lanche.
print('Estou satisfeito!')

print(len(lanche))
print(sorted(lanche)) #mostra em ordem alfabetica

for cont in range(0, len(lanche)): #vai de zero até o range que estiver.
    print(lanche[cont]) #Vai imprimir todos as variaveis que estiverem na tupla.
    print(f'Eu vou comer  {lanche[cont} na posição {cont}') #vai mostrar a posição
    
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}') #vai mostrar a posição também.
 
 
 a = (2, 5, 4)
 b = (5, 8, 1, 2)
 c = a + b #Nesse caso ele concatena as tuplas e não soma.
print(c.count(5)) #vai contar quantas vezes o número 5 está aparecendo dentro de C, no caso duas vezes
print(c.index(8)) #vai dizer em que posição está o 8 dentro da Tupla.
print(c.index(5, 1)) #da pra fazer com deslocamento.

pessoa = ('Vitor', 39. 'M', 99.88) #Dentro de python pode ter dados de tipos diferentes dentro da Tupla.
del(pessoa) #pode deletar a variavel.


 