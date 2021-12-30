"""
Enunciado:

Faça uma função e um programa de teste para o cálculo do volume de uma esfera. Sendo que o raio é passado por
parâmetro.

V = 4/3*pi*R³
"""
from math import pi


def testa_entrada():
    """
    Testa a entrada do usuário para ver se é um valor válido
    :return: 1, se a entrada é válida. 0, se é inválida.
    """
    try:
        global raio_esfera
        raio_esfera = float(input('Qual o tamanho do raio da esfera ? '))
    except ValueError:
        return 0
    else:
        return 1


def calcula_volume_esfera(raio, p=3.14):
    """
    Calcula o volume da esfera
    :param raio: Raio da esfera
    :param p: Número pi
    :return: O volume da esfera
    """
    return 4/3*p*raio**3


raio_esfera = None
# Permanece no laço enquanto o raio não for válido
while not testa_entrada():
    print('Valor inválido. O Raio precisa ser um número ')

print(f'O volúme da esfera é {calcula_volume_esfera(raio_esfera)}')




