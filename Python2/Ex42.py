''' 42 - Refaça o desafio 35 dos triangulos, acrescentando o recurso de mostrar que o tipo de triangulo 
será formado:

- Equilátero: todos os lados iguais
- Isósceles: Dois lados iguais 
- Escaleno: todos os lados diferentes'''

print('-='*20)
print('Analisador de Triângulos: ')
print('-='*20)
r1 = float(input('Primeiro segmento de reta'))
r2 = float(input('Segundo segmento de reta'))
r3 = float(input('Terceiro segmento de reta'))


if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('OS segmentos acima podem formar um triangulo !')
    if r1 == r2 == r3:
    print('EQUILATERO')
    elif r1 != r2 != r3 != r1:
    print('ESCALENO')
    else:
    print('ISOCELES')
else:
    print('Os segmentos acima não podem formar triangulo!')       