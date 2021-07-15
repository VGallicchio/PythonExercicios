#29-Escreva um programa que leia a velocidade de um carro.
#Se ele passar 80km/h mostrar mensagem que foi multado.
#A multa vai custar 7rs por cada km acima do limite.

from random import randint
c = randint(0, 250)
print("Você passou no radar a {} Km/h".format(c))
if(c > 80):
    multa = (c-80)*7
    print("Você foi multado, em um valor de {} R$".format(multa))
else :
    print("Dentro do limite de velocidade")
