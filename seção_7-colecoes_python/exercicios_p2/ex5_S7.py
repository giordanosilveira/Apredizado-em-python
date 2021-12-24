"""
Enunciado

Leia uma matriz 5x5. Leia também um valor X. O programa deverá fazer uma busca desse valor na matriz e, ao final,
escrever a localização (linha e coluna) ou uma mensagem de não encontrado
"""

from random import randint
matriz = []

# Percorrendo as 'linhas' da matriz
for i in range(5):
    lista = []

    # Percorrendo as 'colunas' da matriz e preechendo com valores gerados aleatóriamente entre um range de 0 a 56
    for j in range(5):
        lista.append(randint(0, 56))

    # Colocando os elementos das colunas nas linhas
    matriz.append(lista)

for lista in matriz:
    print(lista, end='\n')

# Percorrendo a matriz
busca = int(input('Qual número você procura dentro da matriz? '))
for i, lista in enumerate(matriz):
    for j, num in enumerate(lista):

        # se achou o número, printa a mensagem e encerra o programa
        if busca == num:
            print(f'O número {busca} está na linha {i + 1} e na coluna {j + 1}')
            quit()
print(f"O número {busca} não está na matriz")