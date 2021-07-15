#programa que mostre o salario de um func e mostre seu novo sal como 15% de aumento

salario = float(input('Digite o salario em R$'))
novo = salario + (salario*0.15) #pode fazer % num / 100

print('Um funcionário que ganhava {} R$ com 15% de aumento irá receber {:.2f} R$'.format(salario, novo))