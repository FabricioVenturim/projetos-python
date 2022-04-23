Para executar o programa, é necessário apenas rodar o arquivo main.py da pasta. Ela chamará a função interface do módulo ler_arquivos.

Coisas interessantes do módulo ler_arquivo:
    Há 4 opções para o usuário:
    
    [ 1 ] Adicionar arquivo de comandos
        O usuário deverá passar para o programa o arquivo com os comandos que ele deseja executar. O programa consegue verificar se o arquivo existe na pasta e retorna uma mensagem se encontrou ou não o arquivo e volta para o menu.

    [ 2 ] Adicionar arquivo de conteúdo
        O usuário deverá passar para o programa o arquivo com o conteúdo que ele deseja aplicar os comandos. O programa consegue verificar se o arquivo existe na pasta e retorna uma mensagem se encontrou ou não o arquivo e volta para o menu. Além disso, o programa verifica se o arquivo conteúdo possui no máximo 1000 caracteres e retorna uma mensagem de erro se o arquivo possuir mais.
    
    [ 3 ] Iniciar os comandos
        O programa só iniciará as operações se o arquivo de comandos e o arquivo de conteúdo tiverem sido adicionados, se não retornar qual arquivo falta para começar. Quando ambos os arquivos estiverem adicionados, o programa irá pedi um nome para o arquivo de registro. Se o usuário não digitar nada, o programa irá salvar "registro.txt" como padrão. 

    [ 4 ] Sair
        Ao clicar, o programa finaliza.

Após clicar em Iniciar os comandos(3), a função aplica_comandos será exucutada. Ela, primeiramente, verificará a presença das operações Agrupar, Buscar, Contar, Maior, Substituir e Preguiça no arquivo de comandos, chamando funções específicas de verificação para cada operação de acordo com a regra passada. Após encontrar, ela aplicará a operação e registrará no arquivo de saída. Portanto, as operações serão resgistradas na ordem que forem escritas no arquivo comandos. 
Após registrar, o programa volta para o menu.