"""
Listas alinhadas (nested lists)

Alguma linguagens de programação possuem uma estrutura de dados chamadas de arrays:
    - unidimensionais (vetores)
    - multidimencionais (matrizes)

Em python nós temos as listas
numeros = [1, 'b', 3.213, True, 5]

# Exemplos
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz 3 x 3
print(listas)
print(type(listas))

# Acessando os dados
print(listas[0][1])  # num = 2
print(listas[2][1])  # num = 8

# Iterandos com loops em uma lista alinhada
for lista in listas:
    for num in lista:
        print(num)

# List Comprehension
[[print(valor) for valor in lista] for lista in listas]
"""

# outros exemplos

# Gerando um tabuleiro/matrix 3x3
tabuleiro = [[coluna for coluna in range(1, 4)] for linha in range(1, 4)]
print(tabuleiro)

# Gerando jogadas para o jogo da velha
velha = [['X' if num % 2 == 0 else 'O' for num in range(1, 4)] for valor in range(1, 4)]
print(velha)

# Gerando valores iniciais
print([['*' for i in range(1, 4)] for j in range(1, 4)])
