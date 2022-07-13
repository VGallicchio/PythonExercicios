import functools

#Criando o generator na memória, linha a linha.
#Atenção ao caminho do seu projeto p/funcionar corretamente.
arquivo = "python-prog-funcional/reccrimepfa-210901-151708.csv" 
arquivo = (row for row in open(arquivo))

#Testando endereço de memória do arquivo.
#print(arquivo)

#Cria um separador para as colunas.
linhas_arquivo = (s.rstrip().split(',') for s in arquivo)

#Cria os headers.
cols = next(linhas_arquivo)

# Converte cada linha para um dicionário com as chaves 'cols', que criamos os headers.
#dicionario = (dict(zip(cols, dados)) for dados in linhas_arquivo)
dicionario = (dict(map(lambda x,y: (x,y), cols, data)) for data in linhas_arquivo)

#Filtrando os anos [6:10], fatia a string pra pegar os últimos 4 digitos das datas q estão: 03/01/2003, pegando só o ano.
anos_filtro = filter(lambda year: int(year['12 months ending'][6:10])>2012, dicionario)

# Reduce, para somar baseado no filtro de anos, dando o total de crimes a partir de 2012 setado no filtro.
total_crimes = functools.reduce(lambda soma, d: soma + int(d['Rolling year total number of offences']), anos_filtro, 0)

#Printando resultado do script:
print(f'A somatoria total do número de crimes à partir de 2012, foi de: {total_crimes}')
