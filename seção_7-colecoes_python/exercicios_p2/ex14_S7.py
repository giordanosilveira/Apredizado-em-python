"""
Enunciado:

Faça um programa para gerar automaticamente números entre 0 e 99 de uma cartela de bingo. Sabendo que cada cartela
deverá ter 5 linhas e de 5 números, gere estes dados de modo a não ter números repitidos dentro de cada cartela. O
programa deverá exibir a cartela gerada.
"""
from random import randint

# inicializando uma lista vazia

cartela = []
linha = []

# Gera uma primeira linha com números diferentes para inicializar a cartela
for i in range(5):
    num = randint(0, 99)

    # Enquanto tiver um número repetido na linha, gera outro número
    while num in linha:
        num = randint(0, 99)
    linha.append(num)

cartela.append(linha)

k = 1
# Enquanto a cartela não dar 5 elementos, permanece no laço
while k != 5:

    # Gera uma linha com números diferentes
    linha = []
    for i in range(5):
        num = randint(0, 99)
        while num in linha:
            num = randint(0, 99)
        linha.append(num)

    # Percorre cada elemento da linha criada
    m = 0
    while m < len(linha):

        # Checa para ver se não acha um elemento igual em cada linha da cartela, caso não haja adiciona essa linha na
        # cartela
        j = 0
        while j < len(cartela):

            # Caso ache, gera uma nova linha de elementos
            while linha[m] in cartela[j]:

                linha = []
                for i in range(5):
                    num = randint(0, 99)
                    while num in linha:
                        num = randint(0, 99)
                    linha.append(num)
                m = 0
                j = 0

            j += 1
        m += 1

    cartela.append(linha)   # adiciona a linha na cartela
    k += 1

for i in range(len(cartela)):
    print(cartela[i])