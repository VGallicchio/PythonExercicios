#31-Desenvolva um programa que pergunte a distância de uma viagem em KM. 
#Calcule o preço da passagem, cobrando 0,50 rs por Km para viagens de até 200km e 0,45 para viagens mais longas

dist = float(input('Qual a distância da viagem em Km'))

if dist <= 200:
    preco = dist*0.50
    print('A passagem vai custar {} R$ '.format(preco))
else:
    preco = dist*0.45
    print('A passagem vai custar {} R$ '.format(preco))


'''Ternário
distancia = float(input('Qual a distância a ser percorrida na viagem em Km')
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('O preço da passagem será {:.2F} R$ '.format(preco))'''
