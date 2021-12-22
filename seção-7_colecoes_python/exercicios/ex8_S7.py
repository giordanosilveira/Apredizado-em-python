"""
Enunciado:

Crie um programa que lê 6 valores inteiros e, em seguida, mostre na tela os valores lidos na ordem inversa
"""

# Declarando um vetor vazio
vetor = []

# Preenchendo ele com 6 elementos
for i in range(6):
    vetor.append(int(input()))

# Revertendo ele com a função reverse()
vetor.reverse()
print(vetor)

