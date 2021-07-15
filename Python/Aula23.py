'''
Aula 23 - Tratamento de erros.
Nesta aula foi abordado os vários tipos de erros que podem ocorrer
e queles aparecem como exceção no python.

Então foi abordado como funciona o try dentro de python.


try:
	operação. #o que geralmente pode dar problemas, comandos etc..

except:
	falhou #o que vai acontecer quando falhar e se falar o try.

Todo try pode ter vários except dentro dele, eles ajudam muito ao programar para saber
onde estao os erros e como tratalos.
por exemplo.
try:
	operacao
except TypeError:
	falhou
except ValueError:
	falhou
except OSError:
	falhou
else:
	deu certo
finally
	certo/falha
'''
#caso ele de erro, vai aparecer o erro da exce do python e o erro denominado no except.
try:
	a = int(input('Numerador: '))
	b = int(input('Denominador: '))
	r = a / b
except:
	print('Infelizmente tivemos um problema :(')
else: # o else para caso se rodar sem problemas., com o else não aparece msg de problema do python.
	print(f'O resultado é {r}')

#Finally

try:
	a = int(input('Numerador: '))
	b = int(input('Denominador: '))
	r = a / b
except Exception as erro:
	print('Problema encontrado foi {erro.__class__}') # Nesse caso podemos tratar o except exatamente como o erro do python. E ainda tratar como erro de class como erro de valor etc..etc...
else: 
	print(f'O resultado é {r}')
finally:
	print(f'Volte sempre! Muito obrigado!') # Vai finalizar independente de erro ou não.

#Vários except

try:
	a = int(input('Numerador: '))
	b = int(input('Denominador: '))
	r = a / b
except (ValueError, TypeError):
	print('Problema com tipos de dados')
except ZeroDivisionError):
	print('Problema n pode dividir por zero') 	
else: 
	print(f'O resultado é {r}')
finally:
	print(f'Volte sempre! Muito obrigado!') # Vai finalizar independente de erro ou não.

