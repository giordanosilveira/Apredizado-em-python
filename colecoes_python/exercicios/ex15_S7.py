"""
Enunciado:

Leia um vetor com 20 números inteiros. Escreva os elementos do vetor eliminando os elementos repitidos
"""

import random

# Declarando um vetor vazio e preenchendo ele com a função append com números gerados aleatoriamente
vetor = []
for i in range(20):
    vetor.append(random.randint(0, 50))

print(f' O Vetor com elementos repitidos é {vetor}')

# transformando a lista em um conjunto visto que conjuntos internamente em python não admitem repetição
conjunto = set(vetor)
print('O vetor sem elementos repitidos é ')
print(*conjunto)
