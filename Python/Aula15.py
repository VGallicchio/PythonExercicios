#Aula 15 Interrompendo Repetições While
n = s = 0
while True:
    n = int(input('Digite um número: ' ))
    if n == 999:
        break
    else:
        s += n
print('A soma vale {} '.format(s))

''' Utilizando f Strings, conhecidas como 'peps'
O python pode-se usar as f strings por exemplo:
'''
print('A soma vale {} '.format(s)) # ao invez de fazer assim
print(f'A soma vale {s} ') #O f já faz com que a string seja assumida dentro do {}.
