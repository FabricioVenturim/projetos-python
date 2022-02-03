# O usuário deverá escolher uma quantidade de dados e o tipo de dado.
# Após escolher, o programa apresentará os números.

# O usuário deverá escolher uma quantidade de dados e o tipo de dado.
from random import randint

quant_dados = int(input('Quantos dados você deseja? '))
print('Qual tipo de dado você deseja?')
print('''[4] d4
[6] d6
[8] d8
[10] d10
[12] d12
[20] d20''')

tipo_dado = int(input('Escolha: '))
while tipo_dado not in [4, 6, 8, 10, 12, 20]:
    tipo_dado = int(input('Dado inválido. Por favor, escolha dentre as opções o dado que deseja: '))

# Após escolher, o programa apresentará os números.
while quant_dados > 0:
    print(randint(1,tipo_dado))
    quant_dados -= 1
