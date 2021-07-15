#35-Escreva um programa que leia o comprimento de tres retas e diga ao usuário se ele pode ou não formar
#um triangulo
'''
if:
    print("")
elif:
    print("")
else:
    print("")
    if da net que funciona sei lá o porque''' 
    
print('-='*20)
print('Analisador de Triângulos: ')
print('-='*20)
r1 = float(input('Primeiro segmento de reta'))
r2 = float(input('Segundo segmento de reta'))
r3 = float(input('Terceiro segmento de reta'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('OS segmentos acima podem formar triangulo!')
else:
    print('Os segmentos acima não podem formar triangulo!')
        