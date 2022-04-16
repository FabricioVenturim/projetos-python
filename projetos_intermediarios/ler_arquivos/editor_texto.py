import re
from datetime import datetime

#=======================================================================================
# Função principal onde todos as funções do método editor_texto se encaixam.
#=======================================================================================
def aplica_comandos(comandos, conteudo, arquivo_registro): 
    lista_palavras = comandos.split()
    contador = 1
    for palavra in lista_palavras: 
        if contador == len(lista_palavras):
            verifica_agrupar(palavra, conteudo, arquivo_registro)
            verifica_maior(palavra, conteudo, arquivo_registro)
            verifica_preguica(palavra, conteudo, arquivo_registro)
            
        elif contador == len(lista_palavras) - 1:
            palavra_parametro_1 = lista_palavras[contador]
            verifica_agrupar(palavra, conteudo, arquivo_registro)
            verifica_maior(palavra, conteudo, arquivo_registro)
            verifica_preguica(palavra, conteudo, arquivo_registro)
            verifica_buscar(palavra, palavra_parametro_1, conteudo, arquivo_registro)
            verifica_contar(palavra, palavra_parametro_1, conteudo, arquivo_registro)
                       
        else:
            palavra_parametro_1 = lista_palavras[contador]
            palavra_parametro_2 = lista_palavras[contador + 1]
            verifica_agrupar(palavra, conteudo, arquivo_registro)
            verifica_maior(palavra, conteudo, arquivo_registro)
            verifica_preguica(palavra, conteudo, arquivo_registro)
            verifica_buscar(palavra, palavra_parametro_1, conteudo, arquivo_registro)
            verifica_contar(palavra, palavra_parametro_1, conteudo, arquivo_registro)
            verifica_substituir(palavra, palavra_parametro_1, palavra_parametro_2, conteudo, arquivo_registro)
        contador+=1     
    print(f"Arquivo {arquivo_registro} criado e escrito com sucesso!")

#=======================================================================================
# Funções para verificar e aplicar os comandos do arquivo comandos no aquivo conteudo.
#=======================================================================================
def verifica_agrupar(texto_comando, texto_conteudo, nome_registro):
    padrao = re.compile(r".*Agrupar.*")
    if re.fullmatch(padrao, texto_comando): 
        texto = agrupar(texto_conteudo)
        horario_execucao = datetime.now()
        horario_execucao_arrumado = horario_execucao.strftime("%d/%m/%Y %H:%M:%S")
        registrar(nome_registro,texto,"Agrupar",horario_execucao_arrumado)


def verifica_maior(texto_comando, texto_conteudo, nome_registro):
    padrao = re.compile(r".*Maior.*")
    if re.fullmatch(padrao, texto_comando):
        texto = maior(texto_conteudo)
        horario_execucao = datetime.now()
        horario_execucao_arrumado = horario_execucao.strftime("%d/%m/%Y %H:%M:%S")
        registrar(nome_registro,texto,"Maior",horario_execucao_arrumado)


def verifica_buscar(texto_comando,palavra_parametro, texto_conteudo, nome_registro):
    padrao = re.compile(r".*Buscar$")
    if re.fullmatch(padrao, texto_comando):
        texto = buscar(palavra_parametro, texto_conteudo)
        horario_execucao = datetime.now()
        horario_execucao_arrumado = horario_execucao.strftime("%d/%m/%Y %H:%M:%S")
        registrar(nome_registro,texto,"Buscar",horario_execucao_arrumado)


def verifica_contar(texto_comando, palavra_parametro, texto_conteudo, nome_registro):
    padrao = re.compile(r".*Contar$") 
    if re.fullmatch(padrao, texto_comando):
        texto = contar(palavra_parametro, texto_conteudo)
        horario_execucao = datetime.now()
        horario_execucao_arrumado = horario_execucao.strftime("%d/%m/%Y %H:%M:%S")
        registrar(nome_registro,texto,"Contar",horario_execucao_arrumado)


def verifica_substituir(texto_comando, palavra_parametro, palavra_parametro_2, texto_conteudo, nome_registro):
    padrao = re.compile(r".*Substituir$")
    if re.fullmatch(padrao, texto_comando):
        texto = substituir(texto_conteudo, palavra_parametro, palavra_parametro_2)
        horario_execucao = datetime.now()
        horario_execucao_arrumado = horario_execucao.strftime("%d/%m/%Y %H:%M:%S")
        registrar(nome_registro,texto,"Substituir",horario_execucao_arrumado)


def verifica_preguica(texto_comando, texto_conteudo, nome_registro):
    padrao = re.compile(r".*Preguiça.*")
    if re.fullmatch(padrao, texto_comando):
        texto = preguica(texto_conteudo)
        horario_execucao = datetime.now()
        horario_execucao_arrumado = horario_execucao.strftime("%d/%m/%Y %H:%M:%S")
        registrar(nome_registro,texto,"Preguiça",horario_execucao_arrumado)

#=======================================================================================
# Funções das operações solicitadas
#=======================================================================================
def buscar(palavra, conteudo):
    documento = conteudo.splitlines()
    lista_de_linhas=[]
    for linha in documento:
        if re.search(palavra, linha):
            lista_de_linhas.append(linha)
    linhas_com_busca=""
    for item in lista_de_linhas:
        linhas_com_busca=linhas_com_busca+item+"\n"  #Arrumar depois
    return linhas_com_busca

def agrupar(frase):
    lista_palavras = list(frase)
    while " " in lista_palavras:
        lista_palavras.remove(" ")
    while "\n" in lista_palavras:
        lista_palavras.remove("\n")
    frase_sem_espacos=""
    for i in lista_palavras:  #Adicionar cada letra dentro de uma string
        frase_sem_espacos += i
    return frase_sem_espacos 

def maior(conteudo):
    texto = conteudo.split()
    tam_palavras = list()
    for palavra in texto:
        tam_palavras.append(len(palavra))

    maior = max(tam_palavras)
    maiores_palavras = ""
    for a, b in zip(texto, tam_palavras):
        if b == maior:
            maiores_palavras=maiores_palavras+a+" "
    return maiores_palavras

def contar(palavra, conteudo):
    string = conteudo
    substring = palavra
    quantidade = string.count(substring)
    return str(quantidade)

def substituir (conteudo, palavra_antiga, palavra_nova):
    return conteudo.replace(palavra_antiga, palavra_nova)

def preguica(conteudo):
    return re.sub(r"\S\S\S\S\S(\S)*", "", conteudo) 

#=======================================================================================
# Funções que possibilitam a criação e escrita de registros
#=======================================================================================
def registrar(nome_registro, texto_resultado, operação, horario):
    with open(nome_registro, "a", encoding="utf-8") as arquivo_registro:
        arquivo_registro.write(operação + horario + "\n")
        arquivo_registro.write(texto_resultado)
        arquivo_registro.write("\n")


