'''
Ex 99 - Faça um programa que tenha uma função chamada maior(), que receba vários parametros com valoeres inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''

def maior(* num):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')

#Programa
maior(5, 7, 3, 1, 4)
maior(8, 4, 7)
maior(1, 2)
maior(6)
maior()

#Programa usando MAX para pegar maior valor.
def maior(* num):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor}, ', end='')
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {max(num)}')


#Programa
maior(5, 7, 3, 1, 4)
maior(8, 4, 7)
maior(1, 2)
maior(6)
maior(0)#Com o max é importante não deixar celulas vazias para analisar se nãod a erro.
