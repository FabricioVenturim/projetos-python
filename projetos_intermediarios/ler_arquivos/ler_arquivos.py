#Opções de interface 
#solicitar ao usuário o nome do arquivo comandos
#solicitar ao usuário o nome do arquivo texto de conteúdo
#registrar as operações realizadas pelo programa em um arquivo texto saída.
    #registro com o comando executado,
    #horário de execução e
    #resultado obtido.

#Opções de interface 
    #1 - Adicionar arquivo de comandos
    #2 - Adicionar arquivo de conteúdo
    #3 - Iniciar os comandos
    #4 - Sair
import editor_texto

def interface():
    escolha = None
    arq_comandos = False #False - Arquivo não adicionado / True - Arquivo adicionado
    arq_conteudo = False #False - Arquivo não adicionado / True - Arquivo adicionado
    while escolha != 4:
        print("""
            [ 1 ] Adicionar arquivo de comandos
            [ 2 ] Adicionar arquivo de conteúdo
            [ 3 ] Iniciar os comandos
            [ 4 ] Sair
            """) # menu
        escolha = verifica_int("Escolha sua opção: ")
        if escolha == 1:
            # Adicionar Arquivo de Comando
            arquivo_comandos = str(input("Digite o nome do arquivo comando que você deseja: "))
            if verifica_existencia_arquivo(arquivo_comandos):
                arq_comandos = True #Agora que o arquivo foi adicionado, arq_comandos recebe True
                print(f"Arquivo1 {arquivo_comandos} adicionado com sucesso!")

        elif escolha == 2:
            # Adicionar Arquivo de Conteúdo
            arquivo_conteudo = str(input("Digite o nome do arquivo conteudo que você deseja: "))
            if verifica_existencia_arquivo(arquivo_conteudo):
                arq_conteudo = True #Agora que o arquivo foi adicionado, arq_conteudo recebe True
                print(f"Arquivo {arquivo_conteudo} adicionado com sucesso!")

        elif escolha == 3:
            # Iniciando a aplicação dos comandos no arquivo conteúdo
            if arq_comandos and arq_conteudo:
                nome_registro = str(input("Digite o nome do arquivo que você deseja registrar as operações (com a extensão): "))
                cria_registro(nome_registro)
                aplicar_arquivos(arquivo_comandos,arquivo_conteudo, nome_registro)
            elif arq_comandos:
                print("Falta o Arquivo de conteúdo.")
            elif arq_conteudo:
                print("Falta o Arquivo de comandos.")
            else:
                print("Faltam os Arquivos de comandos e os Arquivos de conteúdo.")
        elif escolha == 4: #quer mesmo sair?
            break
        else:
            print("Por favor, escolha uma opção válida!")
    print("Obrigado, Volte Sempre!!!!")

def verifica_int(msg):
    while True:
        try: #Ele tenta transformar a resposta do usuário em inteiro
            inteiro = int(input(msg))
        except: #Se houver erro, a looping continua até digitar um int
            print('ERRO! por favor, digite um inteiro válido!')

            print('''
            [ 1 ] Adicionar arquivo de comandos
            [ 2 ] Adicionar arquivo de conteúdo
            [ 3 ] Iniciar os comandos
            [ 4 ] Sair
            ''')
        else:
            break #Se ele tiver sucesso, o programa segue normalmente
    return inteiro

def verifica_existencia_arquivo(arquivo):
    try:
        teste = open(arquivo)
        teste.close()
    except:
         print(f"O arquivo {arquivo} não foi encontrado na sua pasta.")
         return False
    else: 
        return True

def aplicar_arquivos(arquivo_comanandos, arquivo_conteudo, arquivo_registro):
    with open(arquivo_comanandos, "r", encoding="utf-8") as comandos:
        comandos = comandos.read()

    with open(arquivo_conteudo, "r", encoding="utf-8") as conteudo:
        conteudo = conteudo.read() 

    editor_texto.aplica_comandos(comandos,conteudo,arquivo_registro) #Encontra e aplica os comandos e por fim  

def cria_registro(nome_registro):
    with open(nome_registro, "a", encoding="utf-8") as registro:
        registro.write("")


interface()
