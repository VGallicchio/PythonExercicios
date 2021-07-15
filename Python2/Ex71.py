'''71 - Crie um programa que simule o funcionamento de um caixa eletronico. No inicio pergunte ao usuário qual
será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.

Observação: considere que o caixa só tem notas de 50,20,10 e 1 real.
'''
print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        if totced == 0:
            break
print('=' * 30)
print('VOLTE SEMPRE ao BANCO CEV! TENHA UM BOM DIA!')
