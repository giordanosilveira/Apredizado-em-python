"""
Enunciado:

Faça um programa que leia um valor de N inteiro e positivo, calcule e mostre o valor E, conforme a fórmula a seguir
                        E(n) = 0 + 1/2! + 1/3! + 1/4! + ... + 1/n!
"""
n = int(input('Escreva um número '))
soma = 0
# Loop que vai de dois até N (começa em dois pois o somatório começa com 1/2!)
for i in range(2, n+1):
    mult = 1
    # Essa função faz o fatorial do número (a variável i contém o valor para o fatorial)
    for k in range(1, i+1):
        mult = mult * k
    print(f'O fatorial de {i} é {mult}')
    soma = soma + 1/mult  # Função E(n)
print(f'O somatório da função E é {soma}')
