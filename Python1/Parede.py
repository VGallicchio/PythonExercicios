#programa que leia largura e altura e calcula a area e quantidade de tinta necessaria, cada litro de tinta pinta 2m quadrados


altura = float(input('Digite a altura da parede'))
largura = float(input('Digite a largura da parede'))

area = altura*largura

print('Uma parede com dimensões de {}m x {}m tem area de {}m²'.format(altura, largura, area))

qtdtinta = area/2

print('Para pintar esta parede serão necessários {} Litros de tinta'.format(qtdtinta))