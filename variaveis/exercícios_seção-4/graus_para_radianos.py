"""
Leia um ângulo em gruas e apresente-o convertido em radianos
"""

pi = 3.14  # Definindo pi

# lendo do stdin um ângulo em graus(float) e passando para ângulo em radianos
graus = float(input('Digite um angulo em graus\n'))
print(f'O ângulo em radianos é: {graus*pi/180}')
