import json
import os
from datetime import datetime

#Função para criar dicionários.
def dicionarios_crimes(crime,total):
    add_dict_crimes = {'crime': crime, 'count': total}   
    
    return add_dict_crimes

#Função para retornar a data de processamento formatada.
def data_processamento():
    process_time = datetime.now()
    process_time = process_time.strftime("%d/%m/%Y %H:%M")

    return process_time

#Função para retirar os dados discrepantes < 2 e depois escrever a saida em um arquivo json.
def plot_json(target_path, target_file, data):
    #Cria diretorio para saida dos dados.
    if not os.path.exists(target_path):
        try:
            os.makedirs(target_path)
        except Exception as e:
            print(e)
            raise

    for i in list(dict(data)):
        if len(data[i]['crimes']) < 2:
            data.pop(i)

    with open(os.path.join(target_path, target_file), 'w') as f:
        for i in data:
            f.write('\n')
            json.dump(data[i], f)
