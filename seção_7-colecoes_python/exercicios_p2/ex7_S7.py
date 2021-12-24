"""
Enunciado:

Gerar e imprimir uma matriz de tamanho 10x10, onde seus elementos são da forma:
A[i][j] = 2i + 7j - 2 se i < j;
A[i][j] = 3i^2 - 1 se i = j;
A[i][j] = 4i^3 - 5j^2 + 1 se i > j;
"""

# Só percorri e preenchi a matriz com as regras pedidas
matriz = []
for i in range(10):
    linha = []
    for j in range(10):
        if i < j:
            linha.append(2*i + 7*j - 2)
        elif i == j:
            linha.append(3*i**2 - 1)
        else:
            linha.append(4*i**3 - 5*j**2 + 1)
        matriz.append(linha)
    print(linha, end='\n')
