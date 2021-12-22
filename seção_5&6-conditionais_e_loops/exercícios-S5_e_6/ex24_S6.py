"""
Escreva um programa que leia um número inteiro e calcule a soma de todos os divisores desse número, com exceção dele
próprio
"""

soma = 0
n = int(input('Escreva um número '))
# loop que vai até a metade o número visto que o número não vai ter mais nenhum divisor depois da metade dele a não ser
# ele
for i in range(1, int(n/2) + 1):
    # Se é divisor
    if n % i == 0:
        print(i, end=' ')
        soma = soma + i  # Soma o divisor
print(f'A soma de todos os divisor de {n} é igual a {soma}')
