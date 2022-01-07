"""
Enunciado:
Escreva uma função que recebe uma matriz quadrada de ordem N e calcule a sua trasposta (se B é a matriz transposta de A então ai=bji)
"""

from ex48s_S8 import le_matriz


def transposta(matriz, tam):
    """Faz a transposta de uma matriz

    Args:
        matriz (Matriz de inteiros): Uma matriz quadrada de dados com valores inteiros
        tam (int): tamanho da matriz quadrada

    Returns:
        m_transposta: a matriz transposta
    """
    m_transposta = matriz.copy()
    for i in range(tam - 1):
        j = i + 1
        while j < tam:
            aux = m_transposta[i][j]
            m_transposta[i][j] = m_transposta[j][i]
            m_transposta[j][i] = aux
            j = j + 1
    return m_transposta
        
if __name__ == '__main__':
    tam = int(input('Qual o tamanho da matriz quadrada ?'))
    matriz = le_matriz(tam)
    print('Matriz Original:')
    print(*matriz, sep='\n')
    matriz = transposta(matriz, tam)
    print('Matriz Transposta:')
    print(*matriz, sep='\n')
    
