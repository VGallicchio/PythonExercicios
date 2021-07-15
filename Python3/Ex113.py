'''
Ex 113 - Reescreva a função leiaInt() que fizemos no desafio 104, incluindo
agora a possibilidade da digitação de um numero de tipo inválido.
Aproveite e crie também a função leiaFloat() com a mesma funcionalidade.
'''

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mErro! Digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n

def leiaInt(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mErro! Digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


# Programa principal
n1 = leiaInt('Digite um número Inteiro: ')
n2 = leiaInt('Digite um número Real: ')
print(f'O numero inteiro foi {n1} e o real foi {n2}')
