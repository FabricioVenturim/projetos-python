import editor_texto

def interface():
    """
    -> Função principal do programa: ela cria a interface e verifica se todos os arquivos foram adicionados com sucesso para chamar o módulo de aplicação das operações.

    return: sem return.
    """
    escolha = None
    arq_comandos = False #False - Arquivo não adicionado / True - Arquivo adicionado
    arq_conteudo = False #False - Arquivo não adicionado / True - Arquivo adicionado
    while escolha != 4:
        print("""
=-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-=
[ 1 ] Adicionar arquivo de comandos
[ 2 ] Adicionar arquivo de conteúdo
[ 3 ] Iniciar os comandos
[ 4 ] Sair
=-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-=
            """) # menu
        escolha = verifica_int("Escolha sua opção: ") #A função vai verificar se o número digitado é um int
        if escolha == 1:
            # Adicionar Arquivo de Comando 
            arquivo_comandos = str(input("Digite o nome do arquivo comando que você deseja: "))
            if verifica_existencia_arquivo(arquivo_comandos): #Se o verifica_existencia_arquivo verificar que não há o arquivo na pasta, o programa volta para o menu.
                arq_comandos = True #Agora que o arquivo foi adicionado, arq_comandos recebe True
                print(f"Arquivo {arquivo_comandos} adicionado com sucesso!")

        elif escolha == 2:
            # Adicionar Arquivo de Conteúdo
            arquivo_conteudo = str(input("Digite o nome do arquivo conteudo que você deseja: "))
            if verifica_existencia_arquivo(arquivo_conteudo):#Se o verifica_existencia_arquivo verificar que não há o arquivo na pasta ou o arquivo possui mais de 1000 caracteres, o programa volta para o menu.
                arq_conteudo = True #Agora que o arquivo foi adicionado, arq_conteudo recebe True
                print(f"Arquivo {arquivo_conteudo} adicionado com sucesso!")

        elif escolha == 3:
            # Primeiramente o programa irá analisar se há os dois arquivos para fazer as operações:
            if arq_comandos and arq_conteudo: #Se arq_comandos == True e arq_conteudo == True
                #Se ambos os arquivos estiverem adicionados, o programa perguntará o nome do arquivo registro e chamará as funções que criam os arquivos.
                nome_registro = str(input("Digite o nome do arquivo que você deseja registrar as operações (com a extensão): "))
                nome_registro = nome_registro.strip()
                if nome_registro == "": #Caso o usuário não escreva nada ou só escreva espaços em brancos, o programa cria um arquivo com um nome padrão (registro.txt).
                    nome_registro = "registro.txt"
                cria_registro(nome_registro)
                aplicar_arquivos(arquivo_comandos,arquivo_conteudo, nome_registro)
            elif arq_comandos: #Se faltar o arquivo de conteúdos
                print("Falta o Arquivo de conteúdo.")
            elif arq_conteudo: #Se faltar o arquivo de comandos
                print("Falta o Arquivo de comandos.")
            else: #Se faltar o arquivo de comandos e o arquivo de conteúdos
                print("Falta o Arquivo de comandos e o Arquivo de conteúdo.")
        elif escolha == 4: #Opção de fechar o programa
            break
        else:
            print("Por favor, escolha uma opção válida!")
    print("Obrigado, Volte Sempre!!")


def verifica_int(msg):
    """
    -> Verifica se o caracter passado no input é um int.
    :param msg: mensagem personalizada solicitando o usuário que digite um número inteiro

    :return: número inteiro
    """
    while True:
        try: #Ele tenta transformar a resposta do usuário em inteiro
            inteiro = int(input(msg))
        except: #Se houver erro, a looping continua até digitar um int
            print('ERRO! por favor, digite um inteiro válido!')

            print('''
=-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-=
[ 1 ] Adicionar arquivo de comandos
[ 2 ] Adicionar arquivo de conteúdo
[ 3 ] Iniciar os comandos
[ 4 ] Sair
=-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-==-=-=
            ''')
        else:
            break #Se ele tiver sucesso, o programa segue normalmente.
    return inteiro


def verifica_existencia_arquivo(arquivo):
    """
    -> Verifica se arquivo está na pasta do programa e se o arquivo possuí menos de 1000 de caracteres.
    :param arquivo: O arquivo para verificar se existe
    :return: False ou True
    """
    try: #O programa tenta abrir e fechar o arquivo que o usuário passou.
        teste = open(arquivo)
        teste.close()
    except:#Se não consegui, ele retorna falso e volta para o menu.
        print(f"O arquivo {arquivo} não foi encontrado na sua pasta.")
        return False
    else: 
        with open(arquivo, "r", encoding="utf-8") as conteudo:
            #Abre o arquivo e verifica se a quantidade de caracteres é no máximo 1000.
            conteudo = conteudo.read()
            tamanho_arquivo = len(list(conteudo))
            if tamanho_arquivo > 1000:
                print(f"Desculpe, o máximo permitido é de 1000 caracteres e o seu arquivo possuí {tamanho_arquivo}.")
                return False
            else:        
                return True


def aplicar_arquivos(arquivo_comanandos, arquivo_conteudo, arquivo_registro):
    """
    -> Função que abre os arquivos de comando e conteúdo e chama o módulo editor_texto para aplicar os comandos.
    :param arquivo_comanandos: Arquivo com as operações a serem executadas
    :param arquivo_conteudo: Arquivo com o conteúdo que será aplicado as operações
    :param arquivo_registro: Arquivo que será registrada as operações
    :return: Sem return
    """
    with open(arquivo_comanandos, "r", encoding="utf-8") as comandos:
        comandos = comandos.read()

    with open(arquivo_conteudo, "r", encoding="utf-8") as conteudo:
        conteudo = conteudo.read() 

    #Aqui chama a função aplica_comandos do módulo editor_texto.
    editor_texto.aplica_comandos(comandos,conteudo,arquivo_registro) #Encontra e aplica os comandos


def cria_registro(nome_registro): 
    """
    -> Função que cria um registro na pasta do programa
    :param nome_registro: Nome desejado para o arquivo
    :return: Sem return
    """
    with open(nome_registro, "a", encoding="utf-8") as registro:
        registro.write("") #Ao tentar abrir um arquivo que não existe, o python cria esse arquivo na pasta do programa

