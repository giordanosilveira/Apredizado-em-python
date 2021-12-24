"""
Enunciado:

Leia uma matriz 3x3 elementos. Calcule a soma dos elementos que estão abaixo da diagonal principal
"""

from random import randint
matriz = []

# Percorrendo as 'linhas' da matriz
for i in range(3):
    lista = []

    # Percorrendo as 'colunas' da matriz e preechendo com valores gerados aleatóriamente entre um range de 0 a 56
    for j in range(3):
        lista.append(randint(0, 56))

    # Colocando os elementos das colunas nas linhas
    matriz.append(lista)

for lista in matriz:
    print(lista, end='\n')

soma = 0
# Percorre a matriz até somente i = j
for i in range(3):
    # breakpoint()
    for j in range(i):

        # Caso i < j, ou seja, abaixo da diagonal principal, faz a soma
        if j < i:
            soma = soma + matriz[i][j]
print(f'A soma abaixo da diagonal principal é {soma}')
