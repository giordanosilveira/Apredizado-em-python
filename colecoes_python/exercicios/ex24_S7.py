"""
Enunciado:

Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo
representando o número do aluno e o segundo representando sua altura em metros. Encontre o aluno mais baixo e o mais
alto. Mostre o número do aluno mais baixo e do mais alto, juntamente com sua alturas
"""

from random import uniform

lista = list()
for i in range(10):
    a = i
    b = round(uniform(1.5, 1.9), 2)
    lista.append({a, b})

print(lista)
lista1 = list()
for i, j in enumerate(lista):
    lista1.append(lista[j])
print(lista1)
