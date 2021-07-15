#Escreva um programa que pergunte a qtd de KM percorridos e qtd de dias alugados. Preço a pagar deve ser
#baseado por alguel diario 60 R$ e 0,15 R$ por KM rodado

diarias = int(input('Insira a quantidade de dias que o carro foi alugado :'))
km = float(input('Insira quantidade de KM rodados :'))

custo = (diarias * 60) + (km * 0.15)

print('O custo do aluguel será {:.2f} R$'.format(custo))
