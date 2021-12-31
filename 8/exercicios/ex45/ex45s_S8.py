"""
Enunciado:

No print da pasta
"""

from random import randint
from math import sqrt


def calcula_media(vetor):
    """
    Função que calcula a média de um vetor de números
    :param vetor: vetor de números
    :return: A média aritimética do vetor
    """
    return sum(vetor)/len(vetor)


def desvio_padrao(vetor):
    """
    Função que calcula o desvio padrão de um vetor de números
    :param vetor: vetor de números
    :return: desvio padrão dos elementos do vetor
    """

    # Calcula a média do vetor primeiramente
    media = calcula_media(vetor)

    # Faz a parte do somatório segundo a fórmula pedida
    soma = 0
    for i in vetor:
        soma = soma + (i - media)**2

    # Retorna desvio padrão seguindo a fórmula
    return sqrt(1/(len(vetor) - 1) * soma)


def le_vetor():
    """
    Função que lê uma lista de tamanho especificado pelo usuário
    :return: retorna a lista lida
    """
    tam = int(input('Quantos valores no vetor '))
    lista = []
    for i in range(tam):
        lista.append(randint(0, 100))
    return lista


vetor = le_vetor()
print(f'O valor do desvio padrão do vetor {vetor} é {desvio_padrao(vetor)}')
