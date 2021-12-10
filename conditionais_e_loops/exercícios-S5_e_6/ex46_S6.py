"""
Enunciado:

Faça um programa que gera um número aleatório de 1 a 1000. O usuário deve tentar acertar qual o número foi gerado, a
cada tentativa o programa deverá informar se o chute é menor ou maior que o número gerado. O programa acaba quando o
usuário acerta o número gerado.
"""

# Para fazer o números aleatórios
import random

# Gerador de número aleatório
n = random.randint(1, 1000)


tentativa = int(input('Tente adivinhar o número '))
# Enquanto o usuário não acertar, continua no laço
while tentativa != n:
    # if's que informam ao usuário se o número informado é maior ou menor do que o gerado
    if tentativa < n:
        print('O número informado é menor')
    elif tentativa > n:
        print('o número informado é maior')
    tentativa = int(input())
print(f'Parabéns você acertou. O número gerado foi {n}')
