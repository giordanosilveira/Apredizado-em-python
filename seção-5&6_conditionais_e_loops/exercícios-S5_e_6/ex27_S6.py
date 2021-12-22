"""
Enuciado:

Em matemática, o número harmonico designado por H(n) define-se como sendo a soma da série harmônica: H(n) = 1 + 1/2 +1/3
+ 1/4 + ... + 1/n
Faça um programa que leia um valor n inteiro e positivo e apresente o valor de H(n)
"""

n = int(input('Escreva um número'))
soma = 0
#  Loop de 1 até n
for i in range(1, n+1):
    soma = soma + 1/i
print(soma)
