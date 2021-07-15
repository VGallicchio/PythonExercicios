'''
Ex 105 - Faça um programa que tenha uma função notas(), que pode receber váris notas de alunos
e vai retornar um dicionário com as seguintes informações:
- Quantidade de notas:
- A menor nota:
- A média da turma:
- A situação(opcional)
Adcione tambem as docstrings da função.
'''


def notas(*n, sit=False):
    """
	-> Função para analisar notas e situações de vários alunos.
	:param n: uma ou mais notas dos alunos (aceita várias)
	:param sit: valor opcional, indicando se deve ou não adcionar a situação
	:return: dicionário com várias informações sobre a situação da turma.
	"""
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['Situação'] = 'BOA'
        elif r['média'] >= 5:
            r['Situação'] = 'RAZOÁVEL'
        else:
            r['Situação'] = 'RUIM'
    return r


# Programa principal
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)
