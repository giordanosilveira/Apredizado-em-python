"""
Enunciado:

Faça um programa que leia dois vetores de 10 elementos. Crie um vetor que seja a intersecção entre os dois vetores
anteriores, ou seja, que contém apenas os números que estão em ambos os vetores. Não deve conter números repetidos.
"""
import random

# Gerando um vetor de números aleatórios que variam de 0 a 100
lista1 = list()
for i in range(10):
    lista1.append(random.randint(0, 100))

print(lista1)

# Gerando um vetor de números aleatórios que variam de 0 a 100
lista2 = list()
for i in range(10):
    lista2.append(random.randint(0, 100))

print(lista2)

# Transformando as listas em conjuntos, porque isso já elimina os itens repetidos das listas
conjunto1 = set(lista1)
conjunto2 = set(lista2)

# Criando um terceiro conjunto que contém a intersecção dos conjuntos anteriores
interseccao = conjunto1.intersection(conjunto2)

# Tranformando o conjunto em lista de novo porque o enunciado quis em um vetor
interseccao = list(interseccao)

print(f'Os elemento(os) em comum das listas são(é) {interseccao}')
