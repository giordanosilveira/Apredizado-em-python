"""
Enunciado:
Faça uma função que recebe, por parâmetro, 2 vetores de 10 elementos inteiros e que calcule e retorne o vetor união dos dois primeiros
"""

from random import randint


def gera_lista(tam=10):
    """Gera uma lista de números inteiros

    Args:
        tam (int, optional): Tamanho da lista. Defaults to 10.

    Returns:
        lista [lista de inteiro]: A lista gerada
    """
    lista = []
    for i in range(10):
        lista.append(randint(0, 100))
    return lista


def uniao_lista(lista1, lista2):
    """Fazendo a uniao de duas listas

    Args:
        lista1 ([lista de inteiros]): Uma lista de inteiros
        lista2 ([lista de inteiros]): Uma lista de inteiros

    Returns:
        uniao [lista de inteiro]: A uniao das duas listas
    """
    
    # Transformando as duas listas em conjuntos visto que conjuntos não permitem repetidos
    conj1 = set(lista1)
    conj2 = set(lista2)
    
    # Usa a função union() para criar um conjunto que é a união dos dois conjuntos
    uniao = conj1.union(conj2)
    
    return list(uniao)
c

if __name__ == '__main__':
    lista1 = gera_lista()
    print(f'lista 1: {lista1}')
    lista2 = gera_lista()
    print(f'lista 2: {lista2}')
    
    uniao = uniao_lista(lista1, lista2)
    print(f'A união das duas lista {uniao}')
