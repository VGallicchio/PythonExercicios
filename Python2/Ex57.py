    '''Ex 57 - Faça um programa que leia o sexo de uma pessoa,
más só aceite os valores M ou F. Caso esteja errado. peça 
digitação novamente até ter um valor correto'''

sexo = str(input('Digite seu Sexo M/F')).strip().upper()[0] #[0] pega só a primeira letra. fateamentro de string

while sexo not in 'MfFf':
    print('Sexo inexistente digite novamente')
    sexo = str(input('Digite seu Sexo M/F')).strip().upper()[0]
print('Sexo {}'.format(sexo))

'''
ATENÇÃO E COM AND NÃO OR.

sexo = str(input('Digite seu Sexo M/F')).strip().upper()

while sexo != 'M' and sexo != 'F':
    print('Sexo inexistente digite novamente')
    sexo = str(input('Digite seu Sexo M/F')).strip().upper()
print('Sexo {}'.format(sexo))


'''