"""
Faça um programa que simula o lançamento de dois dados, d1 e d2, n vezes, e tem como saída o número de cada dado e a
relação entre eles (>,<,==) de cada lançamento
"""
# Para fazer o números aleatórios
import random

n = int(input('Escreva um número '))

# Dados recebem números aleatórios
d1 = random.randint(1, 6)
d2 = random.randint(1, 6)

# Loop que vai de 1 à n
for i in range(1, n):
    print(f'Dado 1: {d1}', end=' ')
    print(f'Dado 2: {d2}')
    # if1s que controlam a relação entre eles
    if d1 == d2:
        print(f'O valor do dado 1: {d1} é igual ao dado 2: {d2}')
    elif d1 < d2:
        print(f'O valor do dado 1: {d1} é menor que o valor do dado 2: {d2}')
    else:
        print(f'O valor do dado 1: {d1} é maior que o valor do dado 2: {d2}')
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
