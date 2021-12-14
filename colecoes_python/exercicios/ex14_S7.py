"""
Enunciado:

Faça um programa que leia um vetor de 10 posições e verifique se existem valores iguais e os escreva na tela
"""

import random

# Declarando um vetor vazio e preenchendo ele com a função append com números gerados aleatoriamente
vetor = []
for i in range(10):
    vetor.append(random.randint(0, 141))

print(vetor)

# Busca simples: compara o valor da posição atual com todos do vetor, começando na posição atual + 1
for i in range(10):
    for j in range(i+1, 10):
        if vetor[i] == vetor[j]:
            print(f'Já existe um {vetor[i]} na lista {vetor} na posição {j}')
