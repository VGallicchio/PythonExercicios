
''' 37 - Escreva um programa que leia um número inteiro qualquer e peça oara o usuário escolher qual
será a base de conversão
- 1 para Binário
- 2 para Octal
- 3 para Hexadecimal 
O python já tem conversores dentro de sua estruturas bin = binário, oct - octal, hex = hexadecimal. 
O python exibe uma codificação antes dos numeros convertidos 0b,etc: para fazer isso basta tratar 
como vai aparecer na programação, para aparecer a partir da 2 posição excluindo o 0b por exemplo.
'''


print('-='*20)
print('Base de conversão')
print('-='*20)
n = int(input('Digite um numero inteiro')).strip()

print('-='*20)
print(''' Escolha uma das bases para conversão:
1 - Conversão Para Binário 
2 - Conversão para Octal
3 - Coversão para Hexadecimal''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print(' {} convertido para Binário é igual a {} '.format(n, bin(n)[2:]))
elif opcao ==2:
    print(' {} convertido para Octal é igual a {} '.format(n, oct(n)[2:]))
elif opcao == 3:
    print(' {} convertido para Hexadecimal é igual a {} '.format(n, hex(n)[2:]))
else:
    print('Opção inválida')
