"""
Escreva um programa que declare um inteiro, inicialize-o com 0, e incremente-o de 1000 em 1000, imprimindo seu valor
na tela, até que seu valor seja 100000 (cem mil)
"""

# Começa de 0 e vai até 100.000 de 1000 em 1000
for n in range(0, 100_000 + 1, 1000):
    print(n, end=' ')
