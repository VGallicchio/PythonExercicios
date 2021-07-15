'''Aula extra como colocar cores em python
aula mundo 1 rever se for preciso
é o codigo para você poder colcoar cores.
\033[style back text m
cor do estilo, cor do texto e cor do fundo.

exemplo
\033[0;33;44;m
0 estilo, 33 texto, 44 fundo

para estilo o 0, 1, 4 e 7 são os que funcionam melhor para terminal, porém existem outros
estilo:
0 = sem estilo
1 = negrito
4 = underline
7 = inverte as config.

texto:
cada numero representa uma cor
30 = branco  - 40
31 = vermelho - 41
32 = verde - 42
33 = amarelo - 43
34 = azul esc - 44
35 = roxo - 45
36 = azul claro -46 
37 = cinza. - 47 - background
para mais cores precisa usar bibliotecas e etc...

cor de fundo:
mesmas cores do que as anteriores na mesma ordem so que numeração a partir de 40 até 47:

abaixo exemplos
'''
Teste print('\033[0;30;41mOlá, Mundo![m') #assim deve ficar o código.
print('\033[7;33;44mOlá, Mundo!\033[m')

Teste\033[4;33;44[m
Teste\033[1;35;43[m

#Exemplo 2
nome = 'Vitor'
print('Olá! Muito prazer em te conhecer, {}{}{}'.format('\033[4;34m',nome, '\033[m'))

#exemplo 3:
cores = {'limpa':\033[m', 'azul':'\033[34m'}
