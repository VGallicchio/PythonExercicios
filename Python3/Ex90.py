'''
Ex  90 faça um programa que leia nome e média de um aluno guardando também
a situação em um dicionário. No final mostre o conteúdo da estrutura na tela.
'''


boletim = dict()
boletim['Aluno'] = str(input('Nome do Aluno: ')).capitalize()
boletim['Média'] = float(input(f'Média de {boletim["Aluno"]}: '))
while 0 < boletim['Média'] > 10: # se for menor que zero e maior que 10 média inválida.
    boletim['Média'] = float(input(f'Média inválida digite média de 0 a 10 {boletim["Aluno"]}: '))
if boletim['Média'] >= 7:
    boletim['Situação'] = 'Aprovado'
elif 5 <= boletim['Média'] < 7: #entre 5 e 7 recuperação.
    boletim['Situação'] = 'Recuperação'
else:
    boletim['Situação'] = 'Reprovado'
for k, v in boletim.items():
    print(f' - {k} {v}')
