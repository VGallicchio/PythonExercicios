'''
Ex 89 Crie um programa que leia nome e duas notas de vários alunos
guarde tudo em uma lista composta. No final mostre um boletim contendo
a média de cada um e permite que o usuário possa mostrar as notas de
cada um individualmente.
'''
boletim = list()
lista = []

while True:
    aluno = str(input('Aluno: '))
    n1 = float(input('Nota 1: '))
    while True:
        if n1 > 10 or n1 < 0:
            n1 = float(input('Nota inválida [0 a 10..]: '))
        else:
            break
    n2 = float(input('Nota 2: '))
    while True:
        if n2 > 10 or n2 < 0:
            n2 = float(input('Nota inválida [0 a 10..]: '))
        else:
            break
    media = (n1 + n2) / 2
    if aluno not in lista:
        boletim.append([aluno, [n1, n2], media])
    resp = str(input('Deseja Inserir outro Aluno? [S/N]')).upper().strip()[0]
    if resp not in 'SsNn':
        resp = str(input('Inválido digite ? [S/N]')).upper().strip()[0]
    if resp in 'Nn':
        break
print('Boletim')
print('--' * 30)
print(f'{"No.":<4}{"Nome.":<10}{"Média":>8}')
print('--' * 30)
for i, a in enumerate(boletim):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('--' * 30)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(boletim) - 1:
        print(f'Notas de {boletim[opc][0]} São {boletim[opc][1]}')
print('FIM Boletim')
