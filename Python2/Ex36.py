''' 36 - Escreva um programa para aprovar um empréstimo bancário para compra de uma casa. 
O programa vai pergntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então
o empréstimo será negado'''

print('-='*20)
print('Analisador de finânciamento bancário')
print('-='*20)
nome = str(input('Nome completo do Comprador: ')).strip()
valor = float(input('Qual valor do imóvel a ser financiado? '))
sal = float(input('Qual o salário atual do senhor {} ! '.format(nome)))
parcela = float(input('O senhor {} vai se propor a pagar em quantos anos? '.format(nome)))
print('-='*20)
mensalidade = valor / (parcela * 12)
aval = sal * 0.3
print('Para pagar uma casa de RS {:.2f} em {} anos, a prestação será de {:.2f} RS Mensais'.format(valor, parcela, mensalidade))

if mensalidade <= aval:
    print('Empréstimo imobiliário Aprovado')
else:
    print('Empréstimo imobiliário Negado')
