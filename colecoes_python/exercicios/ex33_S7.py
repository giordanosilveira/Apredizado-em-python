"""
Enunciado:

Faça um programa que leia um vetor de 15 posições e o compacte, ou seja, elimine as posições com valor 0. Para isso,
todos os elementos á frente do valor zero, devem ser movidos uma posição atrás do vetor
"""
import random

# Gerando um vetor de números aleatórios que variam de 0 a 15
numeros = list()
for i in range(15):
    numeros.append(random.randint(0, 15))

print(f'Lista normal {numeros}')

# Percorrendo todos os elementos da lista
for i in range(len(numeros)):

    # Caso ache um 0 na lista, acha a posição desse 0 e o remove
    if 0 in numeros:
        pos = numeros.index(0)  # Index retorna a posição do valor passado
        numeros.pop(pos)  # Pop o dado informado do vetor e puxa para a esquerda os elementos à frente do retirado


print(f'A lista compactada {numeros}')

