#34-Escreva um programa que Leia o salario, calcule seu valor de aumento.
#Salarios acima de 1250, calcular aumento de 10%
#Salarios menores ou iguais aumento de 15%

sal = float(input('Qual o salario do funcionário ?'))

if (sal > 1250):
    aumento = (sal*0.1)+sal
    print('O Salário reajustado será de  {} R$ '.format(aumento))
else:
    aumento = (sal*0.15)+sal
    print('O Salário reajustado será de  {} R$ '.format(aumento))
    