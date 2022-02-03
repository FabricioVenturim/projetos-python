# O jogador deverá escolher o número máximo do interválo da adivinhação
# O computador escolherá um número aleatório entre 0 e o número máximo
# a tarefa do jogador é adivinhar o número com base nas dicas do computador 
from random import randint

# O jogador deverá escolher o número máximo do interválo da adivinhação
num_max = int(input('Escolha o valor máximo do interválo: '))

# O computador escolherá um número aleatório entre 0 e o número máximo
num_do_computador = randint(0, num_max)

# a tarefa do jogador é adivinhar o número com base nas dicas do computador 
tentativas_jogadas = 0
tentativas_permitidas = int((num_max / 10) + 1)

num_do_jogador = None
while tentativas_jogadas < tentativas_permitidas and num_do_jogador != num_do_computador :
    print('=================================================')
    print(f'Você tem {tentativas_permitidas - tentativas_jogadas} tentativas.')
    print('=================================================')
    num_do_jogador = int(input(f'Escolha um número entre 0 e {num_max}: '))
    tentativas_jogadas += 1

    if num_do_jogador < num_do_computador:
        print('Errado!')
        print('Tente um número maior')
    elif num_do_jogador > num_do_computador:
        print('Errado!')
        print('Tente um número menor')
        
if num_do_jogador == num_do_computador:
    print('Parabéns, você acertou o número!!!')
    print(f'Você utilizou {tentativas_jogadas} de {tentativas_permitidas} tentativas.')
elif tentativas_jogadas == tentativas_permitidas:
        print('Sinto muito, suas tentativas acabaram...')
