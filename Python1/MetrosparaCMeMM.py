#programa que leia um valor em metros e converta para cm e mm

n = float(input('Digite a metragem'))

c = n*100
m = n*1000

print('A medida de {} metros para centimétros é {} cm, e para milimetros é {} mm'.format(n, c, m))