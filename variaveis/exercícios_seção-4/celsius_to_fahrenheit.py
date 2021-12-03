"""
Leia um número em graus Celsius e apresente-a convertida em gruas Fahrenheit.
"""

# Lendo uma temperatura em Celsius do stdin e convertendo em Fahrenheit
graus_cel = float(input('Digite uma temperatura em graus Celsius\n'))
print(f'A temperatura em gruas fahrenheit é: {graus_cel*(9.0/5.0)+32.0}')
