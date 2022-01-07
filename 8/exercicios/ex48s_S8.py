"""
Enunciado:
Faça uma função que receba uma matriz de 3 x 3 elementos. Calcule a soma dos elementos que estão acima da diagonal principal

"""

def le_matriz(tam=3):
    """Lê o input do usuário e o coloca numa matriz

    Returns:
        matriz: a matriz feita pelos inputs do usuário
    """
    matriz = []
    print('Digite os valores da matriz')
    for i in range(tam):
        linha = []
        for j in range(tam):
            linha.append(int(input()))
        matriz.append(linha)
    return matriz


def soma_acima_diag_principal(matriz):
    """Soma os números acima da diagonal principal.

    Args:
        matriz (matriz de inteiros): Uma matriz de números inteiros

    Returns:
        Soma: A soma dos elementos da diagonal principal
    """
    soma = 0
    for i in range(3):
        j = i  + 1 # Os elementos da diagonal são quando i=j. j = 1 + 1 para não somar a diagonal principal
        while j < 3:
            soma = soma + matriz[i][j]
            j = j + 1
    return soma


if __name__ == "__main__":
    matriz = le_matriz()
    soma = soma_acima_diag_principal(matriz)
    print('Matriz: ')
    print(*matriz, sep='\n')
    print(f'A soma acima da diagonal principal é igual a {soma}')

    

        



        
            



