"""
Enunciado:

Ler dois conjuntos de números reais, armazenando-os em vetores e calcular o produto escalar entre eles. Os conjuntos têm
5 elementos cada. Imprimir os dois conjuntos e o produtos, sendo que o produto escalar é dado por: x1 * y1 + x2 * y2 +
... + xn * yn
"""

import random

# Declarando dois vetores vazios e preenchendo eles com a função append com números gerados aleatoriamente
vetor1 = []
for i in range(5):
    vetor1.append(random.randint(0, 141))

vetor2 = []
for i in range(5):
    vetor2.append(random.randint(0, 141))

print('O primeiro vetor é ', end=' ')
print(*vetor1)

print('O segundo vetor é ', end=' ')
print(*vetor2)

soma = 0
# Fazendo o produto escalar de dois vetores
for i in range(5):
    soma = soma + vetor1[i]*vetor2[i]
print(f'O profuto escalar do vetor1xvetor2 é igual a {soma}')
