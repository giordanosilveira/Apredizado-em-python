"""
Faça um programa que leia 10 inteiros positivos, ignorando não positivos, e imprima sua média.
"""

"""
Resolução:

comparador controla o número de inteiros positivos lidos
soma controla a soma dos números inteiros

Enquanto não foi lido 10 números inteiro, continue lendo números

Ao sair do Loop, divída por 10.
"""
comparador = 0
soma = 0
while comparador < 10:
    numero = int(input('Digite um número\n'))
    if numero >= 0:
        soma = soma + numero
        comparador += 1
print(f'A média é: {soma/10}')
