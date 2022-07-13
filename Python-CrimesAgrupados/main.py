from functions import *
import csv
#Abrindo csv, depois mapeando com um for tudo que está na região e depois dando append a uma lsita.
#Atenção ao caminho do seu projeto p/funcionar corretamente.
with open("python-crimes-agrupados/reccrimepfa-210901-151708.csv","r") as df:
    crimes = csv.reader(df,skipinitialspace=True)
    regions = list()
    for [data, pfa, region, crime, total] in crimes: 
        resultado = False        
        if not regions:
            regions.append(region)
        else:
            for r in regions:
                if r == region:
                    resultado = True
                    break
            if resultado == False:
                regions.append(region)

    #print("Testando lista regioes")
    #print(regions)
    regions.remove('Region')
    
    #Adcionando a lista de regiões a um dicionário, criando chaves a partir deles (fromkeys)
    add_dict = dict.fromkeys(regions)
    
    #print("=================================================Testando mapeamento fromkeys=================================================")
    #print(add_dict)
    
    #Criando for para o dicionário dicionário aonde vamos contar os crimes > 10.
    for r in add_dict:
        add_dict[r] = dict()
        add_dict[r]['DATA'] = data_processamento() #Chama a função do processamento de data.
        add_dict[r]['region'] = r
        add_dict[r]['crimes'] = list()
        
        #Atenção ao caminho do seu projeto p/funcionar corretamente.
        with open("python-crimes-agrupados/reccrimepfa-210901-151708.csv","r") as df:
            crimes = csv.reader(df,skipinitialspace=True)
            
            #print('========================DIC DENTRO DO FOR===========================')
            #print(add_dict)
            
            #Mapeando e filtrando os crimes.
            for [data, pfa, region, crime, total] in crimes: 
                resultado = False
                if region == r:
                    #Usando a função de criar um dicionário no laço cada crime > 10 terá um append e vai criar um dicionário dentro do laço. 
                    if not add_dict[r]['crimes'] and int(total) > 10:
                        add_dict[r]['crimes'].append(dicionarios_crimes(crime,total))
                    else:
                        for c in add_dict[r]['crimes']:
                            if c['crime'] == crime:
                                c['count'] = int(total) + int(c['count'])
                                resultado = True
                        if resultado == False and int(total) > 10:
                                #Append na contagem de crimes > 10, criando dicionários.
                                add_dict[r]['crimes'].append(dicionarios_crimes(crime,total))
            
#Plotando dados (caminho, nome do arquivo, dados para exportar)
plot_json('python-crimes-agrupados/Resultado', 'Crimes.json', add_dict)
print("Resultados criados com sucesso")
