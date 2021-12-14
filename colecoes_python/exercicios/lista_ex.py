"""

Enunciado:

Faça um programa que possua um vetor denominado A que armazene 6 números inteiros. O programa deve executar os seguintes
passos:
    (a) - Atribua os seguintes valores a esse vetor: 1, 0, 5, -2, -5, -7
    (b) - Armazene em uma variável inteira (simples) a soma entre os valores das posições A[0], A[1], A[5] do vetor e
    mostre na tela esta soma
    (c) - Modifique o vetor na posição 4, atribuindo a esta posição o valor 100
    (d) - Mostre na tela cada valor do vetor A um em cada linha
"""

A = [1, 0, 5, -2, -5, -7]   # (a) - uma simples
soma = A[0] + A[1] + A[5]   # (b) - simples soma de uma lista (vetor)
print(soma)
A[4] = 100                  # (c) - Trocando o valor da posição 4
print(A, sep="\n")          # (d) - uma forma de printar, linha por linha,
                            # itens da lista sem precisar de um laço

