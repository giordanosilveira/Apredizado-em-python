"""
Enunciado:

Leia 10 números inteiros e armazene em um vetor. Em seguida escreva os elementos que são primos e suas respectivas
posições do vetor
"""
import math
import random

# Gerando um vetor de números aleatórios que variam de -8 a 100
numeros = list()
for i in range(10):
    numeros.append(random.randint(0, 100))

# Laço que percorre todos os elementos da lista
numeros_primos = list()
for i, num in enumerate(numeros):

    # Laço que checa se um número é primo.
    ehprimo = True
    for j in range(2, int(math.sqrt(num)) + 1):

        # Se achar um divisor o número não é primo
        if num % j == 0:
            ehprimo = False

    # Se não encontrou nenhum divisor o número é primo, então guarda a posição original dele em uma outra lista
    if ehprimo:
        numeros_primos.append(i)

for pos in numeros_primos:
    print(f'Existe um primo {numeros[pos]} na posição {pos} do vetor{numeros} ')

