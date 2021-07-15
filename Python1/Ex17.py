#/17-Programa que leia comprimento do cateto oposto e do cateto adjacente deum triangulo retangulo, 
#calcule e mostre o comprimento da hipotenusa

#solução matemática:

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2) #formula para medir hipotenusa
print('A hipotenusa vai medir {:.2f}'.format(hi))

#Solução com biblotica math. Pode se usar somente a biblotica from math import hypot
import math

co = float(input('Comprimento do cateto oposto:' ))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f)'.format(hi))
