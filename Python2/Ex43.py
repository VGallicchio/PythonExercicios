''' 43 - Escreva um programa que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status,
de acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida '''

('-='*15)
print('CALCULO IMC')
('-='*15)

nome = str(input('Digite o nome do paciente')).strip()
peso = float(input('Insira o peso do paciente'))
alt = float(input('Insira a altura o paciente'))
('-='*15)
IMC = (alt ** 2)/peso
print('De acordo com os dados o IMC do paciente é {:.1f}: '.format(IMC))

if IMC < 18.5:
    print('Abaixo do peso')
elif 18.5 <= IMC < 25:
    print('Peso ideal')
elif 25 <= IMC < 30:
    print('Sobrepeso')
elif 30 <= IMC < 40:
    print('Obesidade')
else
    ('Obesidade Mórbida')
