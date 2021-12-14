"""
Enunciado:

Faça um programa para ler a nota da prova de 15 alunos e armazene num vetor, calcule e imprima a média geral
"""
import random

# Gerando um vetor vazio e preenchendo com números aleatórios que variam de 0 à 10
vetor = []
for i in range(15):
    vetor.append(random.randint(0, 10))

print(f'A notas dos 15 alunos: {vetor}')

# Fazendo a soma do vetor com a função sum()
soma = sum(vetor)
print(f'A média dos 15 alunos é {soma/15}')
