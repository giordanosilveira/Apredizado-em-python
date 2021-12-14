"""
Enunciado:
Faça um programa que receba do usuário um vetor que contém 10 posições. Em seguida deverá ser impresso o maior e o menor
valor desse vetor
"""

# Declarando um vetor (lista)
vetor = []

# Laço para 10 elementos
print('Digite 10 números')
for i in range(10):
    # Leitura e conversão de uma entrada em float. Depois a adição dele na lista
    vetor.append(float(input()))

# Funções prontas que mostram o máximo e o mínimo de um lista de números
print(max(vetor))
print(min(vetor))
