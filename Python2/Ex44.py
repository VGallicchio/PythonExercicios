''' 44 - Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
e condição de pagamento:

- á vista dinheiro/cheque: 10% da descono
- á vista no cartão: 5% de desconto 
- aem até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros  '''
('-='*11)
print('{:=^40}'.format(' Juros Parcelamento ')
('-='*11)

val = float(input('Qual o valor a ser pago:  R$' ))

print('''Digite sua opção de pagamento
[1] - À vista dinheiro/cheque:
[2] - Parcelado no Cartão''')
op = int(input('Qual opção desejada'))

if op == 1:
    preco = (val * 0.1) - val
    print('O Valor a ser pago será com 10% de desconto, e ficará no total de {:.2f} R$ '.format(preco))
elif op == 2:
    np = int(input('Em quantas vezes será parcelado no cartão ? '))
    if np == 1:
    preco = (val * 0.05) - val
    print('O Valor a ser pago será com 5% de desconto, e ficará no total de {:.2f} R$ '.format(preco))
    if np == 2:
    print('O Valor a ser pago será no total de {} R$ '.format(val))
    if np > 2:
    preco = (val * 0.2) + val
    print('O Valor a ser pago será com 20% de acrescimo, e ficará no total de {:.2f} R$ '.format(preco))    
else:
    print('Opção invalida')
