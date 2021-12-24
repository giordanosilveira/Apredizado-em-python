"""
Enunciado:

Leia uma matriz 4x4 e conte quantos valores maiores que 10 ela possui
"""

# Declarando uma lista vazia
matriz = []
print('Digite os valores da matriz', end='\n')

# Percorrendo as 'linhas' da matriz
for i in range(4):
    lista = []

    # Percorrendo as 'colunas' da matriz
    for j in range(4):
        lista.append(int(input()))

    # Colocando os elementos das colunas nas linhas
    matriz.append(lista)

contador = 0
# Percorrendo a matriz e contando quantos valores maiores que 10 elas possui
for lista in matriz:
    for num in lista:
        if num > 10:
            contador += 1

print(f'A matriz tem {contador} números maiores que 10')

