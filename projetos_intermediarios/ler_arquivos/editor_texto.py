import re
from datetime import datetime

#============================================================================#
# Função principal onde todos as funções do método editor_texto se encaixam. # 
#============================================================================#
def aplica_comandos(comandos, conteudo, arquivo_registro): 
    """
    -> Função principal do módulo editor_texto: verifica a presença das operações no arquivo comandos e aplica, caso encontre, as operações no arquivo de conteúdo e registra em um arquivo de saída.
    :param comandos: Arquivo que contenha os comandos.
    :param conteudo: Arquivo que contenha os conteúdos.
    :param arquivo_registro: Arquivo de saída que será registrada as operações.
    :return: Sem return.
    """
    lista_palavras = comandos.split() #Trasnforma o arquivo comandos em uma lista com cada palavra.
    contador = 1
    #Verifica palavra por palavra se há uma operação válida a ser executada.
    for palavra in lista_palavras: 
        if contador == len(lista_palavras): #Se a palavra analisada for a última do texto, as operações Buscar, Contar e Substituir não poderão ser aplicadas, visto que não haverá parametro para elas.
            verifica_agrupar(palavra, conteudo, arquivo_registro)
            verifica_maior(palavra, conteudo, arquivo_registro)
            verifica_preguica(palavra, conteudo, arquivo_registro)
            
        elif contador == len(lista_palavras) - 1: #Se a palavra analisada for a penúltima do texto, a operação Substituir não poderá ser aplicada, visto que não haverá o segundo parametro para ela.
            palavra_parametro_1 = lista_palavras[contador] #Algumas operações necessitam de um parâmetro para serem executadas, no caso a próxima palavra da lista.
            verifica_agrupar(palavra, conteudo, arquivo_registro)
            verifica_maior(palavra, conteudo, arquivo_registro)
            verifica_preguica(palavra, conteudo, arquivo_registro)
            verifica_buscar(palavra, palavra_parametro_1, conteudo, arquivo_registro)
            verifica_contar(palavra, palavra_parametro_1, conteudo, arquivo_registro)     
        else:
            palavra_parametro_1 = lista_palavras[contador]
            palavra_parametro_2 = lista_palavras[contador + 1] #A operação Substituir necessita de 2 parâmetros para ser execultada, ou seja, as duas próximas palavras da lista.
            verifica_agrupar(palavra, conteudo, arquivo_registro)
            verifica_buscar(palavra, palavra_parametro_1, conteudo, arquivo_registro)
            verifica_maior(palavra, conteudo, arquivo_registro)
            verifica_preguica(palavra, conteudo, arquivo_registro)
            verifica_contar(palavra, palavra_parametro_1, conteudo, arquivo_registro)
            verifica_substituir(palavra, palavra_parametro_1, palavra_parametro_2, conteudo, arquivo_registro)
        contador+=1     
    print(f"Arquivo {arquivo_registro} criado e escrito com sucesso!")

#======================================================================================#
# Funções para verificar e aplicar os comandos do arquivo comandos no aquivo conteudo. #
#======================================================================================#
def verifica_agrupar(texto_comando, texto_conteudo, nome_registro):
    """
    -> Função que verifica se existe a operação Agrupar e, caso exista, aplica e registra o resultado no arquivo solicitado.
    :param texto_comando: texto para verificar a presença da operação.
    :param texto_conteudo: Arquivo para aplicar a operação.
    :param arquivo_registro: Arquivo de saída que será registrada a operação.

    :return: Sem return
    """
    padrao = re.compile(r".*Agrupar$") #Verifica se o Agrupar está no texto passado
    if re.fullmatch(padrao, texto_comando): 
        texto = agrupar(texto_conteudo) #Chama a função agrupar
        horario = horario_execucao() #Mostra o horário da execução
        registrar(nome_registro,texto,"Agrupar",horario) #Chama a função registrar e registra os resultados no arquivo de saída.

def verifica_maior(texto_comando, texto_conteudo, nome_registro):
    """
    -> Função que verifica se existe a operação Maior e, caso exista, aplica e registra o resultado no arquivo solicitado.
    :param texto_comando: texto para verificar a presença da operação.
    :param texto_conteudo: Arquivo para aplicar a operação.
    :param arquivo_registro: Arquivo de saída que será registrada a operação.
    
    :return: Sem return
    """
    padrao = re.compile(r".*Maior$") #Verifica se o Maior está no texto passado
    if re.fullmatch(padrao, texto_comando):
        texto = maior(texto_conteudo) #Chama a função Maior
        horario = horario_execucao() #Mostra o horário da execução
        registrar(nome_registro,texto,"Maior",horario)#Chama a função registrar e registra os resultados no arquivo de saída.


def verifica_buscar(texto_comando, palavra_buscar, texto_conteudo, nome_registro):
    """
    -> Função que verifica se existe a operação Buscar e, caso exista, aplica e registra o resultado no arquivo solicitado.
    :param texto_comando: texto para verificar a presença da operação.
    :param palavra_buscar: a palavra a ser buscada no texto.
    :param texto_conteudo: arquivo para aplicar a operação.
    :param arquivo_registro: arquivo de saída que será registrada a operação.

    :return: Sem return.
    """
    padrao = re.compile(r".*Buscar$") #Verifica se o Buscar está no texto passado
    if re.fullmatch(padrao, texto_comando):
        texto = buscar(palavra_buscar, texto_conteudo) #Chama a função Buscar
        horario = horario_execucao() #Mostra o horário da execução
        registrar(nome_registro,texto,"Buscar", horario, palavra_buscar)#Chama a função registrar e registra os resultados no arquivo de saída.


def verifica_contar(texto_comando, palavra_contar, texto_conteudo, nome_registro):
    """
    -> Função que verifica se existe a operação Contar e, caso exista, aplica e registra o resultado no arquivo solicitado.
    :param texto_comando: texto para verificar a presença da operação.
    :param palavra_contar: a palavra a ser contada no texto.
    :param texto_conteudo: Arquivo para aplicar a operação.
    :param arquivo_registro: Arquivo de saída que será registrada a operação.

    :return: Sem return.
    """
    padrao = re.compile(r".*Contar$") #Verifica se o Contar está no texto passado
    if re.fullmatch(padrao, texto_comando):
        texto = contar(palavra_contar, texto_conteudo) #Chama a função Contar
        horario = horario_execucao() #Mostra o horário da execução
        registrar(nome_registro,texto,"Contar",horario, palavra_contar) #Chama a função registrar e registra os resultados no arquivo de saída.


def verifica_substituir(texto_comando, palavra_antiga, palavra_nova, texto_conteudo, nome_registro):
    """
    -> Função que verifica se existe a operação Substituir e, caso exista, aplica e registra o resultado no arquivo solicitado.
    :param texto_comando: texto para verificar a presença da operação.
    :param palavra_antiga: a palavra buscada no texto e a ser substituída no texto.
    :param palavra_nova: a palavra que substituirá a palavra antiga.
    :param texto_conteudo: arquivo para aplicar a operação.
    :param arquivo_registro: arquivo de saída que será registrado a operação.

    :return: Sem return.
    """
    padrao = re.compile(r".*Substituir$") #Verifica se o Substituir está no texto passado
    if re.fullmatch(padrao, texto_comando):
        texto = substituir(palavra_antiga, palavra_nova, texto_conteudo) #Chama a função Substituir
        horario = horario_execucao() #Mostra o horário da execução
        registrar(nome_registro,texto,"Substituir",horario, palavra_antiga, palavra_nova)#Chama a função registrar e registra os resultados no arquivo de saída.


def verifica_preguica(texto_comando, texto_conteudo, nome_registro):
    """
    -> Função que verifica se existe a operação Preguiça e, caso exista, aplica e registra o resultado no arquivo solicitado.
    :param texto_comando: texto para verificar a presença da operação.
    :param texto_conteudo: arquivo para aplicar a operação.
    :param arquivo_registro: arquivo de saída que será registrado a operação.

    :return: Sem return.
    """
    padrao = re.compile(r".*Preguiça$") #Verifica se o Preguiça está no texto passado
    if re.fullmatch(padrao, texto_comando):
        texto = preguica(texto_conteudo) #Chama a função Preguiça
        horario = horario_execucao() #Mostra o horário da execução
        registrar(nome_registro,texto,"Preguiça",horario)#Chama a função registrar e registra os resultados no arquivo de saída.

#===================================#
# Funções das operações solicitadas #
#===================================#

def buscar(palavra, conteudo):
    """
    -> Função que busca uma palavra em um texto e retorna as linhas nas quais a palavra buscada se encontra.
    :param palavra: Palavra buscada.
    :param conteudo: Texto conteúdo que a função irá procurar a palavra.
    
    :return: String com as linhas que a palavra buscada está presente.
    """
    documento = conteudo.splitlines() #Separa o texto por linhas
    linhas_com_busca=""
    for linha in documento:
        if palavra in linha: #Se a palavra buscada estiver na linha, ela será colocada no linhas_com_busca
            linhas_com_busca=linhas_com_busca+linha+"\n"
    return linhas_com_busca

def agrupar(conteudo):
    """
    -> Função que retira todos os espaços em branco do texto, deixando todas as palavras juntas.
    :param conteudo: O texto que deseja retirar os espaços.
    
    :return: String com a frase sem espaços.
    """
    lista_palavras = list(conteudo)
    while " " in lista_palavras: #Os dois while servem para ir tirando os espaços em branco e linhas vazias
        lista_palavras.remove(" ")
    while "\n" in lista_palavras:
        lista_palavras.remove("\n")
    frase_sem_espacos=""
    for i in lista_palavras:  #Adicionar cada letra dentro de uma string
        frase_sem_espacos += i
    return frase_sem_espacos 

def maior(conteudo):
    """
    -> Função que retorna a maior ou, se houver mais de uma palavra, as maiores palavras encontrada no texto
    :param conteudo: O texto que deseja procurar a(s) maior(es) palavras.
    
    :return: String com as maiores palavra encontradas separadas por " ".
    """
    texto = conteudo.split() 
    tamanho_palavra = list()
    for palavra in texto:
        tamanho_palavra.append(len(palavra))
    maior = max(tamanho_palavra) 
    maiores_palavras = ""
    for palavra, tamanho in zip(texto, tamanho_palavra): #Compara cada item correspondente da lista texto com o item da lista tamanho_palavra e, se o tamanho for igual ao maior, adiciona a palavra na string.
        if tamanho == maior:
            if palavra not in maiores_palavras: #Só adiciona a palavra se ela ainda não tiver sido adicionada. Isso arruma o erro da mesma palavra ser adicionada mais de uma vez caso apareça mais de uma vez no conteúdo. 
                maiores_palavras=maiores_palavras+palavra+" "
    return maiores_palavras

def contar(palavra, conteudo):
    """
    -> Função que conta a quantidade de vezes que a palavra foi encontrada no texto.
    :param palavra: Palavra que se deseja contar a quantidade de vezes que foi encontrada no texto.
    :param conteudo: Texto que se deseja procurar a palavra.

    :return: A quantidade de vezes que a palavra apareceu.
    """
    string = conteudo
    substring = palavra
    quantidade = string.count(substring) #Conta a quantidade de palavra(considerada uma substring) na string.
    return str(quantidade)

def substituir (palavra_antiga, palavra_nova, conteudo):
    """
    -> Função que substitui a palavra antiga pela palavra nova no texto de conteúdo.
    :param palavra_antiga: a palavra que se deseja substituir.
    :param palavra_nova: a palavra que substituirá a palavra antiga.
    :param conteudo: texto que se deseja substituir as palavras.

    :return: String com o texto substituído.
    """
    return conteudo.replace(palavra_antiga, palavra_nova)

def preguica(conteudo):
    """
    -> Função que retira todas as palavras com mais de 4 caracteres.
    :param conteudo: texto onde serão retiradas as palavras.

    :return: String com o texto sem as palavras com mais de 4 caracteres.
    """
    return re.sub(r"\S\S\S\S\S(\S)*", "", conteudo) #Substitui qualquer palavra de 5 ou mais caracteres por "".

#=============================================================#
# Função que disponibiliza o horário da execução da operação  #
#=============================================================#
def horario_execucao():
    """
    -> Função que retorna o horário do momento que ela é chamada.

    :return: Horário de execução.
    """
    horario_execucao = datetime.now()
    return horario_execucao.strftime("%d/%m/%y %H:%M:%S") #Formatação do horário e da data

#===============================================#
# Função que possibilita a escrita de registros #
#===============================================#
def registrar(nome_registro, texto_resultado, operação, horario, parametro_1="", parametro_2=""):
    """
    -> Função que registrará o texto resultado, a operação e o horário de execução em um arquivo de saída.
    :param nome_registro: nome do arquivo de saída para registrar as operações.
    :param texto_resultado: texto com o resultado.
    :param operação: operação realizada.
    :param horario: horario de execução da operação.
    :param parametro_1: Opcional, se a operação necessita de um parâmetro, ela será registrada junto com a operação.
    :param parametro_2: Opcional, se a operação necessita de um segundo parâmetro, ela será registrada junto com a operação.

    :return: sem return.
    """
    with open(nome_registro, "a", encoding="utf-8") as arquivo_registro:
        arquivo_registro.write(operação + " " + parametro_1 + " " + parametro_2 + " " + horario + "\n")
        arquivo_registro.write(texto_resultado + "\n")
        arquivo_registro.write("\n")

    