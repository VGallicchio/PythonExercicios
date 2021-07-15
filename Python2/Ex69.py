'''69 Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá 
perguntar se o usuário quer ou não continuar. No final mostre:
A - Quantas pessoas tem mais de 18 anos.
B - Quantos homens foram cadastrados.
C - Quantas mulheres tem menos de 20 anos.
'''
import os
h = m = maior = 0
r = 'Ss'
while r in 'Ss':
    nome = str(input('Digite nome: '))
    idd = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()[0]
    r = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    os.system('clear')
    if idd > 18:
        maior += 1
    if sexo != 'M' and sexo != 'F':
        print('Sexo Inválido digite M - para Masculino e F - para feminino')
    if sexo in 'Mm':
        h += 1
    if sexo in 'Ff' and idd < 20:
        m += 1
print('Foram cadastrados {} pessoa(s) com mais de 18 anos; \n{} pessoa(s) do sexo Masculino; \n{} Mulher(es) com menos de 20 anos '.format(maior, h, m))
print('FIM')

#Curso em vídeo
tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
       sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}' )
print(f'Ao todo temos {totH} homens cadastrados')
print(f'E temos {totM20} mulheres com menosd e 20 anos')
