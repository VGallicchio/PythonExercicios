import os
import requests
import json
import time

# Carrega os dados para dentro da variável
# Para que possam ser manipulados
# Cria o arquivo e escreve o nome do repositório em cada linha

#Função ler o usuário e criar o json com os repos.
def request_api(usuario):
    if not os.path.exists("python-requests/GitUser"):
        try:
            os.makedirs("python-requests/GitUser")
        except Exception as e:
            print(e)
            raise
    #Utilizando a api para o requests.get
    request = requests.get(f'https://api.github.com/users/{usuario}/repos')
    #Validação de existencia.
    if request.status_code == 404:
        return print("Usuário Inexistente")
    else: 
        #Load content dos dados e gravando o arquivo.
        dados = json.loads(request.content)

        #Atenção ao caminho do seu projeto p/funcionar corretamente.
        with open(os.path.join("python-requests/GitUser", f"{usuario}.txt"), 'w') as arquivo:     
            for i in dados:
                arquivo.write('\n')
                json.dump("Repo: " + i['name'] + "  " + "Link:  " + i['html_url'], arquivo)

        return print('Arquivo criado com sucesso')

#Função para ler os arquivos criados.
def listando_arquivos():
        #Especifica o nome do dir do seu projeto.
        path_to_files = 'python-requests/GitUser'
        files = [pos_file for pos_file in os.listdir(path_to_files) if pos_file.endswith('.txt')] 
        return print(files)
