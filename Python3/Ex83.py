'''Ex 83 Crie um programa onde o usuário digite uma expressão
qualquer e use parenteses, seu aplicativo deverá analisar se a 
expressão passada está com os parenteses abertos e fechados na ordem correta.
'''

expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
