"""
Enunciado:

Escreva um programa que receba como entrada o valor do saque realizado pelo cliente de um banco e retorne quantas notas
de cada valor serão necessárias para atender ao saque com a menor quantidade de notas possível. Serão utilizados notas
de 100, 50, 20, 10, 5, 2 e 1 real.
"""

# tuplas para as cédulas visto que elas não recebem mais nenhum valor
cedulas = [100, 50, 20, 10, 5, 2, 1]

saque = int(input('Escreva o valor sacado '))

conta_notas = 0
i = 0

# Enquanto o saque não chega a 0, continua no laço
while saque != 0:

    # Se der para subtrair de saque, subtraia e o contador de nota aumenta 1
    if saque - cedulas[i] >= 0:
        conta_notas += 1
        saque = saque - cedulas[i]
    # Caso não dê, troca para uma cédula menor
    else:
        if i < 6:
            i += 1
print(f'O menor número de notas para o saque de R${saque},00 é {conta_notas}')

