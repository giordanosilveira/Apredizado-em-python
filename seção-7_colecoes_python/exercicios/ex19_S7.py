"""
Enunciado:

Faça um vetor de tamanho 50 preenchido com o seguinte valor: (i + 5 * i)%(i + 1), sendo i a posição do elemento do
elemento no vetor. Em seguida imprima o vetor, 2 elementos por linha
"""

# laço que compreende 50 elementos que preenche a lista com a fórmula dada
lista = []
for i in range(50):
    lista.append((i + 5 * i) % (i + 1))

# printa a lista de dois em dois elementos por linha
for i in range(50):
    # Pula uma linha a cada dois elementos do vetor (se i = 2, então i % 2 = 0, logo pule uma linha)
    if i % 2 == 0:
        print()
    print(lista[i], end=' ')

