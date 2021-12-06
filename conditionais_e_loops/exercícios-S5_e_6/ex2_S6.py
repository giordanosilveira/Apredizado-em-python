"""
Escreva um programa que escreva na tela, de 1 até 100, de 1 em 1, 3 vezes. A primeira vez deve usar a estrutura de
repetição for, a segunda e a terceira while
"""

# Escrevendo de forma crescente de 1 a 100 três vezes
for n in range (1, 100 + 1):
    print(f'{n}', end=' ')
print()

n = 1
while n <= 100:
    print(n, end=' ')
    n = n+1

print()
n = 1
while n <= 100:
    print(n, end=' ')
    n = n+1
