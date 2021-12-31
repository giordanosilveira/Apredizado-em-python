"""
Enunciado:

Escreva um programa que leia um número inteiro positivo e em seguida imprima n linhas do triângulo de Pascal
1
1 1
1 2 1
1 3 3 1
"""

n_linhas = int(input('Quantas linhas do triângulo de pascal você quer imprimir: '))

# Inicializando as listas para ficar mais fácil
lista1 = [1 if n == 0 else 0 for n in range(n_linhas + 1)]
lista2 = [0 for n in range(n_linhas + 1)]

print(lista1[0])
# Percorre as linhas
for i in range(1, n_linhas):

    # Percorre o vetor responsável por aquela linha
    # range(i + 1) para modificar a última posição, responsável pela última coluna da linha
    for j in range(i + 1):

        # A lista responsável pela linhas ímpares é a lista 2
        if i % 2 == 1:

            # A coluna inicial da linha é sempre 1
            if j == 0:
                lista2[j] = 1
                print(lista2[j], end=' ')
            # A coluna final da linha é sempre 1
            elif j == i:
                lista2[j] = 1
                print(lista2[j], end=' ')
            # Caso seja uma intermediária recebe a coluna da linha anterior + coluna - 1 da linha anterior
            else:
                lista2[j] = lista1[j] + lista1[j - 1]
                print(lista2[j], end=' ')
        else:
            if j == 0:
                lista1[j] = 1
                print(lista1[j], end=' ')
            elif j == i:
                lista1[j] = 1
                print(lista1[j], end=' ')
            else:
                lista1[j] = lista2[j] + lista2[j - 1]
                print(lista1[j], end=' ')
    print()


# O algoritmo funciona com duas listas. Uma lista responsável pela linha atual e a outra responsável por atualizar a
# lista atual. Na próxima volta do laço, as listas invertem suas funções.
