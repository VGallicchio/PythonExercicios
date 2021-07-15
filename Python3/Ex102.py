'''
Ex 102 - Crie um programa que tenha uma função fatorial(), que receba dois parametros:
O primeiro que indique o numero a calcular e o outro chamado show, que será um valor lógico (opcional)
indicando se será mostrado ou não na tela o processo de calculo do fatorial.
'''

def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um numero.
    :para n: O número a ser calculado.
    :para show: (opcional) Mostrar ou Não a conta.
    :return: O valor do Fatorial de um número n.
    """

    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# Programa principal.
h = str(input('Precisa de ajuda? Para acessar o guia do usuário digite S/N: ')).upper().strip()[0]
if h == 'S':
    help(fatorial)
else:
    n = int(input('Digite um número para saber sem fatorial: '))
    op = str(input('Digite S/N - para mostrar sua base de calculo: ')).upper().strip()[0]
    if op == 'S':
        print(fatorial(n, show=True))
    elif op == 'N':
        print(fatorial(n, show=False))
    else:
        print('Operação inválida')
