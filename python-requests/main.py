from functions import *

#Interface para criar os arquivos, listar ou terminar o programa.
while True:
    try:
        op = int(input('''
        [1] - Inserir Usuário GIT:
        [2] - Listagem dos Usuários:
        [3] - Abrir listagem:
        [4] - Sair
        Insira a opção: '''))
        if op == 1:
            usuario = input('Insira o seu usuário do github: ')
            request_api(usuario)
            time.sleep(2)
        elif op == 2:
            listando_arquivos()
        elif op == 3:
            f = input("Insira o usuário para listar GitRepo: ")
            try:
                f = open("python-requests/GitUser/"+f+".txt")
                #f = open('python-requests/'+f+'.txt')
                file_contents = f.read()
                print(file_contents)
                f.close()
            except:
                print('O arquivo não existe!')
        elif op == 4:
            break
        else:
            print('Opção inválida digite novamente: ')
    
    except:
        print('Operação inexistente tente de novo!')
print('FIM')
