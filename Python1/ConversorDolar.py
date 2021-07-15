#programa que conversao de dolar

n1 = float(input('Digite sua grana'))
n2 = float(input('Digite o valor do dolar'))

c = n1/n2

print('Com {} reais é possivel comprar {:.2f} dolars '.format(n1, c))