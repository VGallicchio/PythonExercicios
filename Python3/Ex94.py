'''
Ex  94 faça um programa que leia nome, sexo e idade de várias pessoas guardando
os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final mostre:
A) Quantas pessaos cadastradas.
B) Uma lista com mulheres.
D) Uma lista com idade acima da média.
'''

pessoa = dict()
galera = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome: ')).capitalize()
    while True:
        pessoa['Sexo'] = str(input('Sexo: [M/F]: ')).upper().strip()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('Erro: Por favor, digite apenas M ou F.')
    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar ? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos')
print('C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['Sexo'] in 'Ff':
        print(f'{p["Nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da média  ', end='')
for p in galera:
    if p['Idade'] >= media:
        print('       ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
