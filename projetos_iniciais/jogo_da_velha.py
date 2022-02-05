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
        peça_player1 = "X"
        peça_player2 = "O"
        vez_de_jogar = 1 # 1 - player1  2 - player2
    else:
        peça_player1 = "O"
        peça_player2 = "X"
        vez_de_jogar = 2 # 1 - player1  2 - player2

    # Inicia o jogo
    p = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    velha = False
    vencedor = False
    while velha is False and vencedor is False:
        tabuleiro(p)
        if vez_de_jogar == 1:
            jogada = int(input(f'{player1}({peça_player1}) escolha um espaço: ')) 
            p[jogada - 1] = peça_player1
            vez_de_jogar = 2
        elif vez_de_jogar == 2:
            jogada = int(input(f'{player2}({peça_player2}) escolha um espaço: ')) 
            p[jogada - 1] = peça_player2 
            vez_de_jogar = 1
        
        velha = verifica_velha(p)


# As funções dentro da função 'jogar' para que ela funcione
def tabuleiro(list):
    """ Faz um print do tabuleiro do jogo da velha """
    return print(f'''
     {list[0]} | {list[1]} | {list[2]}
    ---|---|---
     {list[3]} | {list[4]} | {list[5]}
    ---|---|---
     {list[6]} | {list[7]} | {list[8]}
    ''')


def verifica_velha(list):
    """Verifica de o jogo deu velha"""    
    for item in list:
        if isinstance(item, int):
          return False
    return True

jogar()


