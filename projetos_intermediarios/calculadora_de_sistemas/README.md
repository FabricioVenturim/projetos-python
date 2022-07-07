## Calculadora de Sistemas - Método de Gauss-Jordan

Uma matriz está na forma escalonada reduzida quando ela satisfaz as seguintes condições:

1. O primeiro elemento não-nulo de cada linha não-nula (chamado o pivô da linha) é igual a 1.
2. O pivô da linha i + 1 ocorre à direita do pivô da linha i.
3. Se uma coluna contém um pivô, então todos os outros elementos desta coluna são iguais a 0. 
4. Todas as linhas nulas ocorrem abaixo das linhas não-nulas.

![Matriz escalonada reduzida](https://i.ytimg.com/vi/eYSASx8_nyg/maxresdefault.jpg)

## Utilização

1. Rode o comando `pip install -r requirements.txt` para baixar todas as dependências necessárias.
2. para executar o programa, rode o arquivo `main.py` 

O programa pedirá ao usuário a quantidade de equações que possui o sistema.

Após isso, o programa pedirá que o usuário escreva cada equação. Importante escrever as equações seguindo o padrão:]

```
Digite a 1ª equação: -x + 2y - 4z = 12
Digite a 2ª equaçao: 2x - 3z = 2
Digite a 3ª equaçao: 4y - z + 3x = -3
```

O programa retornará as soluções de cada variável, caso o sistema seja possível e determinado, ou uma mensagem dizendo que o sistema é impossível ou indeterminado. 
