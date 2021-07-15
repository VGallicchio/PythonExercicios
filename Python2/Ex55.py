'''55 - Faça um programa que leia o peso de 5 pessoas e mostre no final qual foi o maior e menor
peso lidos'''

pesmenor = 0
pesomaior = 0

for c in range(1, 5):    
    paciente = str(input('Digite o nome do paciente {} :'.format(c)))
    peso = float(input('Digite o peso do paciente :'.format(c)))
    if c == 1:
        pesmaior = peso
        pesmmenor = peso
    else:
        if peso > pesmaior:
            pesmaior = peso
        if peso < pesmenor:
            pesmenor = peso
print('O maior peso foi do paciente {} que pesa {} Kg'.format(paciente, pesmaior))
print('O menor peso foi do paciente {} que pesa {} Kg'.format(paciente, pesmenor))
