# Jogo da Velha - a princípio 1x1 


def jogar():
    """Onde tudo funciona"""
    # Escolher os nomes dos jogadores
    player1 = str(input('Qual o nome do jogador 1: '))
    player2 = str(input('Qual o nome do jogador 2: '))

    # Escolher as peças dos jogadores
    peça_player1 = int(input(f'{player1}, Qual peça você deseja jogar? [1 - X | 2 - O ]: '))
    while peça_player1 != 1 and peça_player1 != 2:
        peça_player1 = int(input(f'''Desculpe {player1}, Você precisa escolher entre 1 e 2.
    Qual peça você deseja jogar? [1 - X | 2 - O ]: '''))
    if peça_player1 == 1:
        peças = {'X': player1 ,'O': player2}
    else:
        peças =  {'X': player2 ,'O': player1}
    
    # Inicia o jogo
    p = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    velha = False
    vencedor = False
    tabuleiro(p)

    while velha is False and vencedor is False:
        lista_de_espaços = espaços_disponíveis(p)

        for k, v in peças.items():
            jogada = int(input(f'{v}({k}) escolha um espaço: '))
            while jogada not in lista_de_espaços: 
                print('Por favor, digite um espaço válido!')
                jogada = int(input(f'{peças[v]}({k}) escolha um espaço: '))
            p[jogada - 1] = k
            tabuleiro(p)
            velha = verifica_velha(p)
            if velha is True:
                break
                
# As funções dentro da função 'jogar' para que ela funcione
def tabuleiro(lista):
    """ Faz um print do tabuleiro do jogo da velha """
    return print(f'''
     {lista[0]} | {lista[1]} | {lista[2]}
    ---|---|---
     {lista[3]} | {lista[4]} | {lista[5]}
    ---|---|---
     {lista[6]} | {lista[7]} | {lista[8]}
    ''')


def verifica_velha(lista):
    """Verifica de o jogo deu velha"""    
    for item in lista:
        if isinstance(item, int):
          return False
    return True


def espaços_disponíveis(lista):
    """ Atualiza e mostra os espaços disponíveis para os jogadores colocarem as peças"""
    lista_de_espaços = []
    for item in lista:
        if isinstance(item,int):
            lista_de_espaços.append(item)
    return lista_de_espaços


jogar()


