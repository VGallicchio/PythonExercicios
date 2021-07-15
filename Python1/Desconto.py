#programa que preco do produto e mostre seu novo preco com 5% de desconto

produto = float(input('Digite o preço do produto R$'))
novo = produto - (produto*0.05) #pode fazer % num / 100

print('Um produto que custa {} R$ custará {:.2f} R$ com 5% de desconto '.format(produto, novo))