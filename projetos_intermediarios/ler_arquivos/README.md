Repositório original: https://github.com/FabricioVenturim/ler-edita-arquivos

Para executar o programa, é necessário apenas rodar o arquivo main.py da pasta. Ela chamará a função interface do módulo ler_arquivos.

## projeto:

### Parte 1:

Elaborar um módulo com funcionalidades para

(a) ler um arquivo texto de Comandos(com comandos para o programa executar) após solicitar o nome do arquivo ao usuário.

(b) ler um arquivo texto de Conteúdo(com o texto em que os comandos serão executados) após solicitar o nome do arquivo ao usuário, e

(c) registrar as operações realizadas pelo programa em um arquivo texto de Saída. A cada operação realizada, um registro deve ser adicionado ao arquivo com o comando executado, o horário de execução e o resultado obtido.
Este módulo também deve oferecer todas as funcionalidades da interface - possibilitando a interação do usuário com o programa.
	
### Parte 2:

Elaborar um módulo com funcionalidades para o reconhecimento de comandos no arquivo texto de Comandos e a execução destes comandos no arquivo texto de Conteúdo. O arquivo texto de Conteúdo pode possuir QUALQUER caractere padrão da língua portuguesa, mas não é necessário que o conteúdo faça sentido linguístico. O tamanho máximo do conteúdo é de 1000 caracteres, mas não existe tamanho mínimo. os comandos são:
- Agrupar - Remove todos os espaços em branco do arquivo de Conteúdo e imprime o resultado.
- Maior - Imprime a maior palavra encontrada no arquivo de Conteúdo, mesmo que a palavra não faça sentido linguístic.
- Buscar <Texto> - imprime todas as linhas do arquivos de Conteúdo em que <Texto> é encontrado. 
- Contar <Texto> - Exibe a quantodade de vezes em que <texto> ocorre no arquivo de Conteúdo.
- Substituir <Texto_antigo><Texto_novo> - Substitui todo trecho de texto encontrado que corresponda ao primeiro parâmetro pelo texto fornecido no segundo parâmetro.
- Preguiça - Remove todas as palavras com comprimento maior que 4 caracteres e imprime o resultado.


## Coisas interessantes do módulo ler_arquivo:
  
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
  
