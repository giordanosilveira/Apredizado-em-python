"""
Enunciado:

Faça um programa que calcule o desvio padrão de um vetor v contendo n = 10 números, onde m é a media do vetor.

desvio padrão = sqrt(1/(n - 1) * somatório((v[i] -m)^2) de i=1 a n))
"""

"""
Importando a bibliotecas math e randon para, respectivamente, a função raiz quadrada e para gerar números aleatórios
"""
import math
import random

# Gerando um vetor de números aleatórios que variam de -8 a 100
numeros = list()
for i in range(10):
    numeros.append(random.randint(-8, 100))

print(numeros)

# Fazendo a media dos números da lista. A função faz a soma da lista, contanto que todos os dados sejam números
media = sum(numeros)/10

# For que faz o somatório solicitado
somatorio = 0
for num in numeros:
    somatorio = somatorio + (num - media)**2

# Calculando o desvio padrão
desvio_padrao = math.sqrt(1/(10 - 1) * somatorio)
print(f'O desvio padrão é {desvio_padrao}')

