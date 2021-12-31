"""
Enunciado:

Escreva uma função para determinar a quantidade de primos abaixo de N
"""
from math import sqrt


def eh_primo(divisor):

    """
    Verifica se o divisor é um número primo
    :param divisor: possível divisor
    :return: 1 se o número for primo, 0 senão for
    """

    maior_divisor = int(sqrt(divisor))
    # É necessário verificar até a raiz quadrada de um número para ver se é primo
    for i in range(2, maior_divisor + 1):

        # Se for divisível por algum número, não é primo
        if divisor % i == 0:
            # breakpoint()
            return 0
    return 1


def primos_abaixo_n(numero):
    """
    Verifica quantos números primos tem abaixo de n
    :param numero: numero
    :return: Quantidade de números primos abaixo de n
    """
    qntd_primos = 0
    for i in range(2, num + 1):
        if eh_primo(i):
            qntd_primos += 1
    return qntd_primos


num = int(input('Digite um inteiro '))
print(f'A quantidade de primos abaixo de {num} é {primos_abaixo_n(num)}')



