"""
Enunciado:
Faça uma função que recebe, por parâmetro, uma matriz A[7][6] e uma linha N e retorne a soma dos elementos dessa linha
"""

from random import randint

def gera_matriz(altura=7, largura=6):
    """Gera uma matriz de números inteiros de tamanho mxn

    Args:
        altura (int, optional): Altura da matriz. Defaults to 7.
        largura (int, optional): largura da matriz. Defaults to 6.

    Returns:
        matriz: a matriz gerada
    """
    matriz = []
    for i in range(altura):
        linha = []
        for j in range(largura):
            linha.append(randint(0, 100))
        matriz.append(linha)
    return matriz, altura, largura
            

def testa_entrada(altura):
    """Checa para ver se o usuário digitou uma linha válida

    Args:
        altura (int): altura da matriz

    Raises:
        IndexError: Se ele digitou um número maior que a altura total, a linha está acima do limite permitido.

    Returns:
        linha [int]: entrada do usuário
    """
    try:
        linha = input('Digite uma linha da matriz ')
        linha = int(linha)
    except ValueError:
        print('O número deve ser um inteiro')
        exit(1)
    else:
        if linha >= altura:
            raise IndexError(f'A altura da matriz é {altura - 1} e você digitou {linha}')
            exit(1)
        return linha


def soma_linha(matrix, linha):
    """Soma uma linha de uma matriz

    Args:
        matrix (matriz de inteiro): A matriz de inteiro
        linha (int): Uma linha dessa matriz

    Returns:
        soma [int]: A soma dessa linha
    """
    return sum(matrix[linha])

   
if __name__ == '__main__':
    matrix, altura, largura = gera_matriz()
    n = testa_entrada(altura)
    soma = soma_linha(matrix, n)
    print(f'A matriz é:')
    print(*matrix, sep='\n')
    print(f'A soma da linha {matrix[n]} da matriz é igual a {soma}')            

 