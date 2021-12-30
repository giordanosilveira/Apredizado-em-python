"""
Enunciado:

Faça uma função que receba um vetor de inteiros e retorne o maior valor.
"""

from random import randint


def maior_valor(vetor):
    """
    Função que retorna o maior valor de um vetor
    :param vetor: vetor de números inteiros
    :return: maior valor do vetor
    """
    return max(vetor)


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
print(f'O maior valor do vetor {vetor} é {maior_valor(vetor)}')
